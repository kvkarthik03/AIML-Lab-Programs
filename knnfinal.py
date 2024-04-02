import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix

def calculate_distance(x1,x2):
    return np.sqrt(np.sum((x1-x2)**2))

def knn_predict(X_train,y_train,x_test,k):
    distances = []

    for i in range(len(X_train)):
        distance = calculate_distance(x_test,X_train[i])
        distances.append((distance,y_train[i]))
    
    distances.sort(key=lambda x: x[0])
    nearest_neighbours = distances[:k]
    class_votes = {}

    for neighbour in nearest_neighbours:
        neighbour_class = neighbour[1]

        if neighbour_class in class_votes:
            class_votes[neighbour_class] += 1
        else:
            class_votes[neighbour_class] = 1
    predicted_class = max(class_votes, key=class_votes.get)
    return predicted_class

iris = load_iris()
X,y = iris.data, iris.target
class_names = iris.target_names

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.4,random_state=42)

k = 3
for i in range(len(X_test)):
    predicted_class = knn_predict(X_train,y_train,X_test[i],k)
    print(f"Predicted class for {X_test[i]}: {predicted_class}, Actual class: {y_test[i]}")

y_pred = [knn_predict(X_train,y_train,X_test[i],k) for i in range(len(X_test))]

print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=class_names))

print("Confusion Matrix")
print(confusion_matrix(y_test,y_pred))