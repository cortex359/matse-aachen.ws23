#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Daten der Versuchstiere
gewichte = [
    12.16, 11.53, 14.02, 11.85, 10.94, 11.83, 12.94, 11.46, 13.15, 12.70,
    10.88, 13.24, 14.04, 10.95, 14.78, 12.39, 13.69, 11.82, 14.28, 12.96,
    13.24, 13.42, 12.23, 15.04, 11.34, 12.28, 13.42, 13.93, 14.73, 11.28
]

# Klasseneinteilung
klassen_grenzen = [10.0, 11.5, 13.0, 14.0, 16.0]
klassen_namen = ["[10,0;11,5)", "[11,5;13,0)", "[13,0;14,0)", "[14,0;16,0)"]

# Klasseneinteilung und Häufigkeitsberechnung
klassen_haeufigkeit = pd.cut(gewichte, bins=klassen_grenzen, labels=klassen_namen, right=False).value_counts().sort_index()
absolute_haeufigkeit = klassen_haeufigkeit.values
relative_haeufigkeit = klassen_haeufigkeit.values / len(gewichte)

# Empirische Verteilungsfunktion
empirische_verteilung = np.cumsum(relative_haeufigkeit)

# Berechnung der Klassengröße
klassengroessen = np.diff(klassen_grenzen)

# Berechnung der Dichte für jede Klasse
dichte = absolute_haeufigkeit / klassengroessen

# Zusammenstellung der Tabelle
tabelle = pd.DataFrame({
    'Klasse': klassen_namen,
    'Absolute Häufigkeit': absolute_haeufigkeit,
    'Relative Häufigkeit': relative_haeufigkeit,
    'Empirische Verteilungsfunktion': empirische_verteilung,
    'Klassengröße': klassengroessen,
    'Klassendichte': dichte
})

print(tabelle)

# Histogramm
plt.figure(figsize=(10, 6))

# Histogramm mit den Klassengrenzen
plt.bar([10, 11.5, 13, 14], dichte, width=klassengroessen, edgecolor='black', alpha=0.7, align="edge")

plt.title('Histogramm der Gewichte der Versuchstiere')
plt.xlabel('Gewichtsklassen (kg)')
plt.ylabel('Dichte')
plt.xticks(klassen_grenzen)
plt.grid(axis='y', alpha=0.75)

# Zeige das Histogramm
plt.savefig('A2-b.pdf')

# Empirische Verteilungsfunktion
plt.figure(figsize=(10, 6))

# Berechnung der empirischen Verteilungsfunktion
for i in range(len(klassen_grenzen)-1):
    plt.hlines(empirische_verteilung[i], klassen_grenzen[i], klassen_grenzen[i+1], color='blue')
plt.hlines(0, 9, klassen_grenzen[0], color='blue')
plt.hlines(1, 16, 17, color='blue')

plt.title('Empirische Verteilungsfunktion der Gewichte der Versuchstiere')
plt.xlabel('Gewicht (kg)')
plt.ylabel('F(x)')
plt.xticks([9] + klassen_grenzen + [17])
plt.yticks(np.linspace(0, 1, 11))
plt.xlim(9, 16)
plt.grid(axis='both', alpha=0.75)

# Zeige die empirische Verteilungsfunktion
plt.savefig('A2-b2.pdf')