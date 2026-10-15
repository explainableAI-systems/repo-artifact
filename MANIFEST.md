# Manifest

Every data file in this package, with the unit one row stands
for. Nothing here is per-encounter or per-claim: that is EHR
micro-data and the ethics approval does not permit sharing it.

| file | rows | cols | sha256 |
|---|---|---|---|
| `results/L01_corpus.csv` | 1 | 20 | `cd2beac9361f` |
| `results/L01b_truncation.csv` | 25 | 5 | `73e122a5713b` |
| `results/L02_by_condition.csv` | 4 | 101 | `c244e9653f03` |
| `results/L02b_contrasts.csv` | 65 | 9 | `e8433e7d410d` |
| `results/L02c_interaction.csv` | 13 | 13 | `5cee5e90dbc9` |
| `results/L02d_by_model.csv` | 4 | 101 | `5f5b438fde5b` |
| `results/L02e_by_hospital.csv` | 3 | 101 | `3a086c59eefd` |
| `results/L03_coverage.csv` | 6 | 12 | `ea580a496451` |
| `results/L03b_reliability.csv` | 6 | 11 | `ce90d4fdefda` |
| `results/L03c_validation.csv` | 6 | 18 | `5e7a5d1a1a57` |
| `results/L03d_weights.csv` | 12 | 4 | `5d7033efe0b7` |
| `results/L05_complete_case.csv` | 44 | 5 | `7d5c0c7d4776` |
| `results/L05b_completeness.csv` | 10 | 8 | `8e661d423793` |
| `results/L05c_length_adjusted.csv` | 56 | 6 | `50a6b4da37d4` |
| `results/L05d_endpoints.csv` | 3 | 19 | `9353f790405d` |
| `results/L05e_interaction_adjusted.csv` | 18 | 8 | `ecfed27da0ea` |
| `results/L08_topup_validation.csv` | 1 | 18 | `8671ca8f6253` |
| `results/L09_construct_sensitivity.csv` | 4 | 11 | `154736848d35` |
| `results/L11_readjudication_agreement.csv` | 3 | 8 | `6d067baa6e26` |
| `results/L11b_validation_readjudicated.csv` | 3 | 21 | `fdc01a3d9665` |
| `results/L12_record_composition.csv` | 12 | 9 | `e573914a89f2` |
| `results/L12b_composition_contrasts.csv` | 18 | 10 | `110ff0171233` |
| `results/L12c_composition_by_model.csv` | 4 | 8 | `ef351f8e2d6e` |
| `results/L14_exposure_bounds.csv` | 6 | 15 | `7ebdac3fe60b` |
| `results/L15_readjudication_rest_agreement.csv` | 3 | 10 | `743008e172c2` |
| `results/L15b_validation_rest.csv` | 3 | 22 | `32ec17376a59` |
| `results/L16_weighted_validation.csv` | 6 | 33 | `b86bb29f75ad` |
| `results/L17_interaction_by_model.csv` | 20 | 18 | `e8b410031091` |
| `results/L18_provenance.csv` | 19 | 4 | `f4851e95df31` |
| `results/D02_interaction_by_arm.csv` | 6 | 11 | `f5a87161c9a0` |
| `results/D03_interaction.csv` | 1 | 5 | `725d84416f19` |
| `results/D04_interaction.csv` | 1 | 7 | `310d8b63c46e` |
| `results/D05_matcher_sensitivity.csv` | 18 | 7 | `8a8cc0cbb8e3` |

## Refused by the builder

These files exist in the analysis tree and are deliberately
not here. Listing them is part of the record.

| file | reason |
|---|---|
| `L04_topup_sample.csv` | record-level: identifier column claim_id, kode |
| `L08b_topup_returned.csv` | record-level: identifier column claim_id, kode |
| `L10_readjudication_frame.csv` | record-level: identifier column claim_id, kode |
| `L10b_prior_decisions.csv` | record-level: identifier column kode |
| `L13_readjudication_rest_frame.csv` | record-level: identifier column claim_id, kode |
| `L13b_prior_decisions_rest.csv` | record-level: identifier column kode |
| `D01_generations.csv` | record-level: identifier column case_id, explanation_id |
| `D02_scored.csv` | record-level: identifier column case_id |
| `D03_order_ablation.csv` | record-level: identifier column case_id, explanation_id |
| `D04_bundle_ablation.csv` | record-level: identifier column case_id, explanation_id |
