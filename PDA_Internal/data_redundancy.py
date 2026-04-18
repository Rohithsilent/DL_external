import pandas as pd

data = {
    "Name": ["A", "B", "C", "A", "B"],
    "Marks": [85, 90, 88, 85, 90]
}

df = pd.DataFrame(data)

duplicates = df[df.duplicated()]
print(duplicates)

clean = df.drop_duplicates()
print(clean)