from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt

n = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
x = np.array([26, 48, 65, 23, 150, 123, 264, 156, 152, 154, 520, 515])
y = np.array([221, 153, 155, 102, 156, 264, 435, 156, 203, 325, 456, 163])
print("x:", x)
print("y:", y)

x_sum = np.sum(x)
y_sum = np.sum(y)
print("сумма x:", x_sum)
print("сумма y:", y_sum)

xy = x * y
xy_sum = np.sum(xy)
print("x*y:", xy)
print("сумма x*y", xy_sum)

x_squared = x**2
y_squared = y**2
print("x^2:", x_squared)
print("y^2:", y_squared)

x_squared_sum = np.sum(x_squared)
y_squared_sum = np.sum(y_squared)
print("сумма x^2:", x_squared_sum)
print("сумма y^2:", y_squared_sum)

x_mean = np.mean(x)
y_mean = np.mean(y)
print("среднее x:", x_mean)
print("среднее y:", y_mean)

x_diff = x - x_mean
y_diff = y - y_mean
print("xi - x среднее:", x_diff)
print("yi - y среднее:", y_diff)

x_diff_sum = np.sum(x_diff)
y_diff_sum = np.sum(y_diff)
print("сумма xi - x среднее:", x_diff_sum)
print("сумма yi - y среднее:", y_diff_sum)

x_diff_squared = (x - x_mean)**2
y_diff_squared = (y - y_mean)**2
print("(xi - x среднее)^2:", x_diff_squared)
print("(yi - y среднее)^2:", y_diff_squared)

x_diff_squared_sum = np.sum(x_diff_squared)
y_diff_squared_sum = np.sum(y_diff_squared)
print("сумма xi - x среднее:", x_diff_squared_sum)
print("сумма yi - y среднее:", y_diff_squared_sum)

xy_mean = np.mean(xy)
print("x*y среднее:", xy_mean)

x_squared_mean = np.mean(x_squared)
y_squared_mean = np.mean(y_squared)
print("x^2 среднее:", x_squared_mean)
print("y^2 среднее:", y_squared_mean)

Dx = x_squared_mean - (x_mean)**2
Dy = y_squared_mean - (y_mean)**2
print("дисперсия x:", Dx)
print("дисперсия y:", Dy)

b = (xy_mean - x_mean * y_mean)/(Dx)
a = y_mean - b * x_mean

print("Коэффициенты уравнения регрессии:")
print("a =", a)
print("b =", b)

Y = a + b * x

y_diff_Y = y - Y

y_diff_Y_squared = (y - Y)**2
print('(y-Y)^2', y_diff_Y_squared)

plt.scatter(x,y)
plt.plot(x, Y, color = "red")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Точечная диаграмма с линией тренда')
plt.show()

r = (xy_mean - x_mean * y_mean)/(sqrt(Dx) * sqrt(Dy))
print('Линейный коэффициент парной корреляции:', r)

SE = np.sqrt((1 / (12 - 1)) * np.sum(y_diff_Y_squared))
print("Стандартная ошибка остаточной компоненты:", SE)

SE_a = SE * (np.sqrt((x_squared_sum) / (12 * x_diff_squared_sum)))
SE_b = SE**2 / (np.sqrt(x_diff_squared_sum))
print("Стандартная ошибка оценивания коэффициента b:", SE_b)
print("Стандартная ошибка оценивания свободного члена a:", SE_a)

t_a = a / SE_a
t_b = b / SE_b
print('t_a:', t_a)
print('t_b:', t_b)

t_tabl = 2.20

D_a = t_tabl * t_a
D_b = t_tabl * t_b
print('предельная ошибка a:', D_a)
print('предельная ошибка b:', D_b)

alpha = 0.05  # Уровень значимости

#доверительные интервалы
CI_a = (a - D_a, a + D_a)
CI_b = (b - D_b, b + D_b)

print("Доверительный интервал для коэффициента a:", CI_a)
print("Доверительный интервал для коэффициента b:", CI_b)

print('Сравниваем полученное значение t-критерия Стьюдента с критическим при р=0,05 и f = 11 (f=N-1)\n'
      ' (число степеней свободы) значением, указанным в таблице: tтабл = 2,20, можно сказать, что с\n'
      ' вероятностью 95% коэффициент а надёжен, коэффициент b ненадёжен при данном уровне значимости. \n'
      'Так как рассчитанное значение критерия 𝑡𝑎 = 3.91 больше критического, делаем вывод о том, что \n'
      'наблюдаемые различия статистически значимы, коэффициент а надёжен. Значение критерия 𝑡𝑏 = 0.02\n'
      ' меньше табличного, значит различия сравниваемых величин статистически не значимы, коэффициент \n'
      'b ненадёжен при данном уровне значимости.Таким образом, из-за ненадёжности, полученные оценки \n'
      'коэффициента регрессии b не являются эффективными и состоятельными, а само уравнение не может \n'
      'использоваться для моделирования и прогнозирования динамики. Это обусловлено большой ошибкой уравнения регрессии.')