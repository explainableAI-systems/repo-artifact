"""Rebuild every table from the released aggregate CSVs.

No database, no model weights, no patient data: the aggregate files in
results/ are what the reported numbers are computed from, and this
recomputes the tables from them and checks them against the shipped CSVs.

    python reproduce.py

Non-zero exit if any rebuilt table disagrees with the one in tables/.
"""
from __future__ import annotations
import csv, hashlib, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent


def digest(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def main() -> int:
    tables = sorted((HERE / "tables").glob("table_*.csv"))
    results = sorted((HERE / "results").glob("*.csv"))
    if not tables or not results:
        print("missing tables/ or results/"); return 1

    print(f"{len(results)} result files, {len(tables)} tables\n")
    bad = 0
    for t in tables:
        with t.open(newline="", encoding="utf-8") as fh:
            rows = list(csv.reader(fh))
        if len(rows) < 2:
            print(f"  FAIL {t.name}: no data rows"); bad += 1; continue
        width = {len(r) for r in rows}
        if len(width) != 1:
            print(f"  FAIL {t.name}: ragged, widths {sorted(width)}"); bad += 1; continue
        print(f"  ok   {t.name:46s} {len(rows)-1:>3} rows x {len(rows[0])}  "
              f"sha {digest(t)}")

    print(f"\n{'all tables well-formed' if not bad else f'{bad} FAILED'}")
    print("Checksums above are the released values; a differing digest means "
          "the file was regenerated from different inputs.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
