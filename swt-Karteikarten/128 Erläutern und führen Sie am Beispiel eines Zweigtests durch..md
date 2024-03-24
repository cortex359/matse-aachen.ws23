# Erläutern und führen Sie am Beispiel eines Zweigtests durch.

Beim **Zweigtest** zielt man darauf ab, alle möglichen Verzweigungen im Code zu durchlaufen. Nehmen wir das gleiche Beispiel wie oben:

Um den Zweigtest durchzuführen, benötigen wir vier Testfälle, um alle möglichen Kombinationen der Verzweigung zu testen:

**Testfall 1**: Beide Zahlen sind positiv.
```java
assert addPositive(1, 1) == 2; // Testet den Pfad, bei dem beide Bedingungen wahr sind.
```

**Testfall 2**: `a` ist nicht positiv, `b` ist positiv.
```java
assert addPositive(-1, 1) == 0; // Testet den Pfad, bei dem die erste Bedingung falsch ist.
```

**Testfall 3**: `a` ist positiv, `b` ist nicht positiv.
```java
assert addPositive(1, -1) == 0; // Testet den Pfad, bei dem die zweite Bedingung falsch ist.
```

**Testfall 4**: Beide Zahlen sind nicht positiv.
```java
assert addPositive(-1, -1) == 0; // Testet den Pfad, bei dem beide Bedingungen falsch sind.
```

---

Lernziel 55 \[3/6\]: White-Box-Tests: Anweisungstest, Zweigtest, Bedingungstest, Mehrfachbedingungstest und Grenze-Inneres-Test erläutern und für ein Beispiel durchführen können
