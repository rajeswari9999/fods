import numpy as np
from scipy.stats import t

drug_data = [132, 128, 127, 130, 133, 129, 131, 135, 130, 128, 134, 133, 131, 136, 129, 132, 130, 127, 133, 135, 131, 130, 129, 134, 132, 128, 127, 130, 133, 129, 131, 135, 130, 128, 134, 133, 131, 136, 129, 132, 130, 127, 133, 135, 131, 130, 129, 134]

placebo_data = [135, 133, 136, 132, 137, 136, 135, 134, 138, 136, 133, 135, 132, 137, 136, 135, 134, 138, 136, 133, 135, 132, 137, 136, 135, 134, 138, 136, 133, 135, 132, 137, 136, 135, 134, 138, 136, 133, 135, 132, 137, 136, 135, 134, 138, 136, 133, 135]

mean_drug = np.mean(drug_data)
std_drug = np.std(drug_data, ddof=1)
mean_placebo = np.mean(placebo_data)
std_placebo = np.std(placebo_data, ddof=1)

n_drug = len(drug_data)
se_drug = std_drug / np.sqrt(n_drug)
n_placebo = len(placebo_data)
se_placebo = std_placebo / np.sqrt(n_placebo)

t_value = t.ppf(0.975, n_drug - 1)

margin_of_error_drug = t_value * se_drug
margin_of_error_placebo = t_value * se_placebo

confidence_interval_drug = (mean_drug - margin_of_error_drug, mean_drug + margin_of_error_drug)
confidence_interval_placebo = (mean_placebo - margin_of_error_placebo, mean_placebo + margin_of_error_placebo)

print(f"95% Confidence Interval for the mean reduction in blood pressure for the drug group: \n{confidence_interval_drug}")
print(f"95% Confidence Interval for the mean reduction in blood pressure for the placebo group: \n{confidence_interval_placebo}")
