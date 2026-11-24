"""Inline data.json into src.html -> index.html (one self-contained page)."""
from pathlib import Path
here = Path(__file__).parent
data = (here / "data.json").read_text().strip()
assert "</" not in data
(here / "index.html").write_text((here / "src.html").read_text().replace("__DATA__", data))
print("index.html", (here / "index.html").stat().st_size, "bytes")
