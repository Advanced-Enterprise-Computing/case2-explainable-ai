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

The notebook's `# TODO` cells are B2 (the DI formula), C1 (the balance plot), C2 (the two loops and the chosen settings), D1a and D1b (the DiCE and Anchors settings) and D2 (the recommended model).

## Roles and file ownership

Only a file's owner edits it. Before changing someone else's file, ask them.

| Who | Role | Files |
|---|---|---|
| Mohamed Gomaa (issamfarouk) | Team lead. Notebook (run locally), answers to B, C, D1a and D1b, report PDF | `report/part_b.md`, `report/part_c.md`, `report/part_d1.md`, `report/img/`, `report/final/`, `results/` |
| Ahmed Abdelrazek (AhmedElngar) | Part A | `report/part_a.md` |
| Ahmed Farag (AhmedWilly) | D1c (letter to the applicant), D2 (HR briefing), D3 (works council) and Part E | `report/part_d.md`, `report/part_e.md` |

Part D is split over two files: `report/part_d1.md` holds the Part D title with D1a and D1b, and `report/part_d.md` continues directly with `## D1c`, then D2 and D3.

The course notebook is course material, so it stays out of this repo. Mohamed runs it on his machine and puts its results here for everyone: the numbers in `results/summary.md`, the figures in `report/img/`.

## Git

- `git pull` before you start, and push at least twice a day.
- Commit directly to `main`, touching only your own files.
- Commit messages: one short, clear line.
- Never commit `.venv/`, `team.json` or the course's files (task sheet, slides, notebook).

## Timeline

| When | What | Who |
|---|---|---|
| Tue 10.11 – Wed 11.11 | Notebook TODOs and full run, results and figures, answers to B, C, D1a and D1b (done) | Mohamed |
| Wed 11.11 | Roles and the presentation date sent to the team | Mohamed |
| By Sat 14.11, night | Part A in `report/part_a.md` | Ahmed Abdelrazek |
| By Sat 14.11, night | D1c, D2, D3 and Part E in `report/part_d.md` and `report/part_e.md`, from `results/summary.md` | Ahmed Farag |
| Sun 15.11 | Report PDF and review | Mohamed, then all |
| Mon 16.11 | Final check and submission | Mohamed |
