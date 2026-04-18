import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

hours = np.array([0,1,2,3,4,5]).reshape(-1,1)
results = np.array([0,0,0,1,1,1])

model = DecisionTreeClassifier(max_depth=1)
model.fit(hours,results)

from sklearn.tree import export_text

tree_rules = export_text(model, feature_names=["hours"])
print(tree_rules)

plt.figure(figsize = (10,6))
plot_tree(
    model,
    feature_names=["hours"],
    class_names = ["fail","pass"],
    filled=True
)

plt.show()
