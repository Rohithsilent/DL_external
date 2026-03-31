import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Step 1: Data
X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
y = np.array([0, 0, 0, 1, 1, 1])  # 0 = Fail, 1 = Pass

# Step 2: Train model
model = DecisionTreeClassifier(max_depth=2)
model.fit(X, y)

# Step 3: Print tree as text
from sklearn.tree import export_text
tree_rules = export_text(model, feature_names=["Hours"])
print(tree_rules)

# Step 4: Visualize tree
plt.figure(figsize=(10, 6))
plot_tree(
    model,
    feature_names=["Hours"],
    class_names=["Fail", "Pass"],
    filled=True
)

plt.title("Decision Tree Structure")
plt.show()