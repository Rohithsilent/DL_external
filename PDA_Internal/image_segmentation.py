import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

# Step 1: Load image (use your own downloaded image path)
image = cv2.imread("/run/media/rohith/Mine/Projects/DL_external/PDA_Internal/Abstract - Nature.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Resize for faster processing (important!)
image = cv2.resize(image, (100, 100))

# Step 2: Reshape image to 2D array (pixels)
pixels = image.reshape((-1, 3))

# Step 3: Apply Hierarchical Clustering
model = AgglomerativeClustering(n_clusters=4)
labels = model.fit_predict(pixels)

# Step 4: Convert labels back to image shape
segmented = labels.reshape(image.shape[:2])

# Step 5: Display results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(segmented, cmap='viridis')
plt.title("Segmented Image (Hierarchical)")
plt.axis("off")

plt.show()