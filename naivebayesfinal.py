import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

iris = load_iris()
X, y = iris.data, iris.target
class_names = iris.target_names

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Calculate class priors with Laplace smoothing
priors = np.bincount(y_train) / (len(y_train) + len(np.unique(y_train)))

# Calculate mean and variance for each feature in each class
mean = np.array([X_train[y_train == c].mean(axis=0) for c in np.unique(y_train)])
var = np.array([X_train[y_train == c].var(axis=0) for c in np.unique(y_train)])

def predict_naive_bayes(x):
    posteriors = []
    for m, v, p in zip(mean, var, priors):
        log_priors = np.log(p)
        log_likelihood = np.sum(-0.5 * np.log(2 * np.pi * v) - 0.5 * ((x - m) ** 2 / v))
        posteriors.append(log_likelihood + log_priors)
    return np.argmax(posteriors)

y_pred = [predict_naive_bayes(x) for x in X_test]

print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=class_names))

print("Confusion Matrix")
print(confusion_matrix(y_test,y_pred))

