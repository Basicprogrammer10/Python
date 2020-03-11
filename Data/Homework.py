#import numpy as np; np.random.seed(13)
import matplotlib.pyplot as plt


data = [26, 30, 22, 15, 21, 24, 28, 32, 24, 25, 18, 35]

plt.hist(data, ec="k")

plt.show()