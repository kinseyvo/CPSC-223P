import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) 

plt.title('Cubes')
plt.xlabel('Value')
plt.ylabel('Cubed Value')

plt.show()