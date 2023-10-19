import numpy as np
import pandas as pd
from scipy.stats import t


def calculate_confidence_interval(sample, confidence_level, precision):
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)
    critical_value = t.ppf(1 - (1 - confidence_level) / 2, len(sample) - 1)
    margin_of_error = critical_value * sample_std / np.sqrt(len(sample))
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error

    return sample_mean, lower_bound, upper_bound, margin_of_error

data = pd.read_csv('rare_elements.csv')

sample_size = int(input("Enter sample size: "))
confidence_level = float(input("Enter confidence level (between 0 and 1): "))
precision = float(input("Enter desired level of precision: "))

sample = data.sample(n=sample_size, random_state=1)['concentration'].values  

sample_mean, lower_bound, upper_bound, margin_of_error = calculate_confidence_interval(sample, confidence_level, precision)

print(f"Sample Mean: {sample_mean}")
print(f"Confidence Interval: ({lower_bound}, {upper_bound})")
print(f"Margin of Error: {margin_of_error}")
