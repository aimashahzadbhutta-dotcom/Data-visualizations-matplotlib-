from matplotlib import pyplot as plt
#print(plt.style.available)
plt.style.use("ggplot")

drugs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
solubility = [0.8, 0.6, 0.9, 0.7, 0.4, 0.5, 0.8, 0.3, 0.6, 0.7]
toxicity = [0.1, 0.2, 0.05, 0.1, 0.3, 0.4, 0.1, 0.25, 0.5, 0.35]
activity = [0.75, 0.7, 0.85, 0.9, 0.95, 0.65, 0.8, 0.88, 0.72, 0.6]
labels = ['solubility', 'toxicity', 'activity']

plt.stackplot(drugs, solubility, toxicity, activity, labels=labels)
plt.title("Students category Represention")
plt.tight_layout()
plt.legend(loc=(0.07, 0.05))
plt.savefig("My awesome stack plot")
plt.show()