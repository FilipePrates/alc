# Álgebra Linear Computacional - 2023.1
# Trabalho 02
# Aluna: Filipe Santos Pacheco Prates e Lidiana Souza dos Anjos

import pandas as pd
import numpy as np

tol = float(input("Type the tolerance: \n"))

v = [1, 1, 1]
new_v = [0, 0, 0]

k = 0
tolk = 10
cond = True
iter = 0
while tolk >= tol:

    f = [16*v[0]**4 + 16*v[1]**4 + v[2]**4 - 16, v[0]**2 + v[1]**2 + v[2]**2 - 3, v[0]**3 - v[1] + v[2] - 1]

    j = [[64*v[0]**3, 64*v[1]**3, 4*v[2]**3], [2*v[0], 2*v[1], 2*v[2]], [3*v[0]**2, -1, 1]]

    inv_j = np.linalg.inv(j)
    delta_x = -(np.matmul(inv_j, f))
    new_v = v + delta_x

    tolk = np.linalg.norm(delta_x)/np.linalg.norm(new_v)

    v = new_v
    iter += 1
    if tolk >= tol:
        v = new_v

print("The solution is \n", new_v)
print("Number of iterations \n", iter)






