# Erläutern und führen Sie am Beispiel eines Grenze-Inneres-Tests durch.

Beim **Grenze-Inneres-Test** konzentrieren wir uns auf die Grenzwerte und das Verhalten innerhalb dieser Grenzen. Wenn wir zum Beispiel eine Schleife haben, die von 0 bis 10 läuft, würden wir die Werte bei 0 und 10 sowie Werte dazwischen testen. Nehmen wir als Beispiel eine Methode, die prüft, ob eine Zahl im Bereich von 1 bis 100 liegt:

```java
public boolean isInRange(int number) {
    return number >= 1 && number <= 100;
}
```

**Testfall 1**: Test an der unteren Grenze.
```java
assert isInRange(1) == true;
```

**Testfall 2**: Test knapp unter der unteren Grenze.
```java
assert isInRange(0) == false;
```

**Testfall 3**: Test an der oberen Grenze.
```java
assert isInRange(100) == true;
```

**Testfall 4**: Test knapp über der oberen Grenze.
```java
assert isInRange(101) == false;
```

**Testfall 5**: Test innerhalb der Grenzen.
```java
assert isInRange(50) == true;
```

---

Lernziel 55 \[6/6\]: White-Box-Tests: Anweisungstest, Zweigtest, Bedingungstest, Mehrfachbedingungstest und Grenze-Inneres-Test erläutern und für ein Beispiel durchführen können
