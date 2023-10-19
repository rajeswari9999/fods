from sklearn.neighbors import KNeighborsClassifier
import numpy as np

X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])  
y = np.array([0, 0, 1, 1])  

knn = KNeighborsClassifier(n_neighbors=3) 
knn.fit(X, y)

new_patient_features = list(map(float, input("Enter the patient's features separated by spaces: ").split()))

new_patient_features = np.array(new_patient_features).reshape(1, -1)

prediction = knn.predict(new_patient_features)

if prediction[0] == 0:
    print("The patient does not have the medical condition.")
elif prediction[0] == 1:
    print("The patient has the medical condition.")
else:
    print("Invalid prediction.")

