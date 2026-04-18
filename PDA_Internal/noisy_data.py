import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "marks": [85, 90, 300, 88, 87]
}

df = pd.DataFrame(data)

q1 =  df["marks"].quantile(0.25)
q2 = df["marks"].quantile(0.75)

iqr = q2-q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q2 + 1.5 * iqr


outliers = df[(df["marks"]<lower_bound) | (df["marks"]>upper_bound)]
print(outliers)


clean_df = df[(df["marks"]>=lower_bound)&(df["marks"]<=upper_bound)]
print(clean_df)