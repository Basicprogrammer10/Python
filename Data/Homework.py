#import numpy as np; np.random.seed(13)
import matplotlib.pyplot as plt


data = [70, 70, 70, 70, 75, 75, 75, 75, 75, 75, 80, 80, 80, 80, 80, 80, 85, 85, 85, 85, 90, 90, 90, 95, 95, 100]
plt.hist(data, ec="k")

plt.show()