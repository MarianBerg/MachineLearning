#Aufgabe: Brustkrebsdetektion mit Support Vector Machines 1
#
#In der sklearn-Bibliothek sind Datensätze enthalten, 
#die durch einen einfachen Import in den Programmcode importiert und 
#anschließend visualisiert und analysiert werden können. 
#
#    -Importiere den Brustkrebsdatensatz mit load_breast_cancer().
#    -Gib die Features und die Labels in der Konsole aus.
#    -Recherchiere, wie du mit sklearn den Datensatz in einen Trainings- und Testdatensatz 
#       aufteilen kannst (80 Prozent Training, 20 Prozent Test).
#    -Trainiere den Support-Vector-Machine-Algorithmus mit einem linearen Kernel.
#    -Teste das Modell mit den Testdaten und bestimme die Accuracy. 



from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import svm

#import the data
cancer_data = datasets.load_breast_cancer()

features = cancer_data.feature_names
labels =   cancer_data.target_names
print("features: {} \n \nlabels: {}".format(features, labels))

features_train, features_test, labels_train, labels_test = train_test_split(cancer_data.data, cancer_data.target, test_size = 0.2, random_state = 217)

svm_model = svm.SVC(kernel= 'linear')

svm_model.fit(features_train, labels_train)

#Test
labels_predict = svm_model.predict(features_test)

accuracy = metrics.accuracy_score(labels_test, labels_predict)

print(accuracy)