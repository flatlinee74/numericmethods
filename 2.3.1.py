import numpy as np
import matplotlib.pyplot as plt

# f(x) = 2 - 0.5x, f'(x) = -0.5 (удовлетворяет -1 < f'(x) < 0)
f = lambda x: 2 - 0.5 * x

x = np.linspace(0, 3, 100)
y = f(x)

plt.figure(figsize=(10, 5))

# График
plt.subplot(1, 2, 1)
plt.plot(x, y, 'b-', linewidth=2, label='y = f(x)')
plt.plot(x, x, 'k--', label='y = x', alpha=0.5)

# Точка пересечения
x_root = 4/3
plt.plot(x_root, x_root, 'ro', markersize=8, label=f'x* = {x_root:.3f}')

# Итерации
x0 = 0.5
x_current = x0
x_points, y_points = [x0], [0]

for i in range(5):
    y_new = f(x_current)
    x_points.extend([x_current, x_current])
    y_points.extend([y_new, y_new])
    x_current = y_new

plt.plot(x_points, y_points, 'r-o', alpha=0.6, label='Итерации')
plt.grid(True, alpha=0.3)
plt.title('Сходящийся процесс (-1 < f\'(x) < 0)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, y, 'b-', linewidth=2)
plt.plot(x, x, 'k--', alpha=0.5)
plt.plot(x_root, x_root, 'ro', markersize=8)
plt.plot(x_points[:6], y_points[:6], 'r-o', alpha=0.6)
plt.xlim([0, 2])
plt.ylim([0, 2])
plt.grid(True, alpha=0.3)
plt.title('Увеличенный вид')
plt.xlabel('x')
plt.ylabel('y')

plt.tight_layout()
plt.show()

print('График построен. Итерации сходятся к x* = 1.333')