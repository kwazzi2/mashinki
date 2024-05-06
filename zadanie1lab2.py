import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Электрическая активность сетчатки (независимая переменная)
x = np.array([0, 38.5, 59, 97.4, 119.2, 129.5, 198.7, 248.7, 318, 438.5])

# Проницаемость сосудов сетчатки (зависимая переменная)
y = np.array([19.5, 15, 13.5, 23.3, 6.3, 2.5, 13, 1.8, 6.5, 1.8])

def analys(x,y):
    # Корреляционный анализ
    correlation_coefficient, p_value = stats.pearsonr(x, y)
    print("Коэффициент корреляции:", correlation_coefficient)
    print("p-значение:", p_value)

    # Регрессионный анализ
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    print("Уравнение регрессии: y =", slope, "* x +", intercept)
    print("Коэффициент детерминации (r-квадрат):", r_value**2)

    # Построение графика зависимости и линии регрессии
    plt.scatter(x, y)
    plt.plot(x, slope * x + intercept, color='red')
    plt.xlabel("Электрическая активность сетчатки")
    plt.ylabel("Проницаемость сосудов сетчатки")
    plt.title("Зависимость проницаемости сосудов сетчатки \n от электрической активности")
    plt.grid(True)
    plt.show()

analys(x,y)