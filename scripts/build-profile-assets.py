#!/usr/bin/env python3
"""Rebuild the self-contained profile SVGs. Python standard library only."""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parents[1] / 'assets' / 'profile'
OUT.mkdir(parents=True, exist_ok=True)
BG = '#0b111b'
FG = '#edf4fc'
MUTED = '#9aaec5'

def text(x, y, value, size=24, color=FG, weight=400, spacing=0):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}">{escape(value)}</text>'

def svg(name, width, height, title, body):
    value = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title">
<title id="title">{escape(title)}</title>
{body}
</svg>\n'''
    (OUT / name).write_text(value)

hero = '''<style>
.wave { animation: drift 18s linear infinite; }
.wave-back { animation: drift 27s linear infinite reverse; }
.signal-pulse { animation: pulse 3s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }
@keyframes drift { to { transform: translateX(-800px); } }
@keyframes pulse { 50% { opacity: .4; transform: scale(.75); } }
@media (prefers-reduced-motion: reduce) { .wave, .wave-back, .signal-pulse { animation: none; } }
</style><defs>
<linearGradient id="bg" x2="1" y2="1"><stop stop-color="#111c2b"/><stop offset="1" stop-color="#090e17"/></linearGradient>
<linearGradient id="signal"><stop stop-color="#66e6d4"/><stop offset="1" stop-color="#a995ff"/></linearGradient>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#9aaec5" stroke-opacity=".07"/></pattern>
</defs>
<rect width="1200" height="480" rx="24" fill="url(#bg)"/>
<rect x="1" y="1" width="1198" height="478" rx="24" fill="url(#grid)" stroke="#27384b"/>
<g opacity=".16" fill="#a995ff"><path class="wave-back" d="M-800 48 Q-600 108 -400 48 T0 48 T400 48 T800 48 T1200 48 T1600 48 T2000 48 T2400 48 V0H-800Z"/></g>
<g opacity=".13" fill="#66e6d4"><path class="wave" d="M-800 65 Q-600 5 -400 65 T0 65 T400 65 T800 65 T1200 65 T1600 65 T2000 65 T2400 65 V0H-800Z"/></g>
<path d="M48 0H1152" stroke="url(#signal)" stroke-width="4"/>
'''
hero += text(48, 57, 'DOTAN VERETZKY', 20, FG, 700, 3)
hero += text(48, 92, 'SOFTWARE ENGINEERING  /  INTEGRATION QA  /  GAME DEV', 14, MUTED, 400, 1.4)
hero += text(45, 183, 'Systems that connect.', 54, FG, 700, -1.5)
hero += text(45, 250, 'Worlds you can play.', 54, '#66e6d4', 700, -1.5)
hero += text(48, 299, 'API integrations. Practical AI tools. Playable ideas.', 22, MUTED)
# A circuit resolves into a wireframe world: geometric editorial illustration.
hero += '''<g fill="none" stroke-linecap="round" stroke-linejoin="round">
<path d="M765 116H806L837 147H900 M747 193H827L862 228H918 M778 273H817L850 240" stroke="#66e6d4" stroke-width="2" opacity=".6"/>
<path d="M965 84L1100 162V302L965 380L830 302V162Z" stroke="#344459"/>
<path d="M965 113L1074 176V289L965 352L856 289V176Z M856 176L965 239L1074 176 M965 239V352" stroke="url(#signal)" stroke-width="2"/>
<path d="M965 113V239 M856 289L965 239L1074 289" stroke="#a995ff" stroke-opacity=".3" stroke-dasharray="4 7"/>
<ellipse cx="965" cy="239" rx="159" ry="52" transform="rotate(-30 965 239)" stroke="#a995ff" stroke-opacity=".35"/>
</g>
<g fill="#66e6d4"><circle cx="765" cy="116" r="5"/><circle cx="747" cy="193" r="5"/><circle cx="778" cy="273" r="5"/><circle class="signal-pulse" cx="965" cy="239" r="6"/></g>
<circle cx="1074" cy="176" r="6" fill="#a995ff"/>
<path d="M48 393H1152" stroke="#27384b"/>
'''
hero += text(48, 437, 'ZOTA · INTEGRATION QA', 15, '#66e6d4', 700, 1.3)
hero += text(466, 437, "BE'ER SHEVA, ISRAEL", 15, MUTED, 400, 1.3)
hero += text(941, 437, 'SIGNAL / PLAY', 15, '#a995ff', 700, 1.3)
svg('hero.svg', 1200, 480, 'Dotan Veretzky: Systems that connect. Worlds you can play.', hero)

projects = [
 ('video-director', '01 / AI TOOLING', 'Video Director', 'From real footage to finished trailers.', 'Claude Code  /  FFmpeg  /  Python', '#b7a2ff', 'timeline'),
 ('metadata-fetcher', '02 / INTEGRATION ENGINEERING', 'Metadata Fetcher', 'Inspect, audit and export URL metadata.', 'React  /  Node.js  /  API + CI', '#66e6d4', 'nodes'),
 ('orbital-breach', '03 / MULTIPLAYER SYSTEMS', 'Orbital Breach', 'Zero gravity. Two teams. One breach.', 'Three.js  /  TypeScript  /  Colyseus', '#76baff', 'orbit'),
 ('personal-website', '04 / INTERACTIVE WEB', 'Personal Website', 'A portfolio with a city to explore.', 'Next.js  /  React  /  Three.js', '#e8c38c', 'city'),
 ('count-dawn', '05 / GAME JAM', 'Count Dawn', 'Be the monster. Beat the sunrise.', 'Phaser  /  TypeScript  /  Team project', '#ff929d', 'moon'),
 ('beatempie', '06 / ARCADE GAME', 'BeatEmPie', 'Ten pie powers. Seven enemy waves.', 'Phaser  /  TypeScript  /  Team project', '#f5b385', 'pie'),
]
for name, label, title, desc, stack, accent, motif in projects:
    body = f'<rect x="1" y="1" width="598" height="278" rx="18" fill="{BG}" stroke="#2c3c50"/>'
    body += f'<path d="M26 1H150" stroke="{accent}" stroke-width="3"/>'
    body += text(30, 39, label, 14, accent, 700, 1.1)
    body += text(30, 166, title, 36, FG, 700, -0.7)
    body += text(30, 204, desc, 23, MUTED)
    body += '<path d="M30 229H570" stroke="#27384b"/>'
    body += text(30, 257, stack, 16, MUTED)
    art = ''
    if motif == 'timeline':
        for y, xs in [(0, [(0,68),(76,110)]),(23,[(0,115),(123,63)]),(46,[(0,40),(48,90),(146,40)])]:
            for x,w in xs: art += f'<rect x="{x}" y="{y}" width="{w}" height="15" rx="3" fill="{accent}" opacity=".22"/>'
        art += f'<path d="M105 -9V73" stroke="{accent}" stroke-width="2"/><path d="M100 -9H110L105 -3Z" fill="{accent}"/>'
    elif motif == 'nodes':
        art += f'<path d="M20 30H75M95 30H158 M95 30V60H158" fill="none" stroke="{accent}" stroke-width="2"/>'
        for x,y in [(0,15),(75,15),(158,15),(158,45)]: art += f'<rect x="{x}" y="{y}" width="30" height="30" rx="6" fill="{BG}" stroke="{accent}" stroke-width="2"/>'
        art += f'<path d="M83 30L88 35L98 24" fill="none" stroke="{accent}" stroke-width="2"/>'
    elif motif == 'orbit':
        art += f'<ellipse cx="95" cy="30" rx="88" ry="25" fill="none" stroke="{accent}" opacity=".5" transform="rotate(-15 95 30)"/><circle cx="95" cy="30" r="33" fill="none" stroke="{accent}"/><path d="M80 42L101 13L108 48L96 37Z" fill="{accent}"/><circle cx="179" cy="6" r="5" fill="{accent}"/>'
    elif motif == 'city':
        for x,h in [(10,26),(39,49),(70,36),(103,65),(139,39),(169,21)]:
            art += f'<rect x="{x}" y="{65-h}" width="22" height="{h}" fill="{accent}" opacity=".18"/><path d="M{x} 65V{65-h}H{x+22}V65" stroke="{accent}" fill="none"/>'
        art += f'<path d="M0 70H196" stroke="{accent}"/>'
    elif motif == 'moon':
        art += f'<circle cx="109" cy="27" r="34" fill="{accent}"/><circle cx="124" cy="16" r="29" fill="{BG}"/><path d="M0 70H192 M0 61H192" stroke="{accent}" opacity=".4"/><path d="M17 57L30 44L43 57M150 53L163 40L176 53" stroke="{accent}" fill="none" opacity=".7"/>'
    elif motif == 'pie':
        art += f'<ellipse cx="100" cy="37" rx="67" ry="28" fill="{accent}" opacity=".15"/><ellipse cx="100" cy="29" rx="67" ry="26" fill="none" stroke="{accent}" stroke-width="2"/><path d="M33 29L45 64H155L167 29 M62 11L128 50 M90 4L152 41 M50 42L112 5 M76 51L141 12" stroke="{accent}" stroke-width="2" fill="none"/><path d="M23 5L18 -5M172 2L179 -8" stroke="{accent}"/>'
    body += f'<g transform="translate(367 63)">{art}</g>'
    svg(name+'.svg', 600, 280, title+': '+desc, body)
print('Generated', len(list(OUT.glob('*.svg'))), 'SVGs')

# A local animated tagline avoids depending on an external typing-image service.
taglines = ["Software Engineer", "Integration QA Specialist", "Practical AI Tools", "Game Dev Enthusiast", "Always building, always learning"]
tagline = '<svg xmlns="http://www.w3.org/2000/svg" width="760" height="48" viewBox="0 0 760 48" role="img" aria-label="Software engineer, integration QA specialist, AI tools and game development"><style>text{font:600 21px monospace;fill:#66e6d4;opacity:0;animation:rotate 20s infinite}@keyframes rotate{0%,18%{opacity:1}20%,100%{opacity:0}}@media(prefers-reduced-motion:reduce){text{animation:none}text:first-of-type{opacity:1}}</style>'
for index, label in enumerate(taglines):
    tagline += f'<text x="380" y="31" text-anchor="middle" style="animation-delay:{index * 4}s">{escape(label)}</text>'
tagline += '</svg>'
(OUT / "tagline.svg").write_text(tagline)
