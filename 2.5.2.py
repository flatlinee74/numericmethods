# УПРАЖНЕНИЕ 2: Комбинированный метод

def f(x):
    return x**3 + 3*x**2 - 24*x + 1

def f_prime(x):
    return 3*x**2 + 6*x - 24

def f_double(x):
    return 6*x + 6

# Параметры
a, b = 0, 1
eps = 0.000001

print("Уравнение: x^3 + 3x^2 - 24x + 1 = 0")
print("Интервал: [%d; %d], Точность: %s" % (a, b, eps))
print("-" * 70)

# Проверка
print("f(%d) = %d, f(%d) = %d" % (a, f(a), b, f(b)))
print("-" * 70)

# Определяем, где проводить касательную (где f и f'' одного знака)
if f(a) * f_double(a) > 0:
    tangent_side = 'left'   
else:
    tangent_side = 'right'  

print("Касательная проводится в %s точке" % ('левой' if tangent_side == 'left' else 'правой'))
print("-" * 70)

# Итерации
a_curr, b_curr = a, b
n = 0

print("n   | a         | b         | x_хорда    | x_касат    | разность")
print("-" * 90)

while True:
    fa = f(a_curr)
    fb = f(b_curr)
    
    # Метод хорд (соединяем a и б)
    x_chord = a_curr - fa * (b_curr - a_curr) / (fb - fa)
    
    # Метод касательных
    if tangent_side == 'left':
        fp = f_prime(a_curr)
        x_tangent = a_curr - fa / fp
    else:
        fp = f_prime(b_curr)
        x_tangent = b_curr - fb / fp
    
    diff = abs(x_tangent - x_chord)
    
    print("%d   | %.6f   | %.6f   | %.8f   | %.8f   | %.2e" % 
          (n, a_curr, b_curr, x_chord, x_tangent, diff))
    
    if diff < eps:
        break
    
    # Новый интервал: между двумя приближениями
    a_curr = min(x_chord, x_tangent)
    b_curr = max(x_chord, x_tangent)
    
    n += 1
    if n > 20:
        break

print("-" * 90)
result = (x_chord + x_tangent) / 2
print("ОТВЕТ: xi = %.8f" % result)
print("Проверка: f(xi) = %.2e" % f(result))