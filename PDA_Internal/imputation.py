import numpy as np
import pandas as pd

data = {
    "age":[34,32,np.nan,45,28],
    "income":[50000,60000,55000,np.nan,45000],
}


df = pd.DataFrame(data)
mean_age = df["age"].mean()
mean_income = df["income"].mean()


# mean imputation technique

df["age"] = df["age"].fillna(mean_age)
df["income"] = df["income"].fillna(mean_income)

print(df)