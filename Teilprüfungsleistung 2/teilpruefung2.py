#Aufgabe: Sigmoid-Funktion
#Schreibe ein Programm, das die Sigmoid-Funktion der logistischen Regression als Plot visualisiert. 
#Achte darauf, das Intervall der Werte auf der x-Achse entsprechend zu wählen. 


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 200)

y = tf.sigmoid(x)



plt.plot(x, y)

plt.show()