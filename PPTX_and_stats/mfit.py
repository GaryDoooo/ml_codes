import statsmodels.api as sm
from statsmodels.formula.api import *
from pandas import DataFrame as DF
import pandas as pd
from statsmodels.regression.mixed_linear_model import MixedLM
######## Own Modules ##########
#  from utilities import group_by2factors


def SSA_SSB(data):
    # Source: https://www.pythonfordatascience.org/factorial-anova-python/
    # The direct output of the stats model python is different from Minitab
    # and JMP.
    # However, at least the sums of square are correct.
    l = []
    for i, ith_A in enumerate(data):
        for j, ith_A_jth_B in enumerate(ith_A):
            for k in ith_A_jth_B:
                l.append([i, j, k])
    df = DF(l, columns=["A", "B", "Y"])
    # Step 1: Fit the full model
    full_model = ols("Y ~ C(A, Sum) + C(B, Sum) + C(A, Sum):C(B, Sum)",
                     data=df).fit()

    # To get the complete ANOVA table with Type 3 SS
    anova_table = sm.stats.anova_lm(full_model, typ=3)
    # sample output, the Intercept is the [0] element
    #  Intercept              1812.640170
    #  C(A, Sum)                73.870879
    #  C(B, Sum)                51.032793
    #  C(A, Sum):C(B, Sum)      30.603340
    #  Residual                157.680773
    #  Name: sum_sq, dtype: float64
    return (anova_table.sum_sq.iloc[1],  # SSA
            anova_table.sum_sq.iloc[2],  # SSB
            anova_table.sum_sq.iloc[3])  # SSAB
    # Both type III


def try1():
    df = pd.read_csv('mfit.csv', sep='\t')
    print(df)
    #  formula = 'MTF ~ AD + FS + Skew + FS:AD + AD:Skew + FS:Skew'
    formula = 'MTF ~ AD + FS + AD:FS'  # + AD:Skew + FS:Skew'
    # Fit the model
    model = gls(formula, data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=3)

    # Summarize the results
    print(model.summary())
    print(anova_table)
    #  model = MixedLM.from_formula(formula, data=df, groups='Group')
    #  # Fit the model
    #  result = model.fit(reml=True)
    #  print(result.summary())
    #


if __name__ == "__main__":
    try1()
