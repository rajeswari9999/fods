import pandas as pd
import numpy as np
from scipy.stats import t

data = pd.read_csv('customer_reviews.csv')

product_category = input("Enter the product category you want to analyze: ")

category_data = data[data['product_category'] == product_category]['rating']

mean_rating = category_data.mean()
std_dev = category_data.std(ddof=1)  

confidence_level = 0.95

n = len(category_data)
critical_value = t.ppf(1 - (1 - confidence_level) / 2, n - 1)
margin_of_error = critical_value * std_dev / np.sqrt(n)

lower_bound = mean_rating - margin_of_error
upper_bound = mean_rating + margin_of_error

print(f"Product Category: {product_category}")
print(f"Mean Rating: {mean_rating}")
print(f"Confidence Interval: ({lower_bound}, {upper_bound})")
print(f"Margin of Error: {margin_of_error}")
