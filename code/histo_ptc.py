from matplotlib import pyplot as plt 
import numpy as np
plt.style.use("ggplot")

scores = np.random.normal(loc=80, scale=10, size=100)
scores = np.clip(scores, 0, 100)
plt.hist(scores, bins=10, color="orange", edgecolor='black')

plt.title("Exam scores")
plt.xlabel("Scores")
plt.ylabel("Number of students")
plt.savefig("My pretty histo")
plt.show()