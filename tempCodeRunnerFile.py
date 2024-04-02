# Generate a range of feature values for plotting
# x_range = np.linspace(min(x), max(x), 100)
# y_range = [predict(xi, w, b) for xi in x_range]

# # Plot sigmoid function
# plt.plot(x_range, y_range, label='Sigmoid Function')

# # Plot decision boundary (at probability 0.5)
# plt.axhline(y=0.5, color='r', linestyle='--', label='Decision Boundary')

# # Plot sample data points
# plt.scatter(x, y, color='black', label='Sample Data')

# plt.xlabel('Feature Values')
# plt.ylabel('Probability')
# plt.title('Logistic Regression')
# plt.legend()
# plt.grid(True)
# plt.show()