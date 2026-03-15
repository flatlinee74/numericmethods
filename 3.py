import math

print("=" * 60)
print("ПРАКТИЧЕСКАЯ РАБОТА №3: Метод итераций")
print("Уравнение: 2lg(x+7) - 5sin x = 0")
print("=" * 60)

# ОБЩИЕ НАСТРОЙКИ

eps = 0.001  
lam = 0.2    

# Функция
def f(x):
    return 2 * math.log10(x + 7) - 5 * math.sin(x)


# МЕТОД ИТЕРАЦИЙ

print("\n--- МЕТОД ИТЕРАЦИЙ ---")
print(f"λ = {lam}")
print(f"Точность ε = {eps}")
print("\nТаблица итераций:")
print("  n |    x_n    |   f(x_n)  |   x_n+1")
print("-" * 40)

# Начальное приближение (середина отрезка)
x = 0.35
n = 0

while True:
    fx = f(x)
    x_next = x + lam * fx
    
    print(f"{n:3d} | {x:.6f} | {fx:8.6f} | {x_next:.6f}")
    
    if abs(x_next - x) < eps:
        x = x_next
        n += 1
        break
    
    x = x_next
    n += 1

# Последняя итерация
fx = f(x)
x_next = x + lam * fx
print(f"{n:3d} | {x:.6f} | {fx:8.6f} | {x_next:.6f}")

print(f"\nКорень уравнения: x = {x:.4f}")
print(f"Количество итераций: {n}")
