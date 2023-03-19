import numpy as np
import matplotlib.pyplot as plt

#Przykładowy zestaw danych (8 punktów na osi XY)
x = [-2, -1, 1, 3, 4, 5, 7, 11]
y = [9, 4, 0, 4, 9, 16, 20, 5]

#Funkcja realizująca obliczanie wielomianu interpolacyjnego Logrange'a,
#przyjmuje ona następujące parametry:
#- x: jako tablicę z punktami x
#- y: jako tablicę z punktami y
#- X: jako punkt X dla którego obliczona ma zostać wartość y
def interp(x,y,X):
    n = len(x) #wielkość tablicy z punktami na osi x
    Wx = 0 #wynik z obliczoną wartością y dla punktu X
    for i in range(n):
        temp = 1
        for j in range (n):
            if(j != i):
                temp *= (X-x[j]) / (x[i]-x[j])
        Wx += y[i]*temp

    return Wx

#Tworzenie dodatkowych równomiernie rozmieszczonych punktów pomiędzy pierwszym i ostatnim elementem na osi x
x_interp = np.linspace(min(x), max(x), 1000)
#Obliczane wartości y dla każdego punktu z tablicy x_interp
y_interp = [interp(x, y, X) for X in x_interp]

#Rysowanie wykresu
plt.plot(x, y, 'ro', label="Punkty interpolacji")
plt.plot(x_interp, y_interp, label="Wielomian interpolacyjny Logrange'a")
plt.xlabel('x')
plt.ylabel('y')
plt.title("MN-LAB1: Interpolacja wielomianowa Lagrange'a")
plt.legend()
plt.show()