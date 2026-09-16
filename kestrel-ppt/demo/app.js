'use strict';
const NAMES="person,bicycle,car,motorcycle,airplane,bus,train,truck,boat,traffic light,fire hydrant,stop sign,parking meter,bench,bird,cat,dog,horse,sheep,cow,elephant,bear,zebra,giraffe,backpack,umbrella,handbag,tie,suitcase,frisbee,skis,snowboard,sports ball,kite,baseball bat,baseball glove,skateboard,surfboard,tennis racket,bottle,wine glass,cup,fork,knife,spoon,bowl,banana,apple,sandwich,orange,broccoli,carrot,hot dog,pizza,donut,cake,chair,couch,potted plant,bed,dining table,toilet,tv,laptop,mouse,remote,keyboard,cell phone,microwave,oven,toaster,sink,refrigerator,book,clock,vase,scissors,teddy bear,hair drier,toothbrush".split(",");
const EX=["examples/01-ndrf-staging.jpg","examples/02-launch-dawn.jpg","examples/03-hazards-aerial.jpg","examples/04-night-debris.jpg"];
const S=640, RAW_CONF=.12, IOU_NMS=.45;
const $=id=>document.getElementById(id);
let sess=null, img=null, state=null;

const DI = new DescentInference({slice:S, reinspect:.20, publish:.60, iouMerge:.55});

/* ---- inference on an arbitrary sub-rectangle, boxes returned in image coords */
async function infer(im, sx, sy, sw, sh){
  const c=document.createElement('canvas'); c.width=c.height=S;
  const cx=c.getContext('2d');
  const r=Math.min(S/sw, S/sh), nw=sw*r, nh=sh*r, dx=(S-nw)/2, dy=(S-nh)/2;
  cx.fillStyle='#727272'; cx.fillRect(0,0,S,S);
  cx.drawImage(im, sx,sy,sw,sh, dx,dy,nw,nh);
  const d=cx.getImageData(0,0,S,S).data, f=new Float32Array(3*S*S), px=S*S;
  for(let i=0;i<px;i++){f[i]=d[i*4]/255; f[px+i]=d[i*4+1]/255; f[2*px+i]=d[i*4+2]/255;}
  const res=await sess.run({images:new ort.Tensor('float32',f,[1,3,S,S])});
  const o=res[Object.keys(res)[0]], out=o.data, nb=o.dims[2], nc=o.dims[1]-4;
  const cand=[];
  for(let i=0;i<nb;i++){
    let best=0,bi=0;
    for(let k=0;k<nc;k++){const s=out[(4+k)*nb+i]; if(s>best){best=s;bi=k;}}
    if(best<RAW_CONF) continue;
    const X=out[i],Y=out[nb+i],W=out[2*nb+i],H=out[3*nb+i];
    cand.push({cls:bi,score:best,x:sx+(X-W/2-dx)/r, y:sy+(Y-H/2-dy)/r, w:W/r, h:H/r});
  }
  cand.sort((a,b)=>b.score-a.score);
  const keep=[];                                   // light per-pass NMS
  for(const a of cand){ if(keep.some(b=>b.cls===a.cls&&iou(a,b)>IOU_NMS)) continue; keep.push(a); if(keep.length>=120) break; }
  return keep;
}

async function run(){
  if(!img||!sess) return;
  $('run').disabled=true; $('stage').textContent='pass 1 — full frame…';
  const t0=performance.now();
  const W=img.naturalWidth, H=img.naturalHeight;

  const pass1 = await infer(img, 0,0,W,H);
  const cands = DI.candidates(pass1);
  const crops = DI.planCrops(cands, W, H);
  $('stage').textContent=`pass 2 — descending on ${crops.length} region(s)…`;

  let pass2=[];
  for(const k of crops){
    const w=Math.min(k.w,W), h=Math.min(k.h,H);
    pass2 = pass2.concat(await infer(img, k.x,k.y,w,h));
  }
  const merged = DI.merge([...pass1, ...pass2], crops.length?2:1);
  const ms=performance.now()-t0;

  /* --- evidence grid: RGB + descent are REAL; the rest are user-driven ---- */
  const corr = ()=>{
    const tc=+$('sT').value, bc=+$('sB').value;
    return [
      [1,   .55, tc,  bc ],   // rgb full-frame
      [.55, 1,   tc,  bc ],   // descent pass (same sensor, different scale)
      [tc,  tc,  1,   .05],   // thermal
      [bc,  bc,  .05, 1  ],   // ble / wifi
    ];
  };
  const grid = new EvidenceGrid(
    [{name:'RGB full frame'},{name:'RGB descent'},{name:'Thermal'},{name:'Wi-Fi / BLE'}].map((s,i)=>({...s,corr:corr()[i]})), 32);
  const people = merged.filter(d=>d.cls===0);
  for(const p of people){
    const mx=p.x+p.w/2, my=p.y+p.h/2;
    const llr = Math.log(Math.max(1e-6,p.score)/Math.max(1e-6,1-p.score));
    grid.update(mx,my,0,llr);
    if(p.confirmed) grid.update(mx,my,1,llr*.8);
    const tv=+$('vT').value, bv=+$('vB').value;
    if(tv>0) grid.update(mx,my,2, Math.log(tv/(1-tv+1e-9)));
    if(bv>0) grid.update(mx,my,3, Math.log(bv/(1-bv+1e-9)));
  }
  const cells = grid.cells();

  /* --- route + link budget ------------------------------------------------ */
  const base={x:W/2,y:H};
  /* GSD: at 30 m with a 78 deg HFOV the ground swath is 2*30*tan(39) = 48.6 m,
     so one pixel of this frame is 48.6/W metres. Without this the planner
     thinks every cell is kilometres away and correctly refuses to fly. */
  const mpp = 48.6 / W;
  const route = RoutePlanner.plan(cells.filter(c=>c.p>.5), base,
    {budgetJ:+$('vE').value, jPerM:18, jPerHover:300, kMax:15, metersPerPixel:mpp});
  const recs = merged.filter(d=>d.cls===0).map((d,i)=>({
    id:i, bytes: d.score>.6?8300:300, value:d.score, det:d }));
  const link = LinkBudget.pack(recs, +$('vL').value);

  state={pass1,cands,crops,merged,cells,route,link,grid,ms,W,H,base};
  paint(); report();
  $('run').disabled=false; $('stage').textContent='';
}

function paint(){
  const {crops,merged,route,W,H,base}=state;
  const cv=$('cv'), g=cv.getContext('2d');
  cv.hidden=false; $('ph').hidden=true; cv.width=W; cv.height=H;
  g.drawImage(img,0,0);
  const lw=Math.max(2,W/500), fs=Math.max(13,W/58);
  g.lineWidth=lw; g.font=`600 ${fs}px ui-sans-serif,system-ui,sans-serif`;

  if($('kCrop').checked) for(const k of crops){           // descent windows
    g.save(); g.setLineDash([lw*4,lw*3]); g.strokeStyle='#a855f7';
    g.strokeRect(k.x,k.y,Math.min(k.w,W),Math.min(k.h,H));
    g.fillStyle='#a855f7'; g.fillText('DESCEND', k.x+6, k.y+fs+4); g.restore();
  }
  if($('kRoute').checked && route.order.length){          // optimal tour
    g.save(); g.strokeStyle='#22c55e'; g.lineWidth=lw*1.4; g.setLineDash([lw*3,lw*2]);
    g.beginPath(); g.moveTo(base.x,base.y);
    for(const t of route.order) g.lineTo(t.x,t.y);
    g.lineTo(base.x,base.y); g.stroke(); g.setLineDash([]);
    route.order.forEach((t,i)=>{
      g.fillStyle='#22c55e'; g.beginPath(); g.arc(t.x,t.y,fs*.75,0,7); g.fill();
      g.fillStyle='#04141a'; g.textAlign='center'; g.textBaseline='middle';
      g.fillText(i+1,t.x,t.y); g.textAlign='left'; g.textBaseline='alphabetic';
    });
    g.restore();
  }
  for(const d of merged){                                  // detections
    const person=d.cls===0, col=person?(d.confirmed?'#22d3ee':'#64748b'):'#f59e0b';
    g.strokeStyle=col; g.lineWidth=d.confirmed?lw*1.6:lw; g.strokeRect(d.x,d.y,d.w,d.h);
    const t=`${NAMES[d.cls]} ${d.score.toFixed(2)}${d.confirmed?' ✓':''}`;
    const tw=g.measureText(t).width, th=fs*1.35;
    g.fillStyle=col; g.fillRect(d.x,Math.max(0,d.y-th),tw+10,th);
    g.fillStyle='#04141a'; g.fillText(t,d.x+5,Math.max(th-6,d.y-6));
  }
}

function report(){
  const {pass1,cands,crops,merged,cells,route,link,grid,ms}=state;
  const ppl=merged.filter(d=>d.cls===0), conf=ppl.filter(d=>d.confirmed);
  $('mPass').textContent=`${pass1.length} → ${merged.length}`;
  $('mCrop').textContent=crops.length;
  $('mConf').textContent=conf.length;
  $('mMs').textContent=Math.round(ms)+' ms';

  $('oDet').innerHTML = ppl.length
    ? ppl.slice(0,12).map(d=>`<div><b>person</b> ${d.score.toFixed(2)}
        <span class="${d.confirmed?'ok':'mut'}">${d.confirmed?'confirmed by descent':'single pass'}</span></div>`).join('')
    : '<div class="mut">no person above threshold</div>';

  $('oW').innerHTML = grid.streams.map((s,i)=>{
    const w=grid.w[i], pct=(w*100).toFixed(0);
    return `<div class="wrow"><span>${s.name}</span>
      <span class="bar"><i style="width:${pct}%"></i></span><b>${w.toFixed(3)}</b></div>`;
  }).join('') + `<p class="mut sm">Weights solve <code>Σw = 1</code>. Slide a correlation to 0 and
      that stream's weight rises to 1 — the classical Chair-Varshney rule. Slide it to 0.9 and it
      collapses toward half a vote, because it is no longer telling you anything new.</p>`;

  $('oRoute').innerHTML = route.order.length
    ? `<div>Visits <b>${route.visited}</b> of ${route.considered} candidate cells ·
        <b>${Math.round(route.energy)} J</b> of ${$('vE').value} J · posterior collected
        <b>${route.gain.toFixed(2)}</b></div>
       <p class="mut sm">Exact optimum over 2<sup>${route.considered}</sup> subsets by Held-Karp,
        with return-to-base enforced inside the DP. Greedy nearest-first strands the aircraft.</p>`
    : '<div class="mut">no cell above posterior 0.5 — nothing worth the battery</div>';

  $('oLink').innerHTML = `<div>Sends <b>${link.sent.length}</b> of ${merged.filter(d=>d.cls===0).length}
      records · <b>${link.bytes} B</b> of ${$('vL').value} B · value <b>${link.value.toFixed(2)}</b></div>
    <p class="mut sm">0/1 knapsack, not first-in-first-out. A thumbnail costs 8.3 kB and a bare
      geo-record 300 B, so the optimal packet is usually many bare records and one crop.</p>`;
}

/* ---------------------------------------------------------------- bootstrap */
EX.forEach(src=>{const i=new Image();i.src=src;i.onclick=()=>load(src);$('ex').appendChild(i);});
$('file').onchange=e=>{const f=e.target.files[0]; if(f) load(URL.createObjectURL(f));};
$('run').onclick=run;
for(const id of ['sT','sB','vT','vB','vE','vL'])
  $(id).oninput=e=>{ const o=$(id+'v'); if(o) o.textContent=e.target.value; if(state) run(); };

function load(src){
  const im=new Image(); im.crossOrigin='anonymous';
  im.onload=()=>{ img=im; const cv=$('cv'),g=cv.getContext('2d');
    cv.hidden=false; $('ph').hidden=true; cv.width=im.naturalWidth; cv.height=im.naturalHeight;
    g.drawImage(im,0,0); if(sess) run(); };
  im.src=src;
}

$('st').onclick=()=>{
  const r=selfTest();
  $('oTest').innerHTML=r.map(t=>
    `<div class="${t.pass?'ok':'bad'}">${t.pass?'PASS':'FAIL'} — ${t.n}${t.d?` <span class="mut">[${t.d}]</span>`:''}</div>`
  ).join('')+`<div class="sm mut" style="margin-top:8px">${r.filter(x=>x.pass).length}/${r.length} passed.
    The route and link-budget tests compare against brute-force enumeration.</div>`;
};

(async()=>{
  try{
    ort.env.wasm.wasmPaths='https://cdn.jsdelivr.net/npm/onnxruntime-web@1.20.1/dist/';
    sess=await ort.InferenceSession.create('yolov8n.onnx',{executionProviders:['wasm']});
    $('tag').textContent='model ready — everything below runs in this tab';
    $('run').disabled=false; if(img) run();
  }catch(e){ $('tag').textContent='model failed: '+e.message; }
})();
