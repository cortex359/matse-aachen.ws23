import numpy as np
from scipy.stats import norm

# Gewichtsklassen und die zugehörigen Häufigkeiten
gewichte = np.array([2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6])
haufigkeiten = np.array([6, 8, 11, 13, 14, 11, 13, 8, 9, 7])

# Berechnung des Mittelwerts
mittelwert = np.sum(gewichte * haufigkeiten) / np.sum(haufigkeiten)

# Berechnung der Standardabweichung
print(np.sum(haufigkeiten * (gewichte)**2))
print(np.sum(haufigkeiten * (mittelwert)**2))
varianz = np.sum(haufigkeiten * (gewichte - mittelwert)**2) / (np.sum(haufigkeiten) - 1)
standardabweichung = np.sqrt(varianz)

print(mittelwert, varianz, standardabweichung)

# Gesamtzahl der beobachteten Mädchen
gesamtzahl = np.sum(haufigkeiten)

# Grenzen der Klassen
klassengrenzen = np.array([-np.inf, 2.8, 3.0, 3.2, 3.4, np.inf])

# Berechnung der Wahrscheinlichkeiten für jede Klasse
p_klassen = norm.cdf(klassengrenzen[1:], mittelwert, standardabweichung) - \
            norm.cdf(klassengrenzen[:-1], mittelwert, standardabweichung)

# Erwartete Häufigkeiten
erwartete_haufigkeiten = gesamtzahl * p_klassen
print(p_klassen)
print(erwartete_haufigkeiten)

# Anpassung der beobachteten Häufigkeiten an die Klassen
beobachtete_haufigkeiten = np.array([haufigkeiten[0] + haufigkeiten[1],
                                     haufigkeiten[2] + haufigkeiten[3],
                                     haufigkeiten[4] + haufigkeiten[5],
                                     haufigkeiten[6] + haufigkeiten[7],
                                     haufigkeiten[8] + haufigkeiten[9]])

print(beobachtete_haufigkeiten)

# Teststatistik D
teststatistik = np.sum((beobachtete_haufigkeiten - erwartete_haufigkeiten) ** 2 / erwartete_haufigkeiten)
print(teststatistik)
