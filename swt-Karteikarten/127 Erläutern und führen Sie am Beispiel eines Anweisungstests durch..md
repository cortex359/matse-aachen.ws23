# Erläutern und führen Sie am Beispiel eines Anweisungstests durch.

Ein **Anweisungstest** soll sicherstellen, dass jeder ausführbare Code mindestens einmal durchlaufen wird. Gegeben sei folgende Methode:

```java
public int addPositive(int a, int b) {
    if (a > 0 && b > 0) {
        return a + b;
    }
    return 0;
}
```

Um einen Anweisungstest durchzuführen, müssen wir mindestens zwei Testfälle haben:

**Testfall 1**: Beide Zahlen sind positiv.
```java
assert addPositive(1, 1) == 2; // Testet den positiven Pfad durch die if-Anweisung.
```

**Testfall 2**: Eine der Zahlen ist nicht positiv.
```java
assert addPositive(-1, 1) == 0; // Testet den Pfad, der durch die if-Anweisung nicht ausgeführt wird.
```

---

Lernziel 55 \[2/6\]: White-Box-Tests: Anweisungstest, Zweigtest, Bedingungstest, Mehrfachbedingungstest und Grenze-Inneres-Test erläutern und für ein Beispiel durchführen können
