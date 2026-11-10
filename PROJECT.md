# Case 2 – Explainable AI & Fairness

Shared context for the team. Read this file and every file in `progress/` at the start of each work session.

## Start and end of every session

- **Start:** `git pull`, then read this file and every file in `progress/`.
- **End:** update your own file in `progress/` (done, decisions, next, blockers), then commit and push.

## Deliverables

- **One PDF on Moodle.** The case sheet says "17.11.2026 midnight". We submit on **Mon 16.11.2026**; check the exact time on the Moodle submission page.
  - Front page: all three names and matriculation numbers.
  - Every answer is backed by a number or a plot from the notebook.
  - Length limits: C1 2–3 sentences, C3 3–5 sentences, D1c and D2 at most 150 words each, D3 at most 200 words.
  - The completed notebook goes in an appendix.
- **About 5 slides,** only if we present Case 2 (Tue 17.11.2026).

## Tasks

| Part | What | Where |
|---|---|---|
| A | Compare Anchors, DiCE, LIME and SHAP, based on Meza Martínez et al. (2023), https://doi.org/10.1145/3607145: local or global, the form of the explanation, what it reveals and hides, who can use it, and its main limitation | Text |
| B | Diagnose the bias: the data (B1), the Disparate Impact formula and thresholds (B2), AIF360 vs. DataFrame DI (B3), the SHAP plots (B4) | Notebook and text |
| C | Mitigate the bias: remove `sex`, Reweighing, Prejudice Remover, Reject Option Classification. Balance plot (C1), fairness–utility plot over `eta` and `ROC_margin` (C2), comparison of all strategies (C3) | Notebook and text |
| D | Applicant #1460: DiCE (D1a), Anchors (D1b) and a letter to her (D1c). A note for the HR manager (D2) and one for the works council (D3) | Notebook and text |
| E | Six misconceptions (E1–E6): true, false or partly true, corrected and backed by the notebook | Text |

The notebook's `# TODO` cells are B2 (the DI formula), C1 (the balance plot) and C2 (the two loops).

## Roles and file ownership (proposal, to be agreed)

Only a file's owner edits it. Before changing someone else's file, ask them.

| Who | Role | Files |
|---|---|---|
| Mohamed Gomaa (issamfarouk) | Notebook, answers to B and C, the D experiments, report PDF | `notebooks/`, `report/part_b.md`, `report/part_c.md`, `report/img/`, `report/final/` |
| Ahmed Abdelrazek (AhmedElngar) | Part A | `report/part_a.md` |
| Ahmed Farag (AhmedWilly) | Part D texts and Part E | `report/part_d.md`, `report/part_e.md` |

Notebooks merge badly, so only the notebook's owner commits changes to it. Everyone else sends code or numbers to them.

## Git

- `git pull` before you start, and push at least twice a day.
- Commit directly to `main`, touching only your own files.
- Commit messages: one short, clear line.
- Never commit `.venv/`, `team.json` or the course's files (task sheet, slides).

## Timeline (proposal)

| When | What | Who |
|---|---|---|
| Tue 10.11 | Agree on roles and the presentation date. Download the paper. | All |
| Wed 11.11 | Notebook TODOs (B2, C1, C2) | Mohamed |
| Wed 11.11 – Fri 13.11 | Part A | Ahmed Abdelrazek |
| Thu 12.11 – Sat 14.11 | Answers to B and C, the D experiments (DiCE, Anchors) | Mohamed |
| Fri 13.11 – Sat 14.11 | Part D texts and Part E, from the notebook results | Ahmed Farag |
| Sun 15.11 | Report PDF and review | Mohamed, then all |
| Mon 16.11 | Final check and submission | Mohamed |
