# Part E – experiments for the notebook's last cell ("Optional: use this space for small experiments").
# Paste this whole file into that cell and run it after all cells above (ROC_MARGIN_CHOSEN = 0.48, PR_ETA_CHOSEN = 100).
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import cross_val_predict

sex_t = X_test[:, 5]
women, men = sex_t == 0, sex_t == 1
pred = {
    'Baseline': pipeline.predict(X_test).astype(int),
    'Remove sex': (predict_ns(X_test) >= 0.5).astype(int),
    'Reweighing': pipeline_rw.predict(X_test).astype(int),
    f'ROC (margin={ROC_MARGIN_CHOSEN})': apply_roc(ROC_MARGIN_CHOSEN).astype(int),
    f'Prejudice Remover (eta={PR_ETA_CHOSEN})': (predict_pr(X_test) >= 0.5).astype(int),
}
di = lambda p: p[women].mean() / p[men].mean()

# E1 – proxies: how well do the five other features reveal sex?
p_sex = cross_val_predict(LogisticRegression(max_iter=2000), df[FEATURE_ORDER[:5]], df.sex, cv=5, method='predict_proba')[:, 1]
print(f"E1  AUC sex from the 5 other features: {roc_auc_score(df.sex, p_sex):.3f} | "
      f"salary alone: {roc_auc_score(df.sex, df.expected_salary):.3f}")
band = (X_test[:, 0] >= 12) & (X_test[:, 0] <= 16)
print(f"    Remove sex, skill 12-16: women {pred['Remove sex'][band & women].mean():.1%}, men {pred['Remove sex'][band & men].mean():.1%}")
print(f"    salary weight: baseline {pipeline.named_steps['lr'].coef_[0][1]:+.3f}, remove sex {pipeline_ns.named_steps['lr'].coef_[0][1]:+.3f}")

# E2 / E5 – the same applicants, historic rule WITHOUT the sex bonus (sex_weight = 0)
df_fair = simulate_applicants(15000, RANDOM_STATE, sex_weight=0.0)
assert (df_fair[FEATURE_ORDER].values == df[FEATURE_ORDER].values).all()   # identical applicants
for name, d in [('historic rule', df), ('rule without sex bonus', df_fair)]:
    r = d.groupby('sex').recruited.mean()
    print(f"E2  {name:<23} women {r[0]:.1%}, men {r[1]:.1%}, DI {r[0] / r[1]:.3f}")
y_fair = df_fair.loc[df_test.index, 'recruited'].values
print("E5  accuracy vs. historic labels | vs. labels without the sex bonus")
for k, p in pred.items():
    print(f"    {k:<32} {np.mean(p == y_test):.3f} | {np.mean(p == y_fair):.3f}")

# E3 – how many final decisions does ROC change?
p_roc, p_base = pred[f'ROC (margin={ROC_MARGIN_CHOSEN})'], pred['Baseline']
in_band = np.abs(pipeline.predict_proba(X_test)[:, 1] - 0.5) <= ROC_MARGIN_CHOSEN
print(f"E3  ROC changes {np.sum(p_roc != p_base)} of {len(p_roc)} decisions: "
      f"{np.sum((p_base == 0) & (p_roc == 1))} women rejected->hired, {np.sum((p_base == 1) & (p_roc == 0))} men hired->rejected; "
      f"{in_band.sum()} applicants in the band, where decision == (sex is woman): {np.all(p_roc[in_band] == women[in_band])}")

# E4 – two 'models' with DI close to 1 that are clearly not fair
rng = np.random.default_rng(RANDOM_STATE)
lottery = (rng.random(len(y_test)) < 0.30).astype(int)
worst_women = p_base.copy()
w_idx = np.where(women)[0]
n_w = int(round(p_base[men].mean() * women.sum()))
worst_women[w_idx] = 0
worst_women[w_idx[np.argsort(pipeline.predict_proba(X_test[w_idx])[:, 1])[:n_w]]] = 1   # the women with the LOWEST scores
qualified = lambda p, g: p[g & (y_fair == 1)].mean()
for name, p in [('Lottery 30 %', lottery), ('Baseline men + lowest-scored women', worst_women)]:
    print(f"E4  {name:<35} DI {di(p):.3f}, accuracy {np.mean(p == y_test):.3f}, "
          f"qualified women hired {qualified(p, women):.1%}, qualified men hired {qualified(p, men):.1%}")

# E6 – skill vs. sex for women, and an indirect cause SHAP does not show
sv_w = np.abs(shap_values.values[women]).mean(0)
print(f"E6  mean |SHAP| for women: skill {sv_w[0]:.3f}, sex {sv_w[5]:.3f} | lowest skill hired: "
      f"women {X_test[women & (p_base == 1), 0].min():.0f}, men {X_test[men & (p_base == 1), 0].min():.0f}")
X_edu = X_test.copy(); X_edu[:, 3] = np.clip(X_edu[:, 3] + 1, 1, 4)
X_edu_skill = X_edu.copy(); X_edu_skill[:, 0] = np.clip(X_test[:, 0] + 2 * (X_edu[:, 3] - X_test[:, 3]), 0, 20)
p0 = predict_baseline(X_test)
print(f"    education +1: mean change in P = {np.mean(predict_baseline(X_edu) - p0):+.3f}; "
      f"with its effect on skill (+2 per level, as in the simulation): {np.mean(predict_baseline(X_edu_skill) - p0):+.3f}")

# D1c – applicant #1460 under the other models
a = df.loc[[1460], FEATURE_ORDER].values
a_man = a.copy(); a_man[0, 5] = 1
print(f"D1c #1460: baseline {predict_baseline(a)[0]:.3f}, same profile as a man {predict_baseline(a_man)[0]:.3f}, "
      f"remove sex {predict_ns(a)[0]:.3f}, reweighing {predict_rw(a)[0]:.3f}, Prejudice Remover {predict_pr(a)[0]:.3f}; "
      f"label without sex bonus: {df_fair.loc[1460, 'recruited']}")
