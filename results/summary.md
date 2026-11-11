# Notebook results

The key numbers from our completed notebook: every TODO is done, it ran end to end on 11.11.2026 with seed 13, and no cell failed. Use them to back the answers in Parts A–E. The figures are in [`report/img/`](../report/img/).

The notebook itself is course material, so it isn't in this repo; Mohamed runs it locally. All numbers below come from its outputs. A few were computed with the same model and the same SHAP explainer and are marked as such.

## Data and historic decisions (B1–B3)

| | Women | Men |
|---|---|---|
| Applicants | 2,943 | 12,057 |
| Recruited | 196 (6.7 %) | 4,304 (35.7 %) |
| Mean skill (0–20) | 9.93 | 10.60 |
| Mean expected salary (k$) | 64.09 | 71.18 |
| Mean experience (years) | 19.62 | 20.12 |
| Mean education (1 = high school … 4 = PhD) | 2.03 | 2.30 |
| Mean interview score (0–10) | 5.02 | 5.28 |

- **DI of the historic decisions:** 0.187 on all 15,000 applicants, 0.191 on the training set (12,000) and 0.169 on the test set (3,000).
- In the training set, the first recruited women have skill 14, the first recruited men skill 9 (see `b1_skill_salary.png`).

## The company's current model (B4)

Logistic regression trained on the historic decisions. On the 3,000 test applicants: **accuracy 0.947, DI 0.137**.

Mean |SHAP| on the test applicants; the average prediction is 0.244:

| Feature | All | Women (592) | Men (2,408) |
|---|---|---|---|
| Skill | 0.229 | 0.129 | 0.254 |
| Sex | 0.081 | **0.189** | 0.055 |
| Interview score | 0.071 | 0.053 | 0.076 |
| Experience | 0.054 | 0.036 | 0.059 |
| Expected salary | 0.024 | 0.019 | 0.025 |
| Education | 0.001 | 0.001 | 0.001 |

- For women, sex is the most important feature of all.
- On average, being a woman lowers the predicted probability by 0.189, and being a man raises it by 0.055.
- Waterfall for test row 3 (`b4_waterfall_test_row3.png`): a woman with skill 14, interview 9 and 37 years of experience. Skill +0.12, interview +0.10 and experience +0.07, but sex −0.45, so she ends at 0.072 and is rejected.
- (Computed with the notebook's explainer.)

## Mitigation strategies (C1–C3)

| Strategy | Accuracy | DI | Women hired | Men hired | Four-fifths rule |
|---|---|---|---|---|---|
| Baseline | 0.947 | 0.137 | 5.1 % | 37.0 % | ✗ |
| Remove sex | 0.903 | 0.725 | 23.0 % | 31.7 % | ✗ |
| Reweighing | 0.941 | 0.269 | 9.6 % | 35.8 % | ✗ |
| ROC (margin 0.48) | 0.837 | 0.909 | 16.7 % | 18.4 % | ✓ |
| Prejudice Remover (eta 100) | 0.903 | 0.839 | 30.7 % | 36.6 % | ✓ |

**Reweighing (C1):**
- Weights: recruited woman 4.41, rejected woman 0.75, recruited man 0.84, rejected man 1.09.
- Share recruited in the training data: 6.8 % of women vs. 35.7 % of men before reweighing, 30.0 % for both after (`c1_reweighing_balance.png`).

**Trade-off (C2, test set; `c2_tradeoff.png`):**

| ROC margin | 0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.45 | 0.46 | 0.47 | **0.48** | 0.49 | 0.5 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DI | 0.137 | 0.173 | 0.218 | 0.295 | 0.432 | 0.636 | 0.687 | 0.770 | **0.909** | 1.344 | ∞ |
| Accuracy | 0.947 | 0.944 | 0.940 | 0.926 | 0.900 | 0.869 | 0.861 | 0.851 | **0.837** | 0.802 | 0.527 |

| Prejudice Remover eta | 1 | 10 | 25 | 50 | **100** |
|---|---|---|---|---|---|
| DI | 0.164 | 0.434 | 0.553 | 0.644 | **0.839** |
| Accuracy | 0.944 | 0.932 | 0.924 | 0.917 | **0.903** |

At margin 0.5, ROC's band covers every probability, so all women are accepted and all men rejected.

**Mean |SHAP| per model (C3, 300 test applicants; `c3_shap_comparison.png`):**

| Feature | Baseline | Remove sex | Reweighing | Prejudice Remover |
|---|---|---|---|---|
| Skill | 0.245 | 0.204 | 0.249 | 0.285 |
| Sex | 0.072 | 0.000 | 0.054 | 0.005 |
| Interview score | 0.066 | 0.066 | 0.069 | 0.066 |
| Experience | 0.048 | 0.060 | 0.049 | 0.051 |
| Expected salary | 0.020 | 0.003 | 0.021 | 0.027 |
| Education | 0.001 | 0.008 | 0.001 | 0.002 |

ROC is left out on purpose: it changes decisions after the model, so the model's SHAP values don't describe its decisions (E3).

## Applicant #1460 (D1)

A woman with skill 16, expected salary 60.4k$, 21 years of experience, a PhD (education 4) and interview score 10. The current model gives her a probability of **0.390**, so she is rejected.

**SHAP** (`d1_waterfall_1460.png`, starting from 0.244):

| Sex | Skill | Interview | Salary | Education | Experience |
|---|---|---|---|---|---|
| **−0.395** | +0.302 | +0.189 | +0.044 | +0.004 | +0.002 |

**DiCE, `sex` may change** (notebook run, 7 examples). 6 of the 7 examples make her a man:

| | Ex 1 | Ex 2 | Ex 3 | Ex 4 | Ex 5 | Ex 6 | Ex 7 |
|---|---|---|---|---|---|---|---|
| Sex | man | woman | man | man | man | man | man |
| Skill | 16 | 18 | 16 | 16 | 13 | **10** | 17 |
| Experience | 21 | 25 | 18 | 25 | 21 | 21 | 22 |
| Interview | 10 | 7.8 | 10 | 10 | 10 | 10 | 10 |

- As a man, she would be hired with nothing else changed, and even with skill 10 instead of 16.
- DiCE isn't seeded in this cell, so the examples change from run to run, but the pattern stays.

**DiCE, `sex` fixed** (advice; seeded, so it can be repeated):

| | Ex 1 | Ex 2 | Ex 3 | Ex 4 | Ex 5 | Ex 6 | Ex 7 |
|---|---|---|---|---|---|---|---|
| Skill | 17 | 17 | 18 | 19 | 20 | 17 | 19 |
| Experience | 22 | 31 | 23 | 9 | 25 | 28 | 32 |
| Interview | 10 | 9.9 | 9 | 9.5 | 9.2 | 8.3 | 8.8 |

- The smallest change: skill 17 instead of 16 and one more year of experience.
- Interview values such as 9.9 appear because the notebook declares every feature continuous.

**DiCE threshold:** 0.3, 0.5 and 0.9 give exactly the same examples. The notebook runs DiCE as a regressor with a desired range, and in that mode the threshold isn't used.

**Anchors:**

| Threshold | Rule (→ rejected) | Precision | Coverage |
|---|---|---|---|
| 0.7 | experience ≤ 30 | 0.72 | 0.76 |
| 0.9 | experience ≤ 30 AND expected salary ≤ 60.63 | 0.97 | 0.24 |
| 0.95 | same as 0.9 | 0.97 | 0.24 |

- The rule names experience and salary, which barely matter for her (SHAP +0.002 and +0.044), and not her sex.
- **Why salary:** applicants who ask for ≤ 60.63k$ are mostly weak candidates. In the training set:

| | Applicants | Women | Mean skill | Rejected by the model |
|---|---|---|---|---|
| Salary ≤ 60.63k$ | 3,000 | 32 % | 6.7 | 95 % |
| Salary > 60.63k$ | 9,000 | 15 % | 11.7 | 62 % |

- **Why never sex:** Anchors cuts every feature into quartiles, and with 80 % men the only bin for sex is "sex ≤ 1", which holds everyone.

## Recommended model: Prejudice Remover, eta 100 (D2)

Accuracy 0.903 and DI 0.839, against 0.947 and 0.137 for the current model. Women's selection rate goes from 5.1 % to 30.7 %, and men's stays at 36.6 %.

Mean |SHAP| on the first 500 test applicants (`d2_pr_shap_bar.png`, `d2_pr_shap_cohort.png`, `d2_pr_shap_beeswarm.png`):

| Feature | All | Women (91) | Men (409) |
|---|---|---|---|
| Skill | 0.281 | 0.282 | 0.280 |
| Interview score | 0.073 | 0.063 | 0.075 |
| Experience | 0.057 | 0.051 | 0.058 |
| Expected salary | 0.031 | 0.029 | 0.032 |
| Sex | 0.005 | 0.015 | 0.003 |
| Education | 0.003 | 0.003 | 0.003 |

- Skill now counts the same for women and men.
- Sex has almost no effect: on average +0.009 for women and −0.001 for men.
- (Computed with the notebook's explainer.)

## Figures

| File | Shows | Part |
|---|---|---|
| `b1_skill_salary.png` | Skill vs. expected salary, by sex and outcome (training set) | B1 |
| `b4_shap_bar.png` | Current model: mean \|SHAP\| per feature | B4 |
| `b4_shap_cohort.png` | Current model: mean \|SHAP\| for women and men | B4 |
| `b4_shap_beeswarm.png` | Current model: direction of each feature's effect | B4 |
| `b4_waterfall_test_row3.png` | Current model: one test applicant's decision | B4 |
| `c1_reweighing_balance.png` | Share recruited per sex, before and after reweighing | C1 |
| `c2_tradeoff.png` | DI vs. accuracy for ROC and Prejudice Remover | C2 |
| `c3_shap_comparison.png` | Mean \|SHAP\| per feature for four models | C3 |
| `d1_waterfall_1460.png` | Applicant #1460's decision, broken down | D1 |
| `d2_pr_shap_bar.png` | Prejudice Remover: mean \|SHAP\| per feature | D2 |
| `d2_pr_shap_cohort.png` | Prejudice Remover: mean \|SHAP\| for women and men | D2 |
| `d2_pr_shap_beeswarm.png` | Prejudice Remover: direction of each feature's effect | D2 |
