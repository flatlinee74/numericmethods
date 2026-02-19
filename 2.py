import math
import matplotlib.pyplot as plt
import numpy as np

print("=" * 60)
print("ПРАКТИЧЕСКАЯ РАБОТА №2: Метод половинного деления")
print("Уравнение: 2lg(x+7) - 5sin x = 0")
print("=" * 60)

# ============================================================
# 1. ТАБЛИЦА ТОЧЕК ДЛЯ ГРАФИКА
# ============================================================

print("\n--- ТАБЛИЦА ЗНАЧЕНИЙ ДЛЯ ПОСТРОЕНИЯ ГРАФИКА ---")
print("x    | y₁ = 2lg(x+7) | y₂ = 5sin x")
print("-" * 40)

x_points = [-2, -1, 0, 1, 2]
y1_points = []
y2_points = []

for x in x_points:
    y1 = 2 * math.log10(x + 7)
    y2 = 5 * math.sin(x)
    y1_points.append(y1)
    y2_points.append(y2)
    print(f"{x:2d}   |     {y1:.3f}      |    {y2:.3f}")

print(f"\nВ точке x = 0: y₁ = {y1_points[2]:.2f}, y₂ = {y2_points[2]:.2f} → y₁ > y₂")
print(f"В точке x = 1: y₁ = {y1_points[3]:.2f}, y₂ = {y2_points[3]:.2f} → y₁ < y₂")
print("⇒ Корень находится на отрезке [0; 1]")

# ============================================================
# 2. СТРОИМ ГРАФИК
# ============================================================

# Создаём кривые для графика
x_smooth = np.linspace(-2, 2, 300)
y1_smooth = 2 * np.log10(x_smooth + 7)
y2_smooth = 5 * np.sin(x_smooth)

plt.figure(figsize=(10, 6))

# Рисуем плавные кривые
plt.plot(x_smooth, y1_smooth, 'b-', linewidth=2, label='y₁ = 2lg(x+7)')
plt.plot(x_smooth, y2_smooth, 'r-', linewidth=2, label='y₂ = 5sin x')

# Отмечаем точки из таблицы
plt.plot(x_points, y1_points, 'bo', markersize=8)
plt.plot(x_points, y2_points, 'ro', markersize=8)

# Подписываем точки
for i in range(len(x_points)):
    plt.text(x_points[i], y1_points[i] + 0.3, f'{y1_points[i]:.2f}', 
             ha='center', fontsize=9, color='blue')
    plt.text(x_points[i], y2_points[i] + 0.3, f'{y2_points[i]:.2f}', 
             ha='center', fontsize=9, color='red')

# Оформление
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Отделение корней: y₁ = 2lg(x+7) и y₂ = 5sin x')
plt.legend()
plt.xlim(-2.2, 2.2)
plt.ylim(-6, 6)
plt.tight_layout()
plt.show()

# ============================================================
# 3. МЕТОД ПОЛОВИННОГО ДЕЛЕНИЯ
# ============================================================

print("\n--- МЕТОД ПОЛОВИННОГО ДЕЛЕНИЯ ---")
print("f(x) = 2lg(x+7) - 5sin x")
print(f"Точность ε = 0.001")
print("\nТаблица итераций:")
print("  n |    a    |    b    |    c    |   f(c)  | f(a) | f(b)")
print("-" * 55)

a, b = 0, 1
n = 0

while (b - a) / 2 > 0.001:
    c = (a + b) / 2
    fc = 2 * math.log10(c + 7) - 5 * math.sin(c)
    fa = 2 * math.log10(a + 7) - 5 * math.sin(a)
    fb = 2 * math.log10(b + 7) - 5 * math.sin(b)
    
    fa_sign = '+' if fa > 0 else '-'
    fb_sign = '+' if fb > 0 else '-'
    
    print(f"{n:3d} | {a:.4f} | {b:.4f} | {c:.4f} | {fc:7.4f} |  {fa_sign}  |  {fb_sign}")
    
    if fa * fc < 0:
        b = c
    else:
        a = c
    n += 1

# Последняя итерация
c = (a + b) / 2
fc = 2 * math.log10(c + 7) - 5 * math.sin(c)
fa = 2 * math.log10(a + 7) - 5 * math.sin(a)
fb = 2 * math.log10(b + 7) - 5 * math.sin(b)
fa_sign = '+' if fa > 0 else '-'
fb_sign = '+' if fb > 0 else '-'
print(f"{n:3d} | {a:.4f} | {b:.4f} | {c:.4f} | {fc:7.4f} |  {fa_sign}  |  {fb_sign}")

root = (a + b) / 2
print(f"\nКорень уравнения: x = {root:.4f}")
print(f"Количество итераций: {n}")

print(f"Длина последнего отрезка: {b - a:.4f}")
