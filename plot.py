import numpy as np
import matplotlib.pyplot as mplt #визуализация данных
x=np.arange (1,25,1) #точки для функции
y= x**4-5*x**2+3 #функция для графика
mplt.plot(x,y, color='red',marker='*',markersize='6') #создание графика по упорядоченным парам,задем цвет и размер
mplt.show() #вывод графикаimport numpy as np