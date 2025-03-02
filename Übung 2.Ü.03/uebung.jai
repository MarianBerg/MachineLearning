/*Aufgabe: Bayes-Theorem

Ein Krankheitstest fällt bei 5 Prozent der Getesteten positiv aus. Es sind aber 1,5 Prozent aller Menschen tatsächlich infiziert. 
Wenn eine Person tatsächlich infiziert ist, fällt der Test zu 97 Prozent positiv aus. 
Schreibe ein Programm, das mit Hilfe des Bayes-Theorems bestimmt, wieviel Prozent der positiven Testergebnisse tatsächlich eine Krankheit bedeuten.
*/

#import "Basic";


//P(Test positiv| Patient infiziert) = 0.97
//P(Patient infiziert) = 0.015
//P(Test positiv) = 0.05
//-> P(Test negativ) = 0.95

//P(Patient infiziert | Test positiv) = ?

//P(Patient infiziert | Test positiv) = P(Test positiv| Patient infiziert) * P(Patient infiziert) / P(Test positiv)


#run print("%\n", 0.97 * 0.015 / 0.05 );