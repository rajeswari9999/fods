from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([[200, 12], [300, 24], [150, 6], [400, 36], [250, 18]])  
y = np.array([1, 1, 0, 1, 0]) 

clf = LogisticRegression()
clf.fit(X, y)

new_customer_features = list(map(float, input("Enter the usage minutes and contract duration of the new customer, separated by spaces: ").split()))

new_customer_features = np.array(new_customer_features).reshape(1, -1)

predicted_churn = clf.predict(new_customer_features)

if predicted_churn[0] == 1:
    print("The new customer is predicted to churn.")
elif predicted_churn[0] == 0:
    print("The new customer is predicted not to churn.")
else:
    print("Invalid prediction.")
