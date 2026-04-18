import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

hours = np.array([0,1,2,3,4,5]).reshape(-1,1)
results = np.array([0,0,0,1,1,1])


model = LogisticRegression()

model.fit(hours,results)

x_values = np.linspace(0,5,50).reshape(-1,1)
predicted = model.predict_proba(x_values)[:,1]

plt.scatter(hours,results, color='red',marker='o',label='actual data')
plt.plot(x_values,predicted,color='blue',label='predicted')
plt.xlabel('hours')
plt.ylabel('results')
plt.legend()
plt.show()