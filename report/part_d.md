## D1c – A reply to applicant #1460

The reply rests on what SHAP, DiCE and our own check of her profile agree on. Her sex lowers her probability by 0.395, more than her skill (+0.302) or her interview (+0.189) raise it. The same application from a man scores 0.999 instead of 0.390, and with sex fixed, DiCE asks for more than most hired men bring: skill 17 and 22 years of experience (0.664), although 3,130 of the 4,315 men it hires among all 15,000 applicants have skill below 17, and 2,531 even below her 16. Measured with the corrected models, her application is stronger than 52 % (Prejudice Remover) to 65 % (without `sex`) of the applications the current model accepts. Without the sex bonus in the historic rule she would have been hired, and the corrected models accept her (Prejudice Remover 0.975, without `sex` 0.932). The Anchors rule is left out, because it names her salary and experience instead of the actual reason (D1b).

> Dear applicant,
>
> A computer program screened your application. It learned from our past hiring decisions, which favoured men, and copied this.
>
> We checked how it rated you. Your skills and your perfect interview counted strongly in your favour. Being a woman counted against you more than anything else. The same application from a man would almost certainly have been accepted.
>
> So you were not rejected for a weakness in your application. It is stronger than more than half of those we accept, so we cannot honestly advise you to change anything. With this program, only scores higher than those of most men we hire would have helped, and that would not be fair advice.
>
> We are correcting the program, and the corrected version recommends you. A member of our HR team will review your application again in person and contact you within two weeks.
>
> Kind regards

**Should the company send it?** Yes, but only together with the remedy it promises: a human review of her application and a corrected model. The letter admits discrimination and raises legal risk. A vague or partial answer, such as the Anchors rule alone, would mislead her, though, and would be exactly the kind of "explanation" Martens et al. (2026) warn against. Applicants in a high-risk system also have a right to a clear and meaningful explanation of the decision (Art. 86 EU AI Act; Art. 15(1)(h) GDPR). Sending the letter without actually changing anything would turn honesty into an empty gesture.

## D2 – Briefing for the HR manager

> **What the current model looks at.** Mostly skill (mean |SHAP| 0.229), but sex comes second (0.081), and for women it is the top factor (0.189), lowering their chance by 0.19 on average. The model selects 5.1 % of women and 37.0 % of men (Disparate Impact 0.137; 0.8 is the usual minimum).
>
> **Our recommendation: Prejudice Remover (eta = 100).** It weighs skill equally for women and men (0.282 vs. 0.280), and sex has almost no effect left (0.005). It selects 30.7 % of women and 36.6 % of men (DI 0.839).
>
> **The cost.** It matches past HR decisions in 90.3 % of cases instead of 94.7 %, but those decisions were biased: compared with past decisions without the sex bonus, it is more accurate (0.917 vs. 0.891). It still needs each applicant's sex to neutralise it, and its DI must be rechecked after every retraining.

## D3 – Assessment for the works council

> **Is the current model discriminatory?** Yes. It selects 5.1 % of women and 37.0 % of men (DI 0.137), far below the four-fifths threshold of 0.8. The cohort SHAP plot shows that sex is the most important feature for women (0.189, ahead of skill with 0.129). Applicant #1460 (PhD, interview 10/10) loses 0.395 for her sex alone; as a man she would score 0.999 instead of 0.390, and DiCE flips her decision by changing only her sex. In a recruitment system, which is high-risk under the EU AI Act, this is direct discrimination.
>
> **Can you trust our explanations?** Only in combination, because several risks from Martens et al. (2026) apply:
>
> - *Irrelevant:* the Anchors rule for #1460 ("experience ≤ 30 and salary ≤ 60.63k$") is 97 % precise, but it names two features that barely affect her (+0.002, +0.044) and hides the real cause, her sex (−0.395).
> - *Unstable:* DiCE with `sex` free is not seeded and changes in every run.
> - *Incoherent:* DiCE proposes interview scores such as 9.9 on a whole-number scale.
> - *Cherry-picked:* we chose which applicants and DiCE examples to show, and D2 shows only averages.
>
> We trust only findings on which SHAP, DiCE and the DI agree.

## References

- European Parliament & Council of the European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*. http://data.europa.eu/eli/reg/2016/679/oj
- European Parliament & Council of the European Union. (2024). Regulation (EU) 2024/1689 (Artificial Intelligence Act). *Official Journal of the European Union, L 2024/1689*. http://data.europa.eu/eli/reg/2024/1689/oj
- Martens, D., Shmueli, G., Evgeniou, T., Bauer, K., Janiesch, C., Feuerriegel, S., Gabel, S., Goethals, S., Greene, T., Klein, N., Kraus, M., Kühl, N., Perlich, C., Verbeke, W., Zharova, A., Zschech, P., & Provost, F. (2026). Beware of "explanations" of AI. *Business & Information Systems Engineering*. https://doi.org/10.1007/s12599-026-01015-y
