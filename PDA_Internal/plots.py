import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample data
subjects = ["Math", "Science", "English", "History"]
marks = [85, 90, 78, 88]

# 🔸 1. Bar Chart (Horizontal)
plt.figure()
plt.bar(subjects, marks)
plt.title("Bar Chart (Horizontal)")
plt.xlabel("Marks")
plt.ylabel("Subjects")
plt.show()

# 🔸 2. Column Chart (Vertical Bar)
plt.figure()
plt.barh(subjects, marks)
plt.title("Column Chart (Vertical)")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 🔸 3. Line Chart
plt.figure()
plt.plot(subjects, marks, marker='o')
plt.title("Line Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 🔸 4. 3D Chart
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4]
y = marks
z = [0, 0, 0, 0]

ax.bar3d(x, z, z, 0.5, 0.5, y)

ax.set_xlabel("Subjects")
ax.set_ylabel("Y")
ax.set_zlabel("Marks")

plt.title("3D Chart")
plt.show()