const fs=require('fs');
const [,,html,kind,name,code,id,salida]=process.argv;
const t=fs.readFileSync(html,'utf8');
const src=t.match(/<script[^>]*>([\s\S]*?)<\/script>/)[1];
const window={};new Function('window',src)(window);
const r=window.LIB.check(kind,id,fs.readFileSync(salida,'utf8'),name,code);
const bad=r.filter(x=>x);
console.log(bad.length?'FALLA: '+bad.slice(0,5).join(' | '):'OK ('+r.length+' verificaciones, todas correctas)');
