import numpy as np


def dataset_minmax(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])
    return minmax



def featureNormalize(dataset):
    """
        Функция позволяет вычислить нормализованную версию матрицы 
        объекты-признаки X со средним значением для каждого признака 
        равным 0 и среднеквадратическим отклонением равным 1
    """
    
    X_norm = dataset
    mu = np.zeros(dataset.shape[1])
    sigma = np.zeros(dataset.shape[1])
    
    # ====================== Ваш код здесь ======================
    # Инструкция: во-первых, необходимо вычислить среднзначение
    #     # каее ждого признака и вычесть его из значений соответствующих
    # признаков в матрице X. Сохранить вектор средних в переменную mu.
    # Во-вторых, необходимо вычислить среднеквадратическое отклонение 
    # для каждого признака и разделить на него соответствующий признак 
    # с учетом нормализации на среднее значение. Сохранить вектор 
    # среднеквадратических отклонений в переменную sigma. Необходимо 
    # отметить, что X является матрицей, в которой каждый столбец 
    # является свойством, а каждая строка - объектом. Нормализацию 
    # требуется выполнить раздельно для каждого свойства
    
    for row in X_norm:
        for i in range(len(row)):
            row[i] = (row[i] - dataset_minmax[i][0]) / (dataset_minmax[i][1] - dataset_minmax[i][0])
    
    # ============================================================
    
    return X_norm, mu, sigma