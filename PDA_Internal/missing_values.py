import pandas as pd
import numpy as np

data = {
    "Age": [20, np.nan, 22, 19],
    "Marks": [85, 90, np.nan, 88]
}

df = pd.DataFrame(data)

mean_age = df["Age"].mean()
mean_marks = df["Marks"].mean()

df["Age"] = df["Age"].fillna(mean_age)
df["Marks"] = df["Marks"].fillna(mean_marks)

print(df)