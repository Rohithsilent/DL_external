import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

x = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y = np.array([0, 0, 0, 1, 1, 1])  # 0 = Fail, 1 = Pass

model = RandomForestClassifier(n_estimators=10,random_state=42)
model.fit(x,y)

y_pred = model.predict(x)

accuracy = accuracy_score(y,y_pred)
print(accuracy)

new_data = np.array([[8]])
predicted_new = model.predict(new_data)
print(predicted_new)