#Aufgabe: Signalübertragung in einem neuronalen Netz
#
#In einem neuronalen Netz wird von einer Schicht zur nächsten das Signal über eine Matrixmultiplikation weitergeleitet. 
#Die Daten an den Knoten der Eingabeschicht werden als Vektor gesehen und die Gewichte zwischen der Eingabe- und der 
#Ausgabeschicht sind in einer Matrix zusammengefasst. 
#Der Eingabevektor wird mit der Gewichtsmatrix multipliziert und das Ergebnis anschließend als Eingabe für die 
#Aktivierungsfunktion verwendet. Schreibe ein Programm, das
#
#    für die Gewichtsmatrix [[0.5,0.32,0.65],[0.755,0.5,0.002],[0.21,0.43,0.03]]
#    den Eingabevektor [1,0,1] und
#    für die Sigmoid-Funktion als Aktivierungsfunktion den Signaltransfer zwischen einer Eingabeschicht mit drei Knoten 
#    und einer Ausgabeschicht mit drei Knoten berechnet. 

import numpy as np
import tensorflow as tf

gewichtsmatrix = np.array([[0.5, 0.32, 0.65], [0.755, 0.5, 0.002], [0.21, 0.43, 0.03]])
eingabevektor = np.array([1, 0, 1])

ausgabevektor = np.dot(gewichtsmatrix, eingabevektor)
print(ausgabevektor)

output = tf.sigmoid(ausgabevektor)
print(output)


