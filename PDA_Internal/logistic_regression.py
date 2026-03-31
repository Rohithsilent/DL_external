import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Step 1: Create simple data (Hours studied vs Pass/Fail)
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)   # input
y = np.array([0, 0, 0, 1, 1, 1])                 # output (0 = Fail, 1 = Pass)

# Step 2: Create and train model
model = LogisticRegression()
model.fit(X, y)

# Step 3: Predict values
y_pred = model.predict(X)

# Step 4: Plot data and decision boundary
plt.figure(figsize=(8, 5))

plt.scatter(X, y, label="Actual Data")  # actual points

# Plot decision boundary
x_values = np.linspace(0, 7, 100).reshape(-1, 1)
y_prob = model.predict_proba(x_values)[:, 1]  # probability of class 1

plt.plot(x_values, y_prob, label="Sigmoid Curve")

plt.xlabel("Hours Studied")
plt.ylabel("Probability of Passing")
plt.title("Logistic Regression Example")

plt.legend()
plt.grid(True)

plt.show()