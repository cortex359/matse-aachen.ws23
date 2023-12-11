#!/usr/bin/env python3

import numpy as np
import scipy.stats as stats

# Gegebene Daten
data = np.array([124, 145, 112, 124, 136, 129, 125, 131, 142, 114])
n = len(data)  # Stichprobengröße

# Berechnung des Mittelwerts und der Standardabweichung der Stichprobe
mean = np.mean(data)
std = np.std(data, ddof=1)

# Konfidenzniveau
alpha = 0.10  # 1 - 90%

# 1. Einseitiges Konfidenzintervall für μ
# t-Wert für das 90%-Konfidenzniveau und n-1 Freiheitsgrade
t_value = stats.t.ppf(1 - alpha, df=n-1)
print(t_value)

# Konfidenzintervall für μ
ci_mu_lower = mean - t_value * std / np.sqrt(n)
ci_mu_upper = np.inf

# 2. Zweiseitiges Konfidenzintervall für σ
# Chi-Quadrat-Werte für das 90%-Konfidenzniveau
chi2_lower = stats.chi2.ppf(alpha / 2, df=n-1)
chi2_upper = stats.chi2.ppf(1 - alpha / 2, df=n-1)
# Konfidenzintervall für σ
ci_sigma_lower = np.sqrt((n - 1) * std**2 / chi2_upper)
ci_sigma_upper = np.sqrt((n - 1) * std**2 / chi2_lower)

print(mean, std, (ci_mu_lower, ci_mu_upper), (ci_sigma_lower, ci_sigma_upper))
