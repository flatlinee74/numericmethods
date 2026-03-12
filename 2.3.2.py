import numpy as np
import matplotlib.pyplot as plt
from math import sin

# Уравнение: x·sin(x) - 1 = 0
# Используем метод простой итерации с релаксацией: x = x - m·F(x)
# где F(x) = x·sin(x) - 1

def F(x):
    return x * sin(x) - 1

# Параметр релаксации (подбираем из условия сходимости)
m = 0.5

# Итерационная функция
phi = lambda x: x - m * F(x)

x0 = 1.0
eps = 1e-4

print('Уравнение: x·sin(x) - 1 = 0')
print('Метод простой итерации с релаксацией')
print(f'x = x - {m}·(x·sin(x) - 1)')
print(f'Начальное приближение: x₀ = {x0}')
print(f'Точность: ε = {eps}\n')

x_current = x0
iterations = [(0, x0, 0)]

for n in range(1, 50):
    x_new = phi(x_current)
    error = abs(x_new - x_current)
    iterations.append((n, x_new, error))
    
    print(f'n={n:2d} | x={x_new:.10f} | |Δx|={error:.2e} | f(x)={F(x_new):.2e}')
    
    if error < eps:
        root = x_new
        print(f'\n✓ Корень найден: x = {root:.10f}')
        print(f'  Итераций: {n}')
        print(f'  Проверка: x·sin(x) - 1 = {F(root):.2e}')
        break
    
    x_current = x_new
else:
    root = x_current
    print(f'\nДостигнуто максимальное число итераций')
    print(f'Последнее приближение: x = {root:.10f}')

# График
x = np.linspace(0.5, 4, 1000)
y1 = x
y2 = [phi(xi) for xi in x]
y_orig = [xi * sin(xi) - 1 for xi in x]

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x, y1, 'k--', label='y = x', alpha=0.5)
plt.plot(x, y2, 'b-', linewidth=2, label=f'y = x - {m}·F(x)')
plt.plot(root, root, 'ro', markersize=10, label=f'x* = {root:.6f}')
plt.grid(True, alpha=0.3)
plt.title('Итерационный процесс')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, y_orig, 'b-', linewidth=2)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.plot(root, F(root), 'ro', markersize=10)
plt.grid(True, alpha=0.3)
plt.title(f'f(x) = x·sin(x) - 1\nКорень: x = {root:.6f}')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.tight_layout()
plt.show()

