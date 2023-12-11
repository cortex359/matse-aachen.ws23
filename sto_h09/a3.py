#!/usr/bin/env python3

import numpy as np
import scipy.stats as stats

# Messwerte
messwerte = np.array([980, 1340, 610, 750, 880, 1250, 2410, 1100, 470, 1040, 910, 1860, 730, 820])

### Teil a)

# Mittelwert und Standardabweichung
mittelwert = np.mean(messwerte)
standardabweichung = np.std(messwerte, ddof=1) # Bessel's correction
n = len(messwerte)

# Konfidenzintervall zum Niveau 0.95
alpha = 0.05
freiheitsgrade = n - 1
t_kritisch = stats.t.ppf(1 - alpha/2, freiheitsgrade)

# Berechnung des Konfidenzintervalls
fehler_margin = t_kritisch * (standardabweichung / np.sqrt(n))
konfidenzintervall = (mittelwert - fehler_margin, mittelwert + fehler_margin)

print(mittelwert, standardabweichung, t_kritisch, konfidenzintervall)

### Teil b)
# Zielintervall-Länge
ziel_laenge = 500

# Auflösen der Gleichung nach t_kritisch
t_benötigt = ziel_laenge / (2 * standardabweichung / np.sqrt(n))

# Finden des entsprechenden Konfidenzniveaus
konfidenzniveau_benötigt = 2 * (1 - stats.t.cdf(t_benötigt, freiheitsgrade))

t_benötigt, konfidenzniveau_benötigt
