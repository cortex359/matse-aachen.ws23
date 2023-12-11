#!/usr/bin/env python3

import numpy as np
import scipy.stats as stats

# Messwerte
messwerte = np.array([1, 2, 3, 4, 4, 4, 6, 7, 9, 10])
n = len(messwerte)  # Stichprobengröße

# Berechnung des Mittelwerts und der Stichprobenvarianz
mittelwert = np.mean(messwerte)
stichprobenvarianz = np.var(messwerte, ddof=1)

# Konfidenzniveaus
alpha_80 = 0.20
alpha_95 = 0.05

# Berechnung der Chi-Quadrat-Werte für das 80% Konfidenzintervall
chi2_low_80 = stats.chi2.ppf(alpha_80 / 2, df=n-1)
chi2_high_80 = stats.chi2.ppf(1 - alpha_80 / 2, df=n-1)

# Berechnung des 80% Konfidenzintervalls für die Varianz
ci_low_80 = (n - 1) * stichprobenvarianz / chi2_high_80
ci_high_80 = (n - 1) * stichprobenvarianz / chi2_low_80

# Berechnung des Chi-Quadrat-Wertes für das 95% Konfidenzintervall
chi2_95 = stats.chi2.ppf(alpha_95, df=n-1)

# Berechnung des 95% Konfidenzintervalls für die Varianz (nach oben begrenzt)
ci_95 = (n - 1) * stichprobenvarianz / chi2_95

print(mittelwert, stichprobenvarianz, (ci_low_80, ci_high_80), ci_95)
