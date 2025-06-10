import numpy as np
import matplotlib.pyplot as plt


# vec = [1, 2, 3, 4, 5]

vec = np.array([1, 2, 4, 5])
matrix = np.array([[1, 2], [3, 4]])
print(vec.shape)

grades_jan = [56, 64, 78, 100]
grades_ben = [86, 94, 98, 90]

plt.scatter(range(len(grades_jan)), grades_jan, c="blue")
plt.scatter(range(len(grades_ben)), grades_ben, c="red")
plt.xlabel("Courses")
plt.ylabel("Grades")
plt.legend(["Jan", "Ben"])
plt.title("Gerades of Studenst")
plt.show()
