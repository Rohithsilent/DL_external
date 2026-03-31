import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Step 1: Create time series data (example: monthly values)
data = [10, 12, 13, 15, 18, 20, 22, 21, 23, 25, 28, 30]

# Step 2: Fit ARIMA model (p=1, d=1, q=1)
model = ARIMA(data, order=(1, 1, 1))
model_fit = model.fit()

# Step 3: Make predictions (future 5 steps)
forecast = model_fit.forecast(steps=5)

# Step 4: Plot original + forecast
plt.figure(figsize=(8, 5))

# Original data
plt.plot(range(len(data)), data, label="Original Data", marker='o')

# Forecast data
forecast_index = range(len(data), len(data) + 5)
plt.plot(forecast_index, forecast, label="Forecast", marker='o', linestyle='--')

plt.xlabel("Time")
plt.ylabel("Values")
plt.title("ARIMA Forecast Example")

plt.legend()
plt.grid(True)

plt.show()