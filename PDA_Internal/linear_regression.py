import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


hours = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
scores = np.array([2, 4, 5, 4, 5])

model = LinearRegression()
model.fit(hours, scores)

scores_predict = model.predict(hours)

plt.figure(figsize=(10, 6))

plt.scatter(hours,scores, marker='o',label='actual scores')
plt.plot(hours, scores_predict, color='red', label='predicted scores')
plt.xlabel('Hours Studied')
plt.ylabel('Scores')
plt.title('Linear Regression: Hours Studied vs Scores')
plt.legend()
plt.grid()
plt.show()