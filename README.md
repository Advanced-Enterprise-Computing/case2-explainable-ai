# Case 2 – Explainable AI & Fairness

Auditing a hiring model for gender bias with SHAP, DiCE and Anchors, and comparing bias mitigations with AIF360.

## The case

A company pre-selects job applications with a logistic regression trained on its own past hiring decisions. After complaints, it brings us in as an external audit team.

- **Diagnose:** measure how differently the model treats women and men (Disparate Impact), and look inside it with SHAP.
- **Mitigate:** compare four ways to reduce the bias: dropping the `sex` feature, Reweighing, Prejudice Remover and Reject Option Classification.
- **Explain:** describe the model's decisions to a rejected applicant, the HR manager and the works council, with SHAP, DiCE and Anchors.
- **Correct:** check six common claims about explainable AI and fairness against our results.

## Layout

| Path | Content |
|---|---|
| `PROJECT.md` | Tasks, deadline, roles and how we work together |
| `progress/` | One handoff note per person |

## Team

| Name | GitHub |
|---|---|
| Mohamed Gomaa | [issamfarouk](https://github.com/issamfarouk) |
| Ahmed Farag | [AhmedWilly](https://github.com/AhmedWilly) |
| Ahmed Abdelrazek | [AhmedElngar](https://github.com/AhmedElngar) |
