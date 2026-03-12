import numpy as np
import matplotlib.pyplot as plt
from math import sin

def bisection(f, a, b, eps):
    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# x·sin(x) - 1 = 0
f = lambda x: x * sin(x) - 1
root = bisection(f, 1, 2, 1e-4)

x = np.linspace(0, 4, 1000)
y = [f(xi) for xi in x]

plt.figure(figsize=(8, 5))
plt.plot(x, y, 'b-', linewidth=2)
plt.plot(root, f(root), 'ro', markersize=8)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.grid(True, alpha=0.3)
plt.title(f'x·sin(x) - 1 = 0\nКорень: x = {root:.6f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

print(f'Корень: x = {root:.10f}')