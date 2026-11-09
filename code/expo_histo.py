from matplotlib import pyplot as plt 
import numpy as np
plt.style.use("ggplot")
#print(plt.style.available)

scores = np.random.exponential(scale=10, size=100)
scores = np.clip(scores, 0, 100)
plt.hist(scores, bins=10, color="yellow", edgecolor='black')

plt.title("Exam scores")
plt.xlabel("Scores")
plt.ylabel("Number of students")
plt.savefig("My pretty expo_histo")
plt.show()