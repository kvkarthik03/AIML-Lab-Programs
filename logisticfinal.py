import math
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def predict(x, w, b):
    # Linear model followed by sigmoid activation
    return sigmoid(x * w + b)

def train(x, y, learning_rate):
    # Initialize weights and bias with zeros
    w = 0
    b = 0

    # Loop through data points, update weights based on sign of error
    for i in range(len(x)):
        # Calculate predicted value
        predicted = predict(x[i], w, b)
        # Update weights based on difference between prediction and actual value
        error = y[i] - predicted
        w += learning_rate * x[i] * error
        b += learning_rate * error

    return w, b

# Sample data (X - single feature, y - labels)
x = [1, 2, 3]  # Feature values
y = [1, 0, 1]  # Labels (can be 1 or 0 for this example)

# Train the model with learning rate (adjust as needed)
w, b = train(x, y, 0.1)

# Make a prediction on new data point
new_data = 4  # Replace with your new data point

prediction = predict(new_data, w, b)
print(prediction)

# Print the prediction (positive or negative based on sign)
if prediction > 0.5:
    print("Positive")
else:
    print("Negative")

# Additional sample data for testing
x_test = [4, 5, 6]  # Feature values
y_test = [1, 0, 1]  # Actual labels

# Make predictions on test data
predictions = [predict(data_point, w, b) for data_point in x_test]

# Print predictions and actual labels
print("Predictions:", predictions)
print("Actual Labels:", y_test)

# Evaluate accuracy
correct_predictions = [(p > 0.5) == actual_label for p, actual_label in zip(predictions, y_test)]
accuracy = sum(correct_predictions) / len(correct_predictions)
print("Accuracy:", accuracy)

