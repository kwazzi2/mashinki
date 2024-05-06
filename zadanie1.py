import pandas as pd
import matplotlib.pyplot as plt

# Импортируем датасет
test = "test.csv"
DataSet = pd.read_csv(test, delimiter=',', nrows=1000)

# Настройка вывода
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None) #максимальная ширина столбцов, не будет обрезаться

# Отключаем переносы
pd.options.display.expand_frame_repr = False

print(DataSet)

print("\n\nПроверка на пропуски")
print(pd.isnull(DataSet))

plt.subplot(1, 2, 1)
plt.xlabel('Площадь')
plt.ylabel('Плотность')
plt.title("Гистограмма для площади")
plt.hist(DataSet['Square'], density=True, color='blue', edgecolor='black')

plt.subplot(1, 2, 2)
plt.title("Ящик с усами для площади")
plt.boxplot(DataSet['Square'])
plt.xlabel('Площадь')
plt.show()

print("\n\nпроверка на аномальные значения")
emissions = DataSet[(DataSet.Square < DataSet.LifeSquare)]
print(emissions)

#обработка аномальных значений
DataSet.loc[DataSet['Rooms'] == 0, 'Rooms'] = 1
DataSet.loc[DataSet['Rooms'] > 6, 'Rooms'] = DataSet['Rooms'].median()
DataSet.loc[DataSet['Square'] < DataSet['LifeSquare'], 'LifeSquare'] = DataSet['Square']+15
DataSet.loc[(DataSet['Square'] > 150) | (DataSet['Square'] < 30), 'Square'] = DataSet['Square'].median()
DataSet.loc[(DataSet['LifeSquare'] > 70) | ((DataSet['LifeSquare'] < 30)), 'LifeSquare'] = DataSet['LifeSquare'].median()

#заполнение пропусков
print("\n\nОбработанные данные")
DataSet['LifeSquare'] = DataSet['LifeSquare'].fillna(DataSet['Square'] - 10)
DataSet['Healthcare_1'] = DataSet['Healthcare_1'].fillna(DataSet['Healthcare_1'].mean())
print(DataSet)

#вычисление количества квартир
print("\n\nКоличество разных квартир")
print("Всего 1-комнатных квартир: ", len(DataSet[DataSet['Rooms'] == 1]))
print("Всего 2-комнатных квартир: ", len(DataSet[DataSet['Rooms'] == 2]))
print("Всего 3-комнатных квартир: ", len(DataSet[DataSet['Rooms'] == 3]))
print("Всего 4-комнатных квартир: ", len(DataSet[DataSet['Rooms'] == 4]))
print("Всего 5-комнатных квартир: ", len(DataSet[DataSet['Rooms'] == 5]))
print("Всего 6-комнатных квартир: ", len(DataSet[DataSet['Rooms'] == 6]))

# Построение сводной таблицы
print("Сводная таблица")
table = DataSet.pivot_table('Id', index="DistrictId", columns="Rooms", aggfunc='count', fill_value=0)
print(table)
