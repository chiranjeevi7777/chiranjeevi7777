import os

TEMPLATE = """<svg viewBox="0 0 1200 140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{aria} section sign">
  <defs>
    <linearGradient id="signGrad{idx}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1d1d1d"/>
      <stop offset="100%" stop-color="#121212"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="140" fill="#0a0a0a"/>
  <line x1="{cx1}" y1="0" x2="{cx1}" y2="30" stroke="#444" stroke-width="3"/>
  <line x1="{cx2}" y1="0" x2="{cx2}" y2="30" stroke="#444" stroke-width="3"/>
  <rect x="{rx}" y="30" width="{rw}" height="80" rx="4" fill="url(#signGrad{idx})" stroke="{accent}" stroke-width="2"/>
  <rect x="{rx2}" y="42" width="{rw2}" height="56" rx="2" fill="none" stroke="#333" stroke-width="1"/>
  <text x="600" y="72" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="28" font-weight="700" fill="#F5F5F0" letter-spacing="4">{title}</text>
  <text x="600" y="94" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="12" fill="{accent}" letter-spacing="3">{subtitle}</text>
  <circle cx="{rx2}" cy="50" r="3" fill="{accent2}"/>
  <circle cx="{rx2_end}" cy="50" r="3" fill="{accent2}"/>
  <circle cx="{rx2}" cy="90" r="3" fill="{accent2}"/>
  <circle cx="{rx2_end}" cy="90" r="3" fill="{accent2}"/>
</svg>
"""

# title, subtitle, filename
SECTIONS = [
    ("ABOUT ME", "OPERATOR PROFILE", "sign-about"),
    ("THE WORKBENCH", "ACTIVE BUILDS", "sign-workbench"),
    ("TOOL WALL", "EQUIPMENT RACK", "sign-tools"),
    ("PROTOTYPE LAB", "EXPERIMENTAL R&amp;D", "sign-lab"),
    ("FACTORY DASHBOARD", "LIVE TELEMETRY", "sign-dashboard"),
    ("PROJECT SHOWCASE", "SHIPPED PRODUCTS", "sign-showcase"),
    ("SHIPPING DOCK", "DEPLOYED &amp; LIVE", "sign-shipping"),
    ("ACHIEVEMENT WALL", "TROPHY CASE", "sign-achievements"),
    ("FACTORY CONVEYOR", "CONTINUOUS DELIVERY", "sign-conveyor"),
    ("COFFEE CORNER", "BREAK ROOM", "sign-coffee"),
    ("GARAGE CLOSING", "END OF SHIFT", "sign-footer"),
]

OUT_DIR = "/home/claude/garage/assets/dividers"
os.makedirs(OUT_DIR, exist_ok=True)

for idx, (title, subtitle, fname) in enumerate(SECTIONS):
    rw = max(560, len(title) * 26 + 160)
    rx = (1200 - rw) // 2
    rw2 = rw - 24
    rx2 = rx + 12
    rx2_end = rx2 + rw2
    accent = "#FFB200" if idx % 2 == 0 else "#FF7A00"
    accent2 = "#FF7A00" if idx % 2 == 0 else "#FFB200"
    svg = TEMPLATE.format(
        aria=title.title(),
        idx=idx,
        cx1=560, cx2=640,
        rx=rx, rw=rw, rx2=rx2, rw2=rw2, rx2_end=rx2_end,
        accent=accent, accent2=accent2,
        title=title, subtitle=subtitle,
    )
    with open(os.path.join(OUT_DIR, f"{fname}.svg"), "w") as f:
        f.write(svg)
    print(f"wrote {fname}.svg")
