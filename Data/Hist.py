import numpy as np; np.random.seed(13)
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
data = [26, 30, 22, 15, 21, 24, 28, 32, 24, 25, 18, 35]
bins = len(data)

plt.hist(data, bins=bins, edgecolor='black')

plt.show()