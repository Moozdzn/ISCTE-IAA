import matplotlib.pyplot as plt
import numpy as np
import random
import math

# 1
mean1 = [3, 3]
cov1 = [[1, 0], [0, 1]]
mean2 = [-3, -3]
cov2 = [[2, 0], [0, 5]]
# diagonal covariance
x, y = np.random.multivariate_normal(mean1, cov1, 5000).T
z, h = np.random.multivariate_normal(mean2, cov2, 5000).T

'''plt.plot(x, y, 'x')
plt.plot(z, h, 'x')
plt.axis('equal')
plt.show()'''

x = np.append(x, z)
y = np.append(y, h)
random.seed(30)
random.shuffle(x)
random.seed(30)
random.shuffle(y)

'''plt.plot(x, y, 'x')
plt.axis('equal')
plt.show()'''
r1_idx = random.randint(0, 4999 * 2)
r2_idx = random.randint(0, 4999 * 2)
r1 = [x[r1_idx], y[r1_idx]]
r2 = [x[r2_idx], y[r2_idx]]


# 2
def distance_2_points(point_1, point_2):
    return math.sqrt(math.pow(point_2[0] - point_1[0], 2) + math.pow(point_2[1] - point_1[1], 2))


r1_x = []
r2_x = []
r1_y = []
r2_y = []

for j in range(10):

    for i in range(len(x)):

        alfa = 0.0010
        distance_to_r1 = distance_2_points(r1, [x[i], y[i]])
        distance_to_r2 = distance_2_points(r2, [x[i], y[i]])
        if distance_to_r1 < distance_to_r2:
            r1[0] = (1 - alfa) * r1[0] + alfa * x[i]
            r1[1] = (1 - alfa) * r1[1] + alfa * y[i]
        else:
            r2[0] = (1 - alfa) * r2[0] + alfa * x[i]
            r2[1] = (1 - alfa) * r2[1] + alfa * y[i]
        if j == 0:
            r1_x.append(r1[0])
            r1_y.append(r1[1])
            r2_x.append(r2[0])
            r2_y.append(r2[1])
print(r1_x)
plt.plot(x, y, 'x')
plt.plot(r1_x, r1_y, 'x')
plt.plot(r2_x, r2_y, 'o')
plt.axis('equal')
plt.show()
