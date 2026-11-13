# Progress – Ahmed Farag (AhmedWilly)

## Done
- **D1c, D2 and D3** in `report/part_d.md`, starting directly with `## D1c` so it continues `part_d1.md`. Word counts: letter 146 (max. 150), D2 147 (max. 150), D3 196 (max. 200). The reasoning for D1c and the "should the company send it?" answer are outside the letter and don't count towards its 150 words.
- **Part E (E1–E6)** in `report/part_e.md`: a verdict and three sentences per statement, each backed by numbers.
- **Experiments for Part E:** `report/part_e_notebook_cell.py`. It reuses the notebook's variables. I tested it on a rebuild of the notebook (seed 13), which reproduced every number in `results/summary.md` exactly (baseline 0.947 / DI 0.137, #1460 = 0.390, all five strategies).

## Note for Mohamed
- Please paste `report/part_e_notebook_cell.py` into the notebook's last cell ("Optional: use this space for small experiments") and run it after everything else, so the appendix shows the Part E evidence. It needs `ROC_MARGIN_CHOSEN = 0.48` and `PR_ETA_CHOSEN = 100`.
- New numbers for `results/summary.md`, if you want them there:
  - **Bias-free labels:** the historic rule rerun on the same applicants with `sex_weight = 0`. Women 28.6 % vs. men 30.3 % recruited (DI 0.944; historic DI 0.187).
  - **Accuracy against the bias-free labels:** baseline 0.891, remove sex 0.923, Prejudice Remover 0.917, Reweighing 0.905, ROC 0.873.
  - **#1460:** as a man 0.999, remove sex 0.932, Reweighing 0.791, Prejudice Remover 0.975. Under the bias-free rule she would have been hired.
  - **ROC 0.48:** changes 516 of 3,000 decisions (69 women → hired, 447 men → rejected). 976 applicants are in the band, where the decision is decided by sex alone.
  - **Proxies:** sex can be predicted from the 5 other features with AUC 0.677 (salary alone 0.646).

## Decisions
- The letter (D1c) is honest: sex was the main reason, and there is no fair advice to give. It promises a human re-review. In our answer the company should send it only if it actually does that re-review.
- D3 risks with examples: irrelevant/unfaithful (the Anchors rule), unstable (unseeded DiCE), incoherent (interview 9.9), cherry-picked (averages, chosen applicants).
- Martens et al. is cited as 2026, the year of the published BISE article (the DOI on the case sheet). The case sheet itself says 2025.

## Next
- Review the report PDF on Sun 15.11.

## Blockers
- None.
