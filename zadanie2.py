import numpy as np
from matplotlib import pyplot as plt

c = np.arange(-10, 1, 0.5)
x = 12.1
l = ((abs(2 * x - c)) ** 3) ** (1/5) + 0.567

print(f"Значение x = {x}")
for i in range(len(c)):
    print(f"Значение l = {round(l[i], 3)} при с = {c[i]}")

print(f"\nМинимальное значение - {round(l.min(), 3)}")
print(f"Максимальное значение - {round(l.max(), 3)}")
print(f"Среднее значение - {round(l.mean(), 3)}")
print(f"Количество элементов в массиве - {len(l)}")
print(f"Отсортированный массив данных - {sorted(l, reverse = True)}")

plt.plot(l, c, color="blue")
plt.xlim(l[len(l) - 1], l[0])
plt.ylim(c[0], c[len(c) - 1])
plt.grid() #сетка
plt.title("График изменения значений функции", color="black")
plt.xlabel("Функция l(c)")
plt.ylabel("Переменная c")
plt.show()