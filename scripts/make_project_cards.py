import os

CARD_TEMPLATE = """<svg viewBox="0 0 760 280" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{name} project card">
  <defs>
    <linearGradient id="wood{idx}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1c1410"/>
      <stop offset="100%" stop-color="#100c0a"/>
    </linearGradient>
    <linearGradient id="metal{idx}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2a2a2a"/>
      <stop offset="100%" stop-color="#1a1a1a"/>
    </linearGradient>
  </defs>

  <!-- workbench surface -->
  <rect width="760" height="280" fill="url(#wood{idx})"/>
  <g stroke="#000" stroke-opacity="0.25" stroke-width="1">
    <line x1="0" y1="60" x2="760" y2="60"/>
    <line x1="0" y1="220" x2="760" y2="220"/>
  </g>

  <!-- the product chassis card -->
  <rect x="24" y="24" width="712" height="232" rx="6" fill="url(#metal{idx})" stroke="{accent}" stroke-width="1.5"/>
  <rect x="36" y="36" width="688" height="208" rx="4" fill="none" stroke="#333" stroke-width="1"/>

  <!-- rivets -->
  <circle cx="48" cy="48" r="3" fill="#444"/>
  <circle cx="712" cy="48" r="3" fill="#444"/>
  <circle cx="48" cy="232" r="3" fill="#444"/>
  <circle cx="712" cy="232" r="3" fill="#444"/>

  <!-- status LED -->
  <circle cx="680" cy="60" r="6" fill="{status_color}">
    <animate attributeName="opacity" values="1;0.4;1" dur="1.8s" repeatCount="indefinite"/>
  </circle>
  <text x="660" y="64" text-anchor="end" font-family="'JetBrains Mono', monospace" font-size="11" fill="{status_color}" letter-spacing="1">{status}</text>

  <!-- name plate -->
  <text x="56" y="78" font-family="'JetBrains Mono', monospace" font-size="26" font-weight="700" fill="#F5F5F0">{name}</text>
  <text x="56" y="100" font-family="'JetBrains Mono', monospace" font-size="13" fill="#9a9a9a">{tagline}</text>

  <!-- divider -->
  <line x1="56" y1="116" x2="704" y2="116" stroke="#333" stroke-width="1"/>

  <!-- spec rows -->
  <text x="56" y="140" font-family="'JetBrains Mono', monospace" font-size="11" fill="{accent}" letter-spacing="1">VERSION</text>
  <text x="56" y="158" font-family="'JetBrains Mono', monospace" font-size="14" fill="#e0e0e0">{version}</text>

  <text x="220" y="140" font-family="'JetBrains Mono', monospace" font-size="11" fill="{accent}" letter-spacing="1">STACK</text>
  <text x="220" y="158" font-family="'JetBrains Mono', monospace" font-size="13" fill="#e0e0e0">{stack}</text>

  <text x="56" y="190" font-family="'JetBrains Mono', monospace" font-size="11" fill="{accent}" letter-spacing="1">ROADMAP</text>
  <text x="56" y="208" font-family="'JetBrains Mono', monospace" font-size="12" fill="#bbb">{roadmap}</text>

  <!-- progress bar -->
  <text x="500" y="140" font-family="'JetBrains Mono', monospace" font-size="11" fill="{accent}" letter-spacing="1">BUILD PROGRESS</text>
  <rect x="500" y="148" width="204" height="14" rx="3" fill="#0d0d0d" stroke="#333" stroke-width="1"/>
  <rect x="503" y="151" width="{progress_width}" height="8" rx="2" fill="{accent}"/>
  <text x="704" y="170" text-anchor="end" font-family="'JetBrains Mono', monospace" font-size="12" fill="#e0e0e0">{progress}%</text>

  <!-- serial footer -->
  <text x="704" y="225" text-anchor="end" font-family="'JetBrains Mono', monospace" font-size="10" fill="#555" letter-spacing="1">SN-{idx_padded} — GARAGE BUILD</text>
</svg>
"""

PROJECTS = [
    {
        "name": "ScholarGuard AI",
        "tagline": "Academic integrity verification engine",
        "status": "LIVE",
        "status_color": "#4ADE80",
        "version": "v2.3.0",
        "stack": "Python / FastAPI / LLM",
        "roadmap": "Multi-language support -> Q3",
        "progress": 92,
    },
    {
        "name": "KnowledgeVault AI",
        "tagline": "Enterprise knowledge intelligence platform",
        "status": "ACTIVE BUILD",
        "status_color": "#FFB200",
        "version": "v1.8.0",
        "stack": "GraphRAG / Vector DB / Node",
        "roadmap": "Hybrid search rollout -> in progress",
        "progress": 78,
    },
    {
        "name": "CardioVision AI",
        "tagline": "Computer vision for cardiac diagnostics",
        "status": "RESEARCH",
        "status_color": "#FF7A00",
        "version": "v0.9.1-beta",
        "stack": "PyTorch / OpenCV / CNN",
        "roadmap": "Clinical validation -> ongoing",
        "progress": 65,
    },
    {
        "name": "NextBook",
        "tagline": "Personalized reading recommendation engine",
        "status": "LIVE",
        "status_color": "#4ADE80",
        "version": "v3.1.2",
        "stack": "React / Node / Recommender ML",
        "roadmap": "Social features -> Q4",
        "progress": 88,
    },
]

OUT_DIR = "/home/claude/garage/assets/project-cards"
os.makedirs(OUT_DIR, exist_ok=True)

for idx, p in enumerate(PROJECTS, start=1):
    accent = "#FFB200" if idx % 2 == 1 else "#FF7A00"
    progress_width = round(198 * p["progress"] / 100)
    fname = p["name"].lower().replace(" ", "-")
    svg = CARD_TEMPLATE.format(
        idx=idx, idx_padded=str(idx).zfill(4),
        name=p["name"], tagline=p["tagline"],
        status=p["status"], status_color=p["status_color"],
        version=p["version"], stack=p["stack"], roadmap=p["roadmap"],
        progress=p["progress"], progress_width=progress_width,
        accent=accent,
    )
    with open(os.path.join(OUT_DIR, f"{fname}.svg"), "w") as f:
        f.write(svg)
    print(f"wrote {fname}.svg")
