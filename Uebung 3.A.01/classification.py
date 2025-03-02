#Aufgabe: KNN mit Trainings- und Testdaten 
#
#Teile nun die Daten aus der vorherigen Aufgabe in Trainings- und Testdaten auf. 
#Dabei sollen die ersten 80 Prozent der Daten die Trainingsdaten und die letzten 20 Prozent die Testdaten sein. 
#Nachdem du das KNN-Modell mit den Trainingsdaten trainiert hast, testest du das Modell für die Testdaten und berechnest die Accuracy.  
# 
#	
#
#Die Accuracy lässt sich am einfachsten über die Konfusionsmatrix bestimmen. Dafür gibt es eine Funktion in sklearn.metrics. 



import pandas as pd


def main():
    data = pd.read_csv("Gehaltsklassen_prepared.csv")

    feature = list(zip(data["Berufserfahrung"], data["Bildungsgrad"]))

    label = list(data["gehalt_over_50k"])

    from sklearn.model_selection import train_test_split
    feature_train, feature_test, label_train, label_test = train_test_split(feature, label, test_size = 0.2, shuffle = False)

    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors = 5)
    knn.fit(feature_train, label_train)

    label_predict = knn.predict(feature_test)

    from sklearn.metrics import confusion_matrix 
    cm = confusion_matrix(label_test, label_predict)

    print(cm)
    




if __name__ == "__main__":
    main()

#Accuracy = TP / (TP+FP)
#         = 0 / (0 + 5)
#         = 0
# Leider eine Accuracy von 0, ist aber anhand der recht kleinen Datenmenge wahrscheinlich nicht representativ.