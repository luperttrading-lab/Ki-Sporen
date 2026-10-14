# Packt alle Seiten in EINE HTML-Datei (zum Weitergeben ohne ZIP).
# Jede Seite steht im Klartext in einem <script type="text/plain">-Block und wird beim Aufruf in einem
# eigenen Rahmen (iframe) angezeigt, damit sich Stile, Skripte und Kennungen der Seiten nicht stören.
# Aufruf: python3 tools/einzeldatei.py <Projektordner> <Ziel.html>
import sys, os, re

ROOT, OUT = sys.argv[1], sys.argv[2]
PAGES = ['index.html', 'nachbau_1_loop_labor.html', 'nachbau_2_ohne_ziel.html', 'nachbau_4_gedaechtnis.html',
         'sporen_labor.html', 'ausbreitungs_labor_sir.html', 'netzwerk_labor_cluster.html']

# In jede Seite: Klicks auf Links zu anderen Seiten an den Rahmen melden statt eine Datei zu laden
HOOK = ('<script>document.addEventListener("click",function(e){var a=e.target.closest&&e.target.closest("a[href]");'
        'if(!a)return;var h=a.getAttribute("href");if(/^[a-z0-9_]+\\.html$/i.test(h)){e.preventDefault();'
        'parent.postMessage({ksGo:h},"*");}},true);</script>')

blocks = []
for f in PAGES:
    t = open(os.path.join(ROOT, f), encoding='utf-8').read()
    assert t.count('</body>') == 1, f
    t = t.replace('</body>', HOOK + '</body>')
    assert not re.search(r'<\\/script|<\\!--', t, re.I), f
    t = re.sub(r'</script', r'<\\/script', t, flags=re.I).replace('<!--', '<\\!--')   # damit der Block nicht vorzeitig endet
    blocks.append(f'<script type="text/plain" data-seite="{f}">\n{t}\n</script>')

shell = '''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>KI-Sporen · Labore</title>
<!--
  KI-Sporen: Nachbau der Labore aus dem Video „KI repliziert sich selbst – Anthropic warnt vor Katastrophe“.
  Diese eine Datei enthält 7 Seiten. Jede Seite steht weiter unten im Klartext in einem eigenen Block
  (<script type="text/plain">) und wird beim Öffnen in einem Rahmen angezeigt. Die Datei lädt nichts aus dem
  Internet nach und sendet nichts. Externe Links (YouTube, Anthropic) öffnen sich nur auf Klick in einem neuen Tab.
-->
<style>
  html,body{margin:0;height:100%;background:#0a0e17}
  iframe{position:fixed;inset:0;width:100%;height:100%;border:0;display:none;background:#0a0e17}
  iframe.on{display:block}
  .nojs{color:#e5edf7;font:16px/1.5 sans-serif;padding:24px;max-width:640px}
</style>
</head>
<body>
<noscript><p class="nojs">Diese Datei zeigt ihre Seiten mit JavaScript an. Bitte im Browser öffnen (Chrome, Edge, Firefox, Safari).</p></noscript>
''' + '\n'.join(blocks) + '''
<script>
(function(){
  var src={},frames={},cur=null;
  document.querySelectorAll('script[data-seite]').forEach(function(s){
    src[s.getAttribute('data-seite')]=s.textContent.replace(/<\\\\\\/script/gi,'</script').replace(/<\\\\!--/g,'<!--');});
  function show(f,push){
    if(!src[f])f='index.html';
    if(!frames[f]){var fr=document.createElement('iframe');fr.title=f;fr.srcdoc=src[f];
      fr.addEventListener('load',function(){try{if(cur===f)document.title=fr.contentDocument.title;}catch(e){}});
      document.body.appendChild(fr);frames[f]=fr;}
    for(var k in frames)frames[k].classList.toggle('on',k===f);
    cur=f;try{document.title=frames[f].contentDocument.title||document.title;}catch(e){}
    var h='#'+f.replace(/\\.html$/,'');
    if(push&&location.hash!==h)history.pushState(null,'',h);
  }
  window.addEventListener('message',function(e){if(e.data&&e.data.ksGo)show(e.data.ksGo,true);});
  window.addEventListener('popstate',function(){show((location.hash.slice(1)||'index')+'.html',false);});
  show((location.hash.slice(1)||'index')+'.html',false);
})();
</script>
</body>
</html>
'''
open(OUT, 'w', encoding='utf-8').write(shell)
print(OUT, os.path.getsize(OUT) // 1024, 'KB')
