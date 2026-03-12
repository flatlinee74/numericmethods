import numpy as np
import matplotlib.pyplot as plt

# Создаем 4 разные функции
def create_functions():
    """Создаем 4 функции для демонстрации всех случаев"""
    
    # Случай 1: f' > 0, f'' > 0 
    def f1(x): return np.exp(x) - 2
    def f1_prime(x): return np.exp(x)
    def f1_double(x): return np.exp(x)
    
    # Случай 2: f' > 0, f'' < 0 
    def f2(x): return np.log(x + 2) - 0.5
    def f2_prime(x): return 1 / (x + 2)
    def f2_double(x): return -1 / (x + 2)**2
    
    # Случай 3: f' < 0, f'' > 0 
    def f3(x): return np.exp(-x) - 0.5
    def f3_prime(x): return -np.exp(-x)
    def f3_double(x): return np.exp(-x)
    
    # Случай 4: f' < 0, f'' < 0 
    def f4(x): return -np.log(x + 1) + 0.5
    def f4_prime(x): return -1 / (x + 1)
    def f4_double(x): return 1 / (x + 1)**2
    
    return [
        (f1, f1_prime, f1_double, "f' > 0, f'' > 0", [-1, 1], 0.5),
        (f2, f2_prime, f2_double, "f' > 0, f'' < 0", [-0.5, 1.5], 0.5),
        (f3, f3_prime, f3_double, "f' < 0, f'' > 0", [0, 2], 0.5),
        (f4, f4_prime, f4_double, "f' < 0, f'' < 0", [0, 2], 0.5)
    ]

# Создание фигуры с 4 подграфиками
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
axes = axes.flatten()

functions = create_functions()

for idx, (f, f_prime, f_double, case_name, x_range, x0) in enumerate(functions):
    ax = axes[idx]
    
    # Генерация точек для графика
    x = np.linspace(x_range[0], x_range[1], 400)
    y = f(x)
    
    # Находим интервал [a, b] содержащий корень
    a, b = x_range
    fa, fb = f(a), f(b)
    
    # Построение функции
    ax.plot(x, y, 'b-', linewidth=2.5, label='f(x)')
    ax.axhline(y=0, color='k', linewidth=1, linestyle='--')
    ax.axvline(x=0, color='k', linewidth=0.5, alpha=0.5)
    
    # Точки на концах интервала
    ax.plot([a, b], [fa, fb], 'ro', markersize=10, label='Граничные точки')
    ax.plot([a, b], [fa, fb], 'r--', alpha=0.5)
    
    # === МЕТОД ХОРД ===
    x_chord = a - fa * (b - a) / (fb - fa)
    y_chord = f(x_chord)
    ax.plot([a, b], [fa, fb], 'g-', linewidth=2, label='Метод хорд', alpha=0.7)
    ax.plot(x_chord, y_chord, 'go', markersize=12, label=f'Хорда: {x_chord:.3f}')
    ax.axvline(x=x_chord, color='g', linestyle=':', alpha=0.7)
    
    # === МЕТОД КАСАТЕЛЬНЫХ ===
    # Выбираем точку для касательной (где f и f'' одинакового знака)
    if fa * f_double(a) > 0:
        x_tangent_point = a
    else:
        x_tangent_point = b
    
    f_tan = f(x_tangent_point)
    fp_tan = f_prime(x_tangent_point)
    
    # Касательная линия
    x_tan_line = np.linspace(x_range[0], x_range[1], 100)
    y_tan_line = f_tan + fp_tan * (x_tan_line - x_tangent_point)
    ax.plot(x_tan_line, y_tan_line, 'm-', linewidth=2, label='Метод касательных', alpha=0.7)
    
    # Пересечение касательной с осью X
    x_tangent = x_tangent_point - f_tan / fp_tan
    ax.plot(x_tangent, 0, 'm*', markersize=15, label=f'Касательная: {x_tangent:.3f}')
    ax.axvline(x=x_tangent, color='m', linestyle=':', alpha=0.7)
    
    # Подписи
    ax.set_title(f'Случай {idx+1}: {case_name}', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('f(x)', fontsize=12)
    ax.legend(loc='best', fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(x_range[0] - 0.2, x_range[1] + 0.2)
    
    # Показываем знаки производных
    sign_text = f"f'({x0:.1f}) = {f_prime(x0):+.2f}\nf''({x0:.1f}) = {f_double(x0):+.2f}"
    ax.text(0.02, 0.98, sign_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.suptitle('УПРАЖНЕНИЕ 1: Все 4 случая методов хорд и касательных\n(согласно Рис. 2.9 учебника)', 
             fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()

# === Таблица результатов ===
print("=" * 80)
print("УПРАЖНЕНИЕ 1: ПОЛНОЕ РЕШЕНИЕ ДЛЯ ВСЕХ 4 СЛУЧАЕВ")
print("=" * 80)
print()

for idx, (f, f_prime, f_double, case_name, x_range, x0) in enumerate(functions):
    a, b = x_range
    fa, fb = f(a), f(b)
    
    print(f"СЛУЧАЙ {idx+1}: {case_name}")
    print("-" * 80)
    print(f"Интервал: [{a}, {b}]")
    print(f"f({a}) = {fa:.4f}, f({b}) = {fb:.4f}")
    print(f"f'({x0}) = {f_prime(x0):.4f}, f''({x0}) = {f_double(x0):.4f}")
    print()
    
    # Метод хорд
    x_chord = a - fa * (b - a) / (fb - fa)
    print(f"МЕТОД ХОРД:")
    print(f"  x₁ = {x_chord:.6f}")
    print(f"  f(x₁) = {f(x_chord):.6f}")
    print()
    
    # Метод касательных
    if fa * f_double(a) > 0:
        x_tan_point = a
    else:
        x_tan_point = b
    
    x_tangent = x_tan_point - f(x_tan_point) / f_prime(x_tan_point)
    print(f"МЕТОД КАСАТЕЛЬНЫХ:")
    print(f"  Точка касания: x = {x_tan_point:.1f}")
    print(f"  x₁ = {x_tangent:.6f}")
    print(f"  f(x₁) = {f(x_tangent):.6f}")
    print()
    print("=" * 80)
    print()