import cv2
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering


image =cv2.imread("/run/media/rohith/Mine/Projects/DL_external/PDA_Internal/Abstract - Nature.jpg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

image = cv2.resize(image,(100,100))

pixels = image.reshape((-1,3))

model = AgglomerativeClustering(n_clusters=4)
labels = model.fit_predict(pixels)

segmented = labels.reshape(image.shape[:2])


plt.figure(figsize=(10,6))

plt.subplot(1,2,1)
plt.imshow(image)
plt.title("image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(segmented,cmap='viridis')
plt.title("segmented")
plt.axis("off")
plt.show()