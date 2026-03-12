import numpy as np
import matplotlib.pyplot as plt
from math import sin, log10

def bisection(f, a, b, eps=1e-6):
    for _ in range(100):
        c = (a + b) / 2
        if abs(f(c)) < eps or (b - a) / 2 < eps:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

def plot_and_solve(f, a, b, interval, title):
    root = bisection(f, interval[0], interval[1])
    
    x = np.linspace(a, b, 1000)
    y = [f(xi) for xi in x]
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, 'b-', linewidth=2)
    plt.plot(root, f(root), 'ro', markersize=8)
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.grid(True, alpha=0.3)
    plt.title(f'{title}\nКорень: x = {root:.6f}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()
    
    return root

# Уравнение a: lg(x) + 6 - x² = 0
f1 = lambda x: log10(x) + 6 - x**2
root1 = plot_and_solve(f1, 0.1, 4, [2, 3], 'lg(x) + 6 - x² = 0')

# Уравнение b: x·sin(x) - 1 = 0
f2 = lambda x: x * sin(x) - 1
root2 = plot_and_solve(f2, 0, 4, [1, 2], 'x·sin(x) - 1 = 0')

print(f'Результаты:')
print(f'a) x = {root1:.10f}')
print(f'b) x = {root2:.10f}')
