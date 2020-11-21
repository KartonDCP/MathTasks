import numpy as np

def computeCost(X, y, theta):
    """
        Функция позволяет вычислить значение стоимостной функции, 
        используя theta в качестве параметров для линейной регрессии 
        (с одной переменной), матрицу объекты-признаки X и вектор меток y
    """
    
    m = y.shape[0]
    J = 0
    for i in range(0, m):
        inner = np.dot(X[i], theta)
        res = inner - y[i]
        val = res ** 2
        J += np.sum(val)

    # ====================== Ваш код здесь ======================
    # Инструкция: вычислить значение стоимостной функции для заданных
    # theta, X и y. Присвоить полученный результат в J
    
    
    
    # ============================================================
    
    return 1 / (2*m) * J