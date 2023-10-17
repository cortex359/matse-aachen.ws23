#!/usr/bin/env python

### Aufgabe 2
def X(i, j):
    if i == j:
        if (i + j) % 2 == 0:
            return 6
        else:
            return -6
    else:
        if (i + j) % 2 == 0:
            return 3
        else:
            return -3


counter = 0
summe = 0
for i in range(1, 7):
    for j in range(1, 7):
        counter += 1
        summe += X(i, j)


print("Aus {} Spielen wurden {} Euro gewonnen, sodass der Erwartungswert {} beträgt.".format(counter, summe, (summe/counter)))