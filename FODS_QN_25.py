from sklearn.tree import DecisionTreeRegressor, export_text
import numpy as np

X = np.array([[50000, 3, 0, 1], [80000, 5, 1, 0], [20000, 1, 2, 1], [60000, 2, 0, 0]])
y = np.array([25000, 20000, 30000, 28000])

reg = DecisionTreeRegressor()
reg.fit(X, y)

new_car_features = list(map(float, input("Enter the mileage, age, brand, and engine type of the new car, separated by spaces: ").split()))

new_car_features = np.array(new_car_features).reshape(1, -1)

predicted_price = reg.predict(new_car_features)

tree_rules = export_text(reg, feature_names=['Mileage', 'Age', 'Brand', 'Engine Type'])
print("Decision Path:")
print(tree_rules)

print(f"The predicted price of the new car is: {predicted_price[0]}")
