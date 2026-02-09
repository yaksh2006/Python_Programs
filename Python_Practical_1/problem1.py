import numpy as np
rows1 = -1 * np.ones((1, 4))
row2 = np.zeros((1, 4))
row3 = 2 * np.ones((1, 4))
result = np.vstack((rows1, row2, row3))
print(result)