# Fügt in alle Seiten dieselbe Navigationsleiste ein (idempotent, zwischen Markern).
# Breit (ab 1180 px): feste Leiste links. Schmal: Zeile mit Knöpfen oben.
import re, sys, os

ROOT = sys.argv[1]
ITEMS = [  # Datei, Kürzel, kurzer Name (schmal), langer Name (breit), Gruppe
    ('index.html', '⌂', 'Übersicht', 'Übersicht', None),
    ('nachbau_1_loop_labor.html', '1', 'Labor 1', 'Loop-Labor · mit Ziel', 'Video-Labore'),
    ('nachbau_2_ohne_ziel.html', '2', 'Labor 2', 'Ohne Ziel', 'Video-Labore'),
    ('nachbau_4_gedaechtnis.html', '4', 'Labor 4', 'Gedächtnis', 'Video-Labore'),
    ('sporen_labor.html', 'S', 'Sporen', 'Sporen-Labor', 'Gegenprobe'),
    ('ausbreitungs_labor_sir.html', 'A', 'Ausbreitung', 'Ausbreitung (SEIQ)', 'Zum Artikel'),
    ('netzwerk_labor_cluster.html', 'B', 'Netzwerk', 'Netzwerk-Cluster', 'Zum Artikel'),
]

CSS = '''<!--KSNAVCSS--><style>
.ksnav{font:14px/1.4 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased;
  display:flex;gap:6px;align-items:center;overflow-x:auto;padding:10px 16px;background:#0d1320;border-bottom:1px solid #1e293b;white-space:nowrap;scrollbar-width:none}
.ksnav::-webkit-scrollbar{display:none}
.ksnav a{text-decoration:none}
.ksnav .ks-brand{font-weight:800;font-size:13px;color:#e5edf7;margin-right:4px;letter-spacing:.02em}
.ksnav .ks-brand small{display:none}
.ksnav .ks-grp,.ksnav .ks-ext,.ksnav .ks-long{display:none}
.ksnav a.ks-i{display:inline-flex;align-items:center;gap:7px;padding:5px 11px 5px 6px;border-radius:999px;border:1px solid #24324d;background:#111726;color:#cdd9ea;font-size:13px;flex:none}
.ksnav a.ks-i b{display:inline-grid;place-items:center;width:22px;height:22px;border-radius:7px;background:#16213a;color:#60a5fa;font-size:12px;font-weight:800}
.ksnav a.ks-i.on{background:#1d4ed8;border-color:#1d4ed8;color:#fff}
.ksnav a.ks-i.on b{background:rgba(255,255,255,.18);color:#fff}
@media(min-width:1180px){
  body{padding-left:226px}
  .ksnav{position:fixed;z-index:50;left:0;top:0;bottom:0;width:210px;flex-direction:column;align-items:stretch;gap:2px;padding:20px 12px;
    border-bottom:0;border-right:1px solid #1e293b;overflow-y:auto;white-space:normal}
  .ksnav .ks-brand{font-size:15px;margin:0 6px 14px}
  .ksnav .ks-brand small{display:block;font-weight:500;font-size:12px;color:#93a4bd;letter-spacing:0;margin-top:2px}
  .ksnav .ks-grp{display:block;font-size:10.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#64748b;margin:14px 8px 4px}
  .ksnav .ks-short{display:none}.ksnav .ks-long{display:inline}
  .ksnav a.ks-i{border:0;background:transparent;border-radius:9px;padding:6px 8px;font-size:13.5px}
  .ksnav a.ks-i:hover{background:#16213a}
  .ksnav a.ks-i.on{background:#1d4ed8}
  .ksnav .ks-ext{display:block;margin-top:auto;padding-top:16px;border-top:1px solid #1e293b;font-size:12.5px}
  .ksnav .ks-ext a{display:block;color:#93a4bd;padding:3px 8px}
  .ksnav .ks-ext a:hover{color:#e5edf7}
  .wrap > a[href="index.html"]:first-child{display:none !important}   /* „← Alle Labore“: die Leiste ersetzt ihn */
}
</style><!--/KSNAVCSS-->'''

def nav(active):
    out = ['<!--KSNAV--><nav class="ksnav" aria-label="Labore">',
           '<span class="ks-brand">KI-Sporen<small>Nachbau der Video-Labore</small></span>']
    grp = None
    for f, k, short, long, g in ITEMS:
        if g and g != grp:
            out.append(f'<span class="ks-grp">{g}</span>'); grp = g
        on = ' on" aria-current="page' if f == active else ''
        out.append(f'<a class="ks-i{on}" href="{f}"><b>{k}</b><span class="ks-short">{short}</span><span class="ks-long">{long}</span></a>')
    out.append('<div class="ks-ext"><a href="https://youtu.be/M7zLg-YNcyU" target="_blank" rel="noopener">Video auf YouTube ↗</a>'
               '<a href="https://www.anthropic.com/research/self-replicating-ai" target="_blank" rel="noopener">Anthropic-Artikel ↗</a></div>')
    out.append('</nav><!--/KSNAV-->')
    return ''.join(out)

for f, *_ in ITEMS:
    p = os.path.join(ROOT, f); t = open(p, encoding='utf-8').read()
    t = re.sub(r'<!--KSNAVCSS-->.*?<!--/KSNAVCSS-->', '', t, flags=re.S)
    t = re.sub(r'<!--KSNAV-->.*?<!--/KSNAV-->', '', t, flags=re.S)
    assert t.count('</head>') == 1, f
    t = t.replace('</head>', CSS + '\n</head>')
    m = re.search(r'<body[^>]*>', t); assert m, f
    t = t[:m.end()] + '\n' + nav(f) + t[m.end():]
    open(p, 'w', encoding='utf-8').write(t)
    print('Leiste eingefügt:', f)
