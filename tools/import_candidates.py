#!/usr/bin/env python3
"""Import candidate Vietnamese universities from published 2025 inventory.
This is a staging dataset, NOT an officially validated list of 226 institutions.
Run: python tools/import_candidates.py
Requires: requests beautifulsoup4
"""
import json, re, sys
from pathlib import Path
import requests
from bs4 import BeautifulSoup

URL="https://dev.thuvienphapluat.vn/chinh-sach-phap-luat-moi/vn/ho-tro-phap-luat/thong-tin-huu-ich/94866/danh-sach-cac-dai-hoc-va-truong-dai-hoc-tren-ca-nuoc"
root=Path(__file__).resolve().parents[1]
resp=requests.get(URL,timeout=45,headers={"User-Agent":"Mozilla/5.0 (compatible; EduMap-data-import/1.0)"})
resp.raise_for_status()
soup=BeautifulSoup(resp.text,"html.parser")
text=soup.get_text("\n",strip=True)
# Source has numbered rows in tables, encoded as STT, MÃ, TÊN TRƯỜNG.
rows=[]
for tr in soup.select("tr"):
    cells=[c.get_text(" ",strip=True) for c in tr.find_all(["th","td"],recursive=False)]
    if len(cells)>=3 and re.fullmatch(r"\d{1,3}",cells[0]):
        num=int(cells[0]); code=cells[1].strip(); name=cells[2].strip()
        if 1<=num<=400 and code and len(name)>5:
            rows.append(dict(source_number=num,code=code,name=name.replace(" (*)","").strip(),source_private_mark="(*)" in name))
dedup={r["source_number"]:r for r in rows}
rows=[dedup[i] for i in sorted(dedup)]
if len(rows)<226:
    raise SystemExit(f"Source parsing returned {len(rows)} rows (<226). Source may have changed. NO output generated.")
for r in rows:
    r.update(source_url=URL,source_year=2025,record_status="candidate_unverified_2026",legal_status=None,manager=None,latitude=None,longitude=None,coordinate_accuracy="not_geocoded")
path=root/"data"/"candidate_inventory_2025.json"
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps({"source":URL,"notice":"2025 reference directory; may include dependent schools, campuses, and duplicate organizations. Not verified 2026; do not equate with 226 distinct universities.","count":len(rows),"institutions":rows},ensure_ascii=False,indent=2),encoding="utf-8")
print(f"Wrote {len(rows)} candidates to {path}")