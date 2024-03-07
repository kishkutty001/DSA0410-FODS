import numpy as np
from scipy import stats

grp1 = [80, 85, 88, 92, 78, 86, 89, 95, 90, 82]
grp2 = [75, 88, 85, 79, 92, 87, 93, 80, 85, 88]

mean_grp1 = np.mean(grp1)
mean_grp2 = np.mean(grp2)

print("mean of group1 score:",mean_grp1)
print("mean of group2 score:",mean_grp2 )

ci_group1 = stats.t.interval(0.95, len(grp1) - 1, loc=mean_grp1)
ci_group2 = stats.t.interval(0.95, len(grp2) - 1, loc=mean_grp2 )

print("95% confident interval group1:",ci_group1)
print("95% confident interval group1:",ci_group2)

t_stat, p_value = stats.ttest_ind(grp1, grp2)

alpha = 0.05
print("\nHypothesis Test:")
print("T-statistic:",t_stat)
print("P-value:",p_value )

if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference between the two groups.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference between the two groups.")

