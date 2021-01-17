import math
import random
import numpy as np
import matplotlib.pyplot as plt

i = 1
s = []

for i in range(10000):
	x = math.sqrt(-2 * math.log(random.random())) * math.cos(2 * math.pi * random.random())
	s.append(x)
plt.hist(s, bins = 50, edgecolor = 'k')

plt.title('Standard Normal Distribution')
plt.xlabel('Variable X')
plt.ylabel('Count')

plt.show()