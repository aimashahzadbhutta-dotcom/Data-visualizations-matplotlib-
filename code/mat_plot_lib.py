from matplotlib import pyplot as plt 

x = [0.1, 0.2, 0.05, 0.1, 0.3, 0.4, 0.1, 0.25, 0.5, 0.35]
y = [0.75, 0.7, 0.85, 0.9, 0.95, 0.65, 0.8, 0.88, 0.72, 0.6]

plt.plot(x, y, color='y', linewidth=3, label='toxicity by activity')

y1 = [180, 206, 129, 334, 493, 308, 312, 602, 454, 320]

plt.plot(x, y1, color='r', label='toxicity by molecular_weight')

x1 = [0.8, 0.6, 0.9, 0.7, 0.4, 0.5, 0.8, 0.3, 0.6, 0.7]
plt.plot(x, x1, color='k',linestyle='--', label='toxicity by solubility') 

plt.xlabel('toxicity')
plt.ylabel('activity')
plt.title('toxicity by activity')

#plt.legend(['toxicity by activity', 'toxicity by molecular_weight'])
#fmt = '[marker][line][color]'

plt.tight_layout()
plt.grid()
plt.legend()
plt.savefig("x_vs_y.png")
plt.show()
