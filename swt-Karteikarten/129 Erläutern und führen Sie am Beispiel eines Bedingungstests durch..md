# Erläutern und führen Sie am Beispiel eines Bedingungstests durch.

Beim **Bedingungstest** fokussieren wir uns auf die Entscheidungsbedingungen innerhalb der Verzweigungen. Für das gleiche Beispiel:

**Testfall 1**: Überprüft, ob `a` positiv ist.
```java
assert addPositive(1, 0) == 0; // `a` erfüllt die Bedingung, `b` nicht.
```

**Testfall 2**: Überprüft, ob `b` positiv ist.
```java
assert addPositive(0, 1) == 0; // `a` erfüllt die Bedingung nicht, `b` schon.
```

---

Lernziel 55 \[4/6\]: White-Box-Tests: Anweisungstest, Zweigtest, Bedingungstest, Mehrfachbedingungstest und Grenze-Inneres-Test erläutern und für ein Beispiel durchführen können
