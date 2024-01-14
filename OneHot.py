import random
from pandas import DataFrame


def one_hot_encode(df, column):
    # Получаем уникальные значения столбца
    categories = df[column].unique()

    # Создаем для каждого значения столбца новый столбец
    for category in categories:
        df[category] = 0

    # В каждом столбце устанавливаем значение 1 для записи, в которой
    # значение столбца column совпадает с названием столбца
    for i in range(len(df)):
        df.loc[i, df.loc[i, column]] = 1

    # Удаляем исходный столбец
    df.drop(column, axis=1, inplace=True)

    return df


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = DataFrame({'whoAmI': lst})

data = one_hot_encode(data, 'whoAmI')

print(data.head())
