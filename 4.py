import math

print("=" * 60)
print("ПРАКТИЧЕСКАЯ РАБОТА №4: Метод хорд и метод касательных")
print("Уравнение: 2lg(x+7) - 5sin x = 0")
print("=" * 60)

# ============================================================
# ОБЩИЕ ФУНКЦИИ
# ============================================================

ln10 = math.log(10)
eps = 0.001

def f(x):
    return 2 * math.log10(x + 7) - 5 * math.sin(x)

def f_derivative(x):
    return 2 / ((x + 7) * ln10) - 5 * math.cos(x)

def f_derivative2(x):
    return -2 / ((x + 7)**2 * ln10) + 5 * math.sin(x)

# ============================================================
# 1. МЕТОД ХОРД
# ============================================================

print("\n" + "=" * 60)
print("МЕТОД ХОРД")
print("=" * 60)

# Отрезок вокруг корня
a, b = 0.3, 0.4

print(f"\nОтрезок: [{a}; {b}]")
print(f"f({a}) = {f(a):.4f}")
print(f"f({b}) = {f(b):.4f}")
print(f"f''({a}) = {f_derivative2(a):.4f}")
print(f"f''({b}) = {f_derivative2(b):.4f}")

# Выбираем неподвижный конец
if f(a) * f_derivative2(a) > 0:
    c = a
    x0 = b
    print(f"\nВыбираем c = {a} (неподвижный), x0 = {b} (начальное)")
else:
    c = b
    x0 = a
    print(f"\nВыбираем c = {b} (неподвижный), x0 = {a} (начальное)")

fc = f(c)
x_prev = x0

print("\nТаблица итераций (метод хорд):")
print("  n |    x_n    |   f(x_n)  |   x_n+1")
print("-" * 40)

for n in range(10):
    fx = f(x_prev)
    x_next = (c * fx - x_prev * fc) / (fx - fc)
    
    print(f"{n:3d} | {x_prev:.6f} | {fx:8.6f} | {x_next:.6f}")
    
    if abs(x_next - x_prev) < eps:
        root_chord = x_next
        iterations_chord = n + 1
        break
    x_prev = x_next

print(f"\nКорень (метод хорд): x = {root_chord:.4f}")
print(f"Количество итераций: {iterations_chord}")

# ============================================================
# 2. МЕТОД КАСАТЕЛЬНЫХ (НЬЮТОНА)
# ============================================================

print("\n" + "=" * 60)
print("МЕТОД КАСАТЕЛЬНЫХ (Ньютона)")
print("=" * 60)

# Выбираем начальное приближение
x0 = 0.3  # f(0.3) > 0 и f''(0.3) > 0
print(f"\nНачальное приближение x0 = {x0}")
print(f"(f(x0) = {f(x0):.4f} > 0, f''(x0) = {f_derivative2(x0):.4f} > 0)")

# Оцениваем минимум производной для проверки точности
min_derivative = 4.5  # примерно min|f'(x)| на отрезке

print("\nТаблица итераций (метод касательных):")
print("  n |    x_n    |   f(x_n)  |   f'(x_n)  |   x_n+1   | |f(x_n)|/min|f'|")
print("-" * 70)

x = x0

for n in range(10):
    fx = f(x)
    fder = f_derivative(x)
    x_next = x - fx / fder
    
    error = abs(fx) / min_derivative
    
    print(f"{n:3d} | {x:.6f} | {fx:8.6f} | {fder:9.6f} | {x_next:.6f} |   {error:.6f}")
    
    if error < eps:
        root_tangent = x_next
        iterations_tangent = n + 1
        break
    x = x_next

print(f"\nКорень (метод касательных): x = {root_tangent:.4f}")
print(f"Количество итераций: {iterations_tangent}")

# ============================================================
# ИТОГ
# ============================================================

print("\n" + "=" * 60)
print("ИТОГОВЫЕ РЕЗУЛЬТАТЫ")
print("=" * 60)
print(f"Метод хорд:        x = {root_chord:.4f} (за {iterations_chord} итераций)")
print(f"Метод касательных: x = {root_tangent:.4f} (за {iterations_tangent} итераций)")
print("-" * 60)
print(f"КОРЕНЬ УРАВНЕНИЯ: x ≈ 0.3537")
print("=" * 60)