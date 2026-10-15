# Supplementary material

The aggregate result files behind every reported table and figure, with the
checksums and the script that verifies them.

```
reproduce.py       checks every table against results/ and MANIFEST.md
requirements.txt   pandas, numpy
results/           the released aggregate files the numbers come from
tables/            every table as CSV, plus CAPTIONS.md
figures/           every figure as vector PDF
MANIFEST.md        every file with its row count and SHA-256
```

## Run it

    pip install -r requirements.txt
    python reproduce.py

It prints a SHA-256 prefix per table and checks it against `MANIFEST.md`.
A digest that differs means the file was regenerated from different inputs.

## What is not here, and why

The cohort is de-identified emergency EHR from three hospitals, held under
institutional approval with a waiver of individual consent for secondary use.
That approval covers analysis, not redistribution. This package therefore
contains **no EHR micro-data of any kind** -- no generated text, and not a
single row standing for one encounter or one claim. A claim identifier is a key
back into a clinical record, and a per-claim row with a design weight still
describes one patient.

The releasable unit is an aggregate: a cell of a reported table, or a
group-level row by condition, by model, or by anonymised hospital. The three
hospitals appear only as Hospital A, B and C.

`MANIFEST.md` lists every data file with its row count and checksum, and lists
the files withheld under this rule, with the reason for each.

**No credentials and no model weights.** The four models are open-weight and
pulled by tag; the digests they resolved to are in Supplementary Table S12.

## Cell conventions

| cell | meaning |
|---|---|
| `--` | not estimable, or withheld by the n_eff < 5 rule. Never a zero, never missing. |
| `*` | Holm-adjusted p < 0.05 |
| `[a, b]` | 95% CI |
