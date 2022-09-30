import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
plt.title('Cubes')
plt.xlabel('Value')
plt.ylabel('Cubed Value')
ax.plot(y_values)

plt.show()
