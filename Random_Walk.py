from random_walk import RandomWalk
from matplotlib import pyplot as plt
import seaborn as sns

### create a "RandomWalk" instance to function ###
rw = RandomWalk(50000)
rw.fill_walk()

plt.style.use('seaborn')
fig, ax = plt.subplots()

### plot each point ; highlight the 1st & last point with different colors ###
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Oranges, edgecolor = 'none', s = 1)
ax.scatter(0, 0, c = 'red', edgecolor = 'none', s = 20)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'blue', edgecolor = 'none', s = 20)

### remove x & y axis ###
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

### set chart title & label axes ###
ax.set_title("Random Walk", fontsize = 24)

plt.show()