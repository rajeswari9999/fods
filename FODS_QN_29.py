import pandas as pd

df = pd.read_csv('stock_data.csv')

stock_variability = df['Closing_Price'].std()

if stock_variability < 10:
    print("The stock prices have low variability, indicating a relatively stable price movement.")
elif 10 <= stock_variability < 50:
    print("The stock prices have moderate variability, indicating some fluctuations in price movement.")
else:
    print("The stock prices have high variability, indicating significant fluctuations in price movement.")

print(f"The variability of stock prices is: {stock_variability}")
