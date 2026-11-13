# Part E – Spotting the misconceptions

The evidence comes from our notebook. The numbers marked "experiment" come from the short code cell at the end of the notebook (`report/part_e_notebook_cell.py`), which reuses the notebook's data and models with seed 13. One of these experiments uses an advantage only auditors of a simulation have: we rerun the historic hiring rule on exactly the same 15,000 applicants without its sex bonus (`sex_weight = 0`). This gives the decisions the company would have made without favouring men, and we call them "bias-free labels" below, although the applicant data itself still contains the education gap.

## E1 – "Our model does not use the attribute `sex`, so it cannot discriminate against women."

**False.** Removing the column does not remove the information, because the other features act as proxies: they reveal an applicant's sex with an AUC of 0.677, salary alone with 0.646, as women ask for 6k$ less (experiment; Barocas & Selbst, 2016). The model without `sex` therefore still selects 23.0 % of women and 31.7 % of men (DI 0.725, below 0.8), and 55.2 % vs. 64.7 % even within the same skill range of 12–16 (experiment). It even flips its salary weight from negative (−0.906) to slightly positive (+0.063), because a low salary demand now also signals "woman".

## E2 – "To find out why fewer women were hired in the past, we simply apply SHAP to the historic dataset."

**Only partly true.** SHAP explains a trained model, not a dataset: a model fitted to the history shows that sex matters (the top feature for women, 0.189), but only as a correlation inside that model, so it cannot separate unequal treatment from women's lower skill (9.93 vs. 10.60) and education (Lundberg & Lee, 2017). The "why" needs the hiring process itself or a causal analysis. Our experiment shows this: with the same applicants and only the sex bonus removed from the historic rule, women's hiring rate rises from 6.7 % to 28.6 % and the DI from 0.187 to 0.944, so the bonus, not the qualifications, caused almost the whole gap.

## E3 – "Reject Option Classification only changes the output after the model, so the SHAP values of the baseline model also explain the final decisions after ROC."

**False.** At margin 0.48, ROC changes 516 of the 3,000 test decisions (69 women to hired, 447 men to rejected), and for the 976 applicants inside its band the final decision depends on sex alone (experiment; Kamiran et al., 2012). The baseline's SHAP values explain its probabilities, not these decisions: one man has a probability of 0.979, explained mainly by his skill (+0.273), experience (+0.169) and interview (+0.158), and ROC still rejects him because he is a man. To explain the final decisions, SHAP would have to be applied to the model and ROC together, which is why ROC is left out of the comparison in C3.

## E4 – "A model with DI = 1.0 is fair."

**False.** DI only compares how many women and men are selected, not who is selected or why (Barocas et al., 2023). In our experiment, a lottery that hires 30 % at random reaches DI 0.947 at an accuracy of 0.576, and a model that keeps the baseline's men but hires the lowest-scored women reaches DI 1.001 while hiring none of the women with a positive bias-free label (vs. 96.5 % of such men). DI ≈ 1 is a sign of group parity, not proof of fairness, and must be complemented by checks within groups, such as equal opportunity (Hardt et al., 2016), and on individual decisions, as for #1460 in D1.

## E5 – "All mitigation strategies have a lower accuracy than the baseline, so their decisions are worse."

**Only partly true.** On the historic labels every strategy is indeed less accurate (0.837–0.941 vs. 0.947), but those labels contain the bias, so accuracy partly measures how well a model copies the past discrimination. On the bias-free labels the ranking turns: removing `sex` (0.923), Prejudice Remover (0.917) and Reweighing (0.905) all beat the baseline (0.891) (experiment). Only ROC stays below it (0.873), because inside its band it decides by sex rather than by merit.

## E6 – "Skill has by far the largest SHAP value, so skill is what causes an applicant to be recruited."

**Only partly true.** Skill is the model's most important feature on average (mean |SHAP| 0.229) and had the largest weight in the historic rule (0.6), but SHAP shows what the model relies on, not what causes recruitment, and for women sex outweighs skill (0.189 vs. 0.129): the least skilled woman the baseline hires has skill 16, the least skilled man 10 (experiment). SHAP also hides indirect causes: education has almost no SHAP value (0.001), yet in the simulation each level adds 2 skill points. Raising education alone changes the predicted probability by +0.001, but together with its effect on skill by +0.081 (experiment).

## References

- Barocas, S., Hardt, M., & Narayanan, A. (2023). *Fairness and machine learning: Limitations and opportunities*. MIT Press. https://fairmlbook.org
- Barocas, S., & Selbst, A. D. (2016). Big data's disparate impact. *California Law Review, 104*(3), 671–732. https://doi.org/10.15779/Z38BG31
- Hardt, M., Price, E., & Srebro, N. (2016). Equality of opportunity in supervised learning. *Advances in Neural Information Processing Systems 29*. https://arxiv.org/abs/1610.02413
- Kamiran, F., Karim, A., & Zhang, X. (2012). Decision theory for discrimination-aware classification. *2012 IEEE 12th International Conference on Data Mining*, 924–929. https://doi.org/10.1109/ICDM.2012.45
- Lundberg, S. M., & Lee, S.-I. (2017). A unified approach to interpreting model predictions. *Advances in Neural Information Processing Systems 30*. https://proceedings.neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html
