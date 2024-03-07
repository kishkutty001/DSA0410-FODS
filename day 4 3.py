import numpy as np
from scipy import stats

design_A_conversion = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0]
design_B_conversion = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1]

t_stat, p_value = stats.ttest_ind(design_A_conversion, design_B_conversion)

alpha = 0.05

print("Hypothesis Test:")
print("T statistic:",t_stat)
print("P_value",p_value)

if p_value < alpha:
    print("Reject the null hypothesis. There is a statistically significant difference in mean conversion rates.")
else:
    print("Fail to reject the null hypothesis. There is no statistically significant difference in mean conversion rates.")
