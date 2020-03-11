import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import sort
plt.style.use('fivethirtyeight')
data = [26, 30, 22, 15, 21, 24, 28, 32, 24, 25, 18, 35, 100]
bins = len(data)
#bins = sort(data)
plt.hist(data, bins=bins, edgecolor='black')
med = np.median(data)
plt.tight_layout()
plt.axvline(med, color='#666FFF', label='Median')
plt.show()