# Wie führt man Äquivalenzklassenbildung und Grenzwertanalyse an einem Beispiel durch?

Nehmen wir an, wir haben eine Funktion `calculateDiscount(age)` die einen Rabatt basierend auf dem Alter einer Person berechnet:
- Kinder unter 6 Jahren fahren kostenlos.
- Kinder und Jugendliche zwischen 6 und 17 Jahren erhalten 50% Rabatt.
- Erwachsene zwischen 18 und 64 Jahren zahlen den vollen Preis.
- Senioren ab 65 Jahren erhalten 30% Rabatt.

**Äquivalenzklassen** wären:
1. Alter < 6 (kostenlos)
2. Alter >= 6 und <= 17 (50% Rabatt)
3. Alter >= 18 und <= 64 (kein Rabatt)
4. Alter >= 65 (30% Rabatt)

**Grenzwerte** wären:
- Für Klasse 1: 0 (untere Grenze), 5 (obere Grenze)
- Für Klasse 2: 6 (untere Grenze), 17 (obere Grenze)
- Für Klasse 3: 18 (untere Grenze), 64 (obere Grenze)
- Für Klasse 4: 65 (untere Grenze), hypothetischer hoher Wert wie 100 (oberer Grenze)

**Testfälle** könnten sein:
- Testen mit Alter 0, 5 (untere und obere Grenzwerte von Klasse 1)
- Testen mit Alter 6, 17 (untere und obere Grenzwerte von Klasse 2)
- Testen mit Alter 18, 64 (untere und obere Grenzwerte von Klasse 3)
- Testen mit Alter 65, 100 (untere und obere Grenzwerte von Klasse 4)
- Zusätzlich könnte man Werte knapp außerhalb der Grenzen testen, also 5,99 oder 6,01 für die Übergänge zwischen den Klassen.

---

Lernziel 54 \[4/4\]: Black-Box-Tests: Äquivalenzklassenbildung und Grenzwertanalyse erläutern und für ein Beispiel durchführen können
