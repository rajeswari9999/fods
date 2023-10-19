from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])

kmeans = KMeans(n_clusters=2, random_state=0) 
kmeans.fit(X)

new_customer_features = list(map(float, input("Enter the shopping-related features of the new customer, separated by spaces: ").split()))

new_customer_features = np.array(new_customer_features).reshape(1, -1)


predicted_segment = kmeans.predict(new_customer_features)

print(f"The new customer is assigned to segment {predicted_segment[0]}")
