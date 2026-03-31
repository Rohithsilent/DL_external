import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Step 1: Data
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y = np.array([0, 0, 0, 1, 1, 1])  # 0 = Fail, 1 = Pass

# Step 2: Train model
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

# Step 3: Predictions on training data
y_pred = model.predict(X)

# Step 4: Accuracy
accuracy = accuracy_score(y, y_pred)

print("Predictions:", y_pred)
print("Actual:", y)
print("Accuracy:", accuracy)

# Step 5: Predict new value
new_data = np.array([[3.5]])
prediction = model.predict(new_data)

print("Prediction for 3.5 hours:", prediction)