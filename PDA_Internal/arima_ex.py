import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

data = [10, 12, 13, 15, 18, 20, 22, 21, 23, 25, 28, 30]

model = ARIMA(data,order=(1,1,1))
model_fit = model.fit()

forecast = model_fit.forecast(steps=5)

forecast_index = range(len(data), len(data)+5)

plt.plot(range(len(data)),data,marker='o',color='blue',label='actual')
plt.plot(forecast_index,forecast,marker='o',linestyle='--',color='red',label='forecast')
plt.xlabel('time')
plt.ylabel('values')
plt.grid(True)
plt.legend()
plt.show()
