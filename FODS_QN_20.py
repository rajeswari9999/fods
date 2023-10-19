from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

new_flower_features = list(map(float, input("Enter the sepal length, sepal width, petal length, and petal width of the new flower, separated by spaces: ").split()))

new_flower_features = np.array(new_flower_features).reshape(1, -1)

prediction = clf.predict(new_flower_features)

species = iris.target_names[prediction][0]
print(f"The predicted species of the new flower is: {species}")
