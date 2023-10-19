import numpy as np
from scipy.stats import ttest_ind

group_A = [0.15, 0.18, 0.22, 0.20, 0.16, 0.19, 0.21, 0.17, 0.23, 0.18]
group_B = [0.12, 0.14, 0.16, 0.13, 0.11, 0.15, 0.14, 0.12, 0.17, 0.13]

t_statistic, p_value = ttest_ind(group_A, group_B)

alpha = 0.05


if p_value < alpha:
    print(f"There is a statistically significant difference between the mean conversion rates of website designs A and B\n (p-value = {p_value:.4f})")
else:
    print(f"There is no statistically significant difference between the mean conversion rates of website designs A and B\n (p-value = {p_value:.4f})")
