if(!self.define){let e,i={};const s=(s,t)=>(s=new URL(s+".js",t).href,i[s]||new Promise((i=>{if("document"in self){const e=document.createElement("script");e.src=s,e.onload=i,document.head.appendChild(e)}else e=s,importScripts(s),i()})).then((()=>{let e=i[s];if(!e)throw new Error(`Module ${s} didn’t register its module`);return e})));self.define=(t,n)=>{const r=e||("document"in self?document.currentScript.src:"")||location.href;if(i[r])return;let o={};const c=e=>s(e,r),l={module:{uri:r},exports:o,require:c};i[r]=Promise.all(t.map((e=>l[e]||c(e)))).then((e=>(n(...e),o)))}}define(["./workbox-1c3383c2"],(function(e){"use strict";self.skipWaiting(),e.clientsClaim(),e.precacheAndRoute([{url:"/index.html",revision:"3a34f2ecb5afe0d14033f6c2daae6640"},{url:"/static/css/main.ae6b75ce.css",revision:null},{url:"/static/js/main.199ebed9.js",revision:null},{url:"/static/js/main.199ebed9.js.LICENSE.txt",revision:"b114cc85da504a772f040e3f40f8e46a"}],{})}));
//# sourceMappingURL=service-worker.js.map
