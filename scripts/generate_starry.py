#!/usr/bin/env python3
"""Regenerate starry-contributions.svg from the GitHub contribution calendar.

Deterministic by design: every star's position, size, brightness, and twinkle
timing is derived from sha256(date:count), so identical contribution data
always produces a byte-identical SVG. No RNG, no wall-clock input.

Usage:  GITHUB_TOKEN=<token> python scripts/generate_starry.py
"""

import hashlib
import json
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

LOGIN = "COMMENTERTHE9"
WIDTH, HEIGHT = 745, 101
PAD_X, PAD_Y = 10.0, 8.0
MAX_BYTES = 200 * 1024

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount weekday } }
      }
    }
  }
}
"""


def fetch_calendar(token: str) -> dict:
    body = json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": f"{LOGIN}-starry-generator",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.loads(resp.read())
    if payload.get("errors"):
        sys.exit(f"ERROR: GraphQL query failed: {payload['errors']}")
    user = payload.get("data", {}).get("user")
    if user is None:
        sys.exit(
            "ERROR: token cannot read the contribution calendar "
            f"for {LOGIN} (user resolved to null)."
        )
    return user["contributionsCollection"]["contributionCalendar"]


def star(day: dict, week_idx: int, cell_w: float, cell_h: float) -> str:
    count = day["contributionCount"]
    h = hashlib.sha256(f"{day['date']}:{count}".encode()).digest()
    cx = PAD_X + (week_idx + 0.5) * cell_w + (h[0] / 255 - 0.5) * cell_w * 0.8
    cy = PAD_Y + (day["weekday"] + 0.5) * cell_h + (h[1] / 255 - 0.5) * cell_h * 0.8
    r = 0.4 + min(count, 20) / 20 * 1.4
    base = 0.15 + min(count, 10) / 10 * 0.30
    peak = min(base + 0.30 + min(count, 15) / 15 * 0.25, 0.95)
    dur = 1.8 + h[2] / 255 * 1.6
    begin = h[3] / 255 * 3.0
    glow = ' filter="url(#gl)"' if count >= 15 else ""
    return (
        f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="#c8dfff" '
        f'opacity="{base:.2f}"{glow}>'
        f'<animate attributeName="opacity" values="{base:.2f};{peak:.2f};{base:.2f}" '
        f'dur="{dur:.1f}s" begin="{begin:.1f}s" repeatCount="indefinite"/></circle>'
    )


def build_svg(calendar: dict) -> str:
    weeks = calendar["weeks"]
    cell_w = (WIDTH - 2 * PAD_X) / max(len(weeks), 1)
    cell_h = (HEIGHT - 2 * PAD_Y) / 7
    stars = [
        star(day, wi, cell_w, cell_h)
        for wi, week in enumerate(weeks)
        for day in week["contributionDays"]
        if day["contributionCount"] > 0
    ]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" '
        f'viewBox="0 0 {WIDTH} {HEIGHT}">',
        "<defs>",
        '<filter id="gl" x="-60%" y="-60%" width="220%" height="220%">'
        '<feGaussianBlur stdDeviation="2.5" result="b"/>'
        '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>'
        "</filter>",
        "</defs>",
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="#060d21" rx="6"/>',
        *stars,
        "</svg>",
    ]
    return "\n".join(parts) + "\n"


def main() -> None:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        sys.exit("ERROR: set GITHUB_TOKEN (or GH_TOKEN).")
    calendar = fetch_calendar(token)
    svg = build_svg(calendar)

    try:
        ET.fromstring(svg)
    except ET.ParseError as exc:
        sys.exit(f"ERROR: emitted SVG is not well-formed XML: {exc}")
    raw = svg.encode()
    if len(raw) > MAX_BYTES:
        sys.exit(f"ERROR: SVG is {len(raw)} bytes, over the {MAX_BYTES} limit.")

    out = Path(__file__).resolve().parents[1] / "starry-contributions.svg"
    out.write_bytes(raw)
    print(
        f"wrote {out.name}: {len(raw)} bytes, "
        f"{svg.count('<circle')} stars, "
        f"{calendar['totalContributions']} contributions, "
        f"sha256={hashlib.sha256(raw).hexdigest()[:16]}"
    )


if __name__ == "__main__":
    main()
