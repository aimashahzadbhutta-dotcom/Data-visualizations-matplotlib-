import numpy as np
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

x = [0.1, 0.2, 0.05, 0.1, 0.3, 0.4, 0.1, 0.25, 0.5, 0.35]
y = [0.75, 0.7, 0.85, 0.9, 0.95, 0.65, 0.8, 0.88, 0.72, 0.6]

width = 0.25
new_x = np.arange(len(x))

plt.bar(new_x + width, y, color='y', width=width, label='toxicity by activity')

y1 = [0.3, 0.4, 0.5, 0.6, 0.6, 0.7, 0.7, 0.8, 0.9, 0.9]

plt.bar(new_x, y1, color='g', width=width, label='toxicity by molecular_weight')

x1 = [0.8, 0.6, 0.9, 0.7, 0.4, 0.5, 0.8, 0.3, 0.6, 0.7]
plt.bar(new_x - width, x1, color='b', width=width, label='toxicity by solubility') 

plt.xlabel('toxicity')
plt.ylabel('activity')
plt.title('toxicity by activity')

#plt.legend(['toxicity by activity', 'toxicity by molecular_weight'])
#fmt = '[marker][line][color]'

plt.xticks(ticks=new_x, labels=x)
plt.tight_layout()
plt.legend()
plt.savefig("x1_vs_y1.png")
plt.show()

