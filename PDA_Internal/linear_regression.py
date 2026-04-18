import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

hours = np.array([1,2,3,4,5]).reshape(-1,1)
marks = np.array([2,3,4,5,5])

model = LinearRegression()
model.fit(hours,marks)

predicted = model.predict(hours)

plt.scatter(hours,marks,marker='o',color='red',label='actual_data')
plt.plot(hours,predicted, color = 'blue',label='predicted')
plt.xlabel('hours')
plt.ylabel('marks')
plt.legend()
plt.show()

predicted_6 = model.predict([[6]])

print(predicted_6)