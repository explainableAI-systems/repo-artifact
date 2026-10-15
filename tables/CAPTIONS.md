# Exported tables

One CSV per reported table, exported directly from the generated output so the exported values are exactly the reported values. Conventions:

| cell | meaning |
|---|---|
| `--` | not estimable, or withheld by the $n_{\mathrm{eff}} < 5$ rule. Never a zero, never a missing value. |
| `*` | Holm-adjusted $p < 0.05$ |
| `[a, b]` | 95% CI, kept inside the cell it annotates |

## Table 1 --- `table_1_alignment_and_flag_rates.csv`

13 data rows, 5 columns.

Evidence alignment and automated audit flag rates by conditioning strategy, all 3, explanations, % [95% CI]. P1 and P3 supply the model-evidence bundle M_h; P2 and P3 the record-context bundle E_i=(R_i,D_i). Intervals are encounter-clustered bootstrap, B=10,. Two further alignment metrics, not estimable under P0 or P2, are in the supplementary material. Supplementary Figure S1 plots these same eleven without the intervals. The lower block carries the audit's labels; how far each is reproduced by clinicians is Table 4. Its first five rows are claim-level rates and the last is the share of explanations carrying at least one flag.

## Table 2 --- `table_2_interaction.csv`

5 data rows, 5 columns.

Model-evidence x record-context interaction. Columns 2–3 are the effect of supplying the model-evidence bundle M_h without and with the record-context bundle. Each metric is scored against its own reference as defined in Section 4.4—only AER_sup against the supplied component A_h. Column 4 is the difference, (P3-P2)-(P1-P0). Percentage points, encounter-clustered bootstrap, Holm-corrected across the prespecified family of 13 metrics, all of which appear in the supplementary material; the five shown here are the ones the interference claim rests on. * marks adjusted p<0.05. ^+ The pooled PRSR interaction is shown for transparency and is not interpreted as a common effect: its ratio denominator is model-dependent and the quantity is not estimable in two of the four models (Section 5.3).

## Table 3 --- `table_3_ablation_and_robustness.csv`

10 data rows, 2 columns.

Robustness of the model-evidence x record-context interaction on supplied-evidence recall: the same quantity re-estimated ten ways. The two ablations remove a component; the order row removes nothing; the last row varies how a feature mention is detected. Percentage points, with the 95% interval or a note beneath each estimate. No row reverses the sign and no interval reaches zero.

## Table 4 --- `table_4_clinician_validation.csv`

6 data rows, 12 columns.

Clinician validation on the data-local subset. n is annotated claims in scope; Pos. how many each rater flagged and Jacc. their positive-set overlap—properties of the deliberately enriched reliability sample, not population quantities. Tier is fixed from reliability alone before any detector performance is seen: R reproducible (kappa >= 0.60 with non-degenerate overlap), M moderate (0.20 <= kappa < 0.60), E exploratory. Sample F_1 is unweighted; design-weighted applies the recorded inclusion probabilities (Horvitz–Thompson over the local domain) and is the column to read. Prev. is the design-weighted positive-label prevalence within each dimension's applicable claim domain—for record support, conditional on record-type claims. n_eff is Kish's effective sample size of the binding domain (predicted positives for precision, reference positives for recall); a weighted ratio is withheld when its own domain falls below five and F_1 when either does, a post hoc rule applied uniformly (2 dimensions). The unweighted confusion matrix behind these ratios is Supplementary Table S10. Unsafe inference carries no primary estimate: adjudication yields reference labels but the two raters share no positive, so performance against them is not validated performance for a reproducible construct. A separate single-rater round of 122 claims under the verbatim codebook question gives precision 0.38 and recall 0.29—a different design, not clinician-validated detector performance.

## Supplementary Table S1 --- `table_S1_all_13_metric_contrasts.csv`

13 data rows, 7 columns.

Supplementary. All 13 metrics in the prespecified Holm family, percentage points. The correction was applied across all 13 and the family was fixed before any p-value was examined; Table 2 shows the five the interference claim rests on. * marks Holm-adjusted p<0.05.

## Supplementary Table S2 --- `table_S2_record_claim_composition.csv`

5 data rows, 5 columns.

Record-claim composition: the mechanism behind a ratio that rises two different ways. PRSR's denominator is set by the generator rather than by the design—under P1 only 32.6% of explanations make any record claim, so its 82.40% rests on 293 of them—while the three rates below it have a denominator the design fixes. P1 raises PRSR by suppression, making 66% fewer record claims, and P2 raises it by supported record-claim production, making almost twice as many. The ratio alone cannot distinguish the two, which is why it is reported here beside them. Post hoc; Holm-corrected within this family of three and not pooled with the prespecified 13.

## Supplementary Table S3 --- `table_S3_composition_contrasts.csv`

21 data rows, 4 columns.

Supplementary. Record-claim composition contrasts, with 95% encounter-clustered bootstrap intervals. Post hoc: Holm correction is applied within this family of three metrics only, never pooled with the prespecified 13. Interaction is (P3-P2)-(P1-P0), defined exactly as in the primary analysis. * marks adjusted p<0.05.

## Supplementary Table S4 --- `table_S4_endpoint_composition.csv`

3 data rows, 6 columns.

Endpoint composition, % of explanations. A composite safety endpoint inherits the validity of its weakest member, and this table shows the consequence: the three compositions agree on the sign of the incremental effect of adding the model-evidence bundle to record context and differ on its significance, according to whether they admit dimensions that did not reach the reproducible tier. The union with a validated basis is therefore the one to read, and on it the effect is directional. No union is treated as a preferred clinical safety outcome.

## Supplementary Table S5 --- `table_S5_backbone_performance.csv`

4 data rows, 8 columns.

The predictor being explained, leave-one-hospital-out, on the full held-out cohorts rather than the prediction-status-stratified audit sample. Reported so that explanations of this model can be interpreted; predictive modelling is not a contribution. ``base'' is the Brier score of a constant predictor at the site prevalence. Discrimination is strong everywhere; the probabilities are not calibrated—the slope is far above 1 and two of three sites score worse than their own base rate. Every explanation restates one of these scores, which is why the fidelity of the restatement is measurable independently of the calibration.

## Supplementary Table S6 --- `table_S6_readjudication_bounds.csv`

6 data rows, 5 columns.

Supplementary. The prospectively specified bound on the re-adjudication, and where the correction actually landed. Exposed is the share of each reference standard that came from adjudication rather than two-reviewer consensus; consensus labels were produced under the full codebook and were never exposed. The range is the extreme over every assignment of the exposed labels—agreeing with the detector on all of them, and contradicting it on all—computed before the second round was returned. Every observed F_1 falls inside its own range, which is the check the construction exists for. The ranges are not confidence intervals and are not reported as uncertainty.

## Supplementary Table S7 --- `table_S7_per_model_profile.csv`

4 data rows, 11 columns.

Per-model profile, pooled over the four conditioning strategies, % except the two rate columns. All four models were served through the same runtime with identical decoding settings, so differences are properties of the models rather than of the harness. PRSR is reported beside record claims per explanation (rec./ex.) and unsupported record claims per explanation (uns./ex.) for the reason Section 5.4 gives: a ratio whose denominator the generator chooses can be raised by making fewer claims. It is not what happens here—the model with the highest PRSR also makes the most record claims—so the ordering is a genuine support difference.

## Supplementary Table S8 --- `table_S8_interaction_by_model.csv`

25 data rows, 6 columns.

Supplementary. The 2x2 interaction computed within each model, same estimator and same encounter-clustered bootstrap as the pooled analysis. On the three attribution metrics the interference claim rests on, every model reproduces the pooled sign, so the effect is not an artefact of pooling. PRSR is not estimable for two models, which stop making record-type claims under one condition—the denominator problem of Section 5.4 reappearing per model. MEA is the opposite case: a pooled null that averages large effects running in both directions. Holm within each metric across the four models; this is a robustness check on an already-corrected effect, not a new primary family. * marks adjusted p<0.05.

## Supplementary Table S9 --- `table_S9_readjudication_effect.csv`

9 data rows, 6 columns.

Effect of the annotation instrument on adjudicated labels. The original adjudication form restated the codebook questions instead of copying them. Re-asking every one of the 175 decisions with the codebook text verbatim—automated label and earlier decision both withheld—changed 61. The split is the point: where a paraphrase dropped a material qualifier the change rate is 66%, and where it did not it is 25%. F_1 moves less than the change rate suggests because consensus labels dominate the reference standard. Corrected values are used throughout; unsafe inference has no estimable F_1 either way.

## Supplementary Table S10 --- `table_S10_unweighted_confusion_matrix.csv`

6 data rows, 5 columns.

Supplementary. Unweighted confusion matrix behind Table 4—the counts the Sample F_1 column is computed from, before any inclusion probability is applied, over the annotated claims in scope for each dimension.

## Supplementary Table S11 --- `table_S11_decoding_sensitivity.csv`

11 data rows, 5 columns.

Supplementary. Decoding sensitivity and prompt order, and the robustness the interference claim rests on: the interaction is negative in every arm with no interval touching zero. Same prompts, same model digests, explanations across arms over stratified encounters. Columns 2–3 are the model-evidence effect without and with record context; column 4 their difference, with an encounter-clustered interval. In the second block, block order reversed re-runs P3 alone with the model-evidence block placed before the record block, scored against the unchanged P0, P1 and P2 of the T=0.2 run a so that position is the only difference, and occlusion half removed drops that component of M_h from P1 and P3 and leaves everything else. The third block recomputes the T=0.2 run a interaction using each half of the feature matcher alone instead of their union: the level moves and the sign does not.

## Supplementary Table S12 --- `table_S12_truncation_by_model_condition.csv`

5 data rows, 6 columns.

Supplementary. Generations reaching the 900-token output cap, as count (%) of the 225 per cell. One output budget is applied to every model and condition, so a difference between cells is a property of the generator rather than of the harness. The cap binds on one model and almost nowhere else, and within that model it binds hardest in the two conditions that supply the model-evidence bundle. The primary contrast is recomputed on untruncated explanations only.

## Supplementary Table S13 --- `table_S13_generation_provenance.csv`

19 data rows, 2 columns.

Supplementary. Generation provenance. Entries without a marker were fixed at generation time and read from the generation scripts. ^+ marks values read from the generation host after the fact: they identify the artefacts present on that host, but Ollama tags are mutable and no digest was captured during generation, so they are a best-effort identification rather than a pinned record. We report the distinction rather than collapse it, because a replicator needs to know which half they can rely on.
