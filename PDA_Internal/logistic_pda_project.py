import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
columns = [
    "Glucose",
    "BloodPressure",
    "Insulin",
    "BMI",
    "Age",
    "Outcome",
]

data = pd.read_csv(url, header=None, names=columns)

x = data[columns[:-1]]
y = data["Outcome"]


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=0)

model = LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)

accuracy = model.score(x_test,y_test)
print(f"Accuracy: {accuracy:.3f}")

y_pred = model.predict(x_test)

plt.figure(figsize=(6,4))

scatter = plt.scatter(
    x_test["Glucose"],
    x_test["Age"],
    c = y_pred,
    cmap = "coolwarm",
    alpha = 0.7,
)


plt.xlabel("Glucose")
plt.ylabel("Age")
plt.title("Predicted Diabetes Class (Logistic Regression)")
plt.colorbar(scatter, label="Predicted class (0 = no, 1 = yes)")
plt.tight_layout()
plt.show()