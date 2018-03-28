import numpy as np
from timeit import timeit
import multiprocessing as mp
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.patches import RegularPolygon

from IPython.display import HTML
import matplotlib.patches as patches

# Initialize the petri dish for this game
DISH = np.random.randint(2,size=(200,200))

deltas = [(-1, -1), (-1, 0), (-1, 1),
		  ( 0, -1),          ( 0, 1),
		  ( 1, -1), ( 1, 0), ( 1, 1)]

#in my backyard function
def calc_step(x, y, surroundings):
	count = 0
	for dx, dy in deltas:
		cmpx = x + dx
		cmpy = y + dy
		count = count + surroundings[cmpx][cmpy]
	value = DISH[x,y]
	if value == 1.0:
		if 2.0 <= count <= 3.0:
			value = 1
		else: 
			value = 0
	else:
		if count == 3:
			value = 1
	return count, value 

# Game Of Life Ruleset:

# Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# calculates the next generation of the population with stadard ruleset in loop
def evolve_standard_ruleset_loop(X):
	volved = X.copy()
	for x in range(0, X.shape[0] - 1):
		for y in range(0, X.shape[1] - 1):
			neighbours, newvalue = calc_step(x,y, X)
			volved[x][y] = newvalue
	return volved

def evolve_standard_ruleset_numpy(X):
    nbrs_count = np.sum(np.roll(np.roll(X, i, 0), j, 1)
                     for i in (-1, 0, 1) for j in (-1, 0, 1)
                     if (i != 0 or j != 0))
    return (nbrs_count == 3) | (X & (nbrs_count == 2))

def evolve_standard_ruleset_scipy(X):
    from scipy.signal import convolve2d
    nbrs_count = convolve2d(X, np.ones((3, 3)), mode='same', boundary='wrap') - X
    return (nbrs_count == 3) | (X & (nbrs_count == 2))


fig = plt.figure(figsize = (15,15))
im = plt.imshow(DISH, animated=True)

def updatefig(*args):
	global DISH
	DISH = evolve_standard_ruleset_numpy(DISH)
	im.set_array(DISH)
	return im,

anim = animation.FuncAnimation(fig, updatefig, interval=16, blit=True)

#print(timeit(lambda: evolve_standard_ruleset_scipy(DISH), number = 100))
#print(timeit(lambda: evolve_standard_ruleset_numpy(DISH), number = 100))

plt.show()
##HTML(anim.to_html5_video())
