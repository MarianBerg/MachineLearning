import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder


data = pd.read_csv("Abo.csv")

label_encoder = LabelEncoder()
features = data[["Erwerbsstatus", "Ausbildungsstand" ,"CQF- Alumni"]]

erwerbstatus_encoder = {'selbststaendig':0, 'angestellt': 1, 'Student': 2 }
features["Erwerbsstatus"] = features["Erwerbsstatus"].map(erwerbstatus_encoder)

ausbildungsstand_encoder = {'Uniabschluss':0, 'Student': 1}
features["Ausbildungsstand"] = features["Ausbildungsstand"].map(ausbildungsstand_encoder)

cqf_encoder = {'nein': 0, 'ja': 1}
features["CQF- Alumni"] = features["CQF- Alumni"].map(cqf_encoder)

labels = data[["Abo"]]
abo_encoder = {'ja': 0, 'nein': 1}
labels_encoded = labels["Abo"].map(abo_encoder)

dtc = DecisionTreeClassifier(random_state=42)

dtc.fit(features, labels_encoded)

print(dtc.predict([[0, 0, 1]]))