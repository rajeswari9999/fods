from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1000, 2], [1500, 3], [1200, 2], [1700, 3], [800, 1]])  
y = np.array([300000, 450000, 360000, 500000, 250000])  

reg = LinearRegression()
reg.fit(X, y)

new_house_features = list(map(float, input("Enter the area and number of bedrooms of the new house, separated by spaces: ").split()))

new_house_features = np.array(new_house_features).reshape(1, -1)

predicted_price = reg.predict(new_house_features)

print(f"The predicted price of the new house is: {predicted_price[0]}")
