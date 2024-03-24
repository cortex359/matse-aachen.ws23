# Erläutern und führen Sie am Beispiel eines Mehrfachbedingungstests durch.

Beim **Mehrfachbedingungstest** überprüfen wir alle Kombinationen von booleschen Bedingungen. Für das Beispiel würden wir folgende Testfälle benötigen:

**Testfall 1**: Beide Bedingungen sind wahr.
```java
assert addPositive(1, 1) == 2;
```

**Testfall 2**: `a` ist wahr, `b` ist falsch.
```java
assert addPositive(1, 0) == 0;
```

**Testfall 3**: `a` ist falsch, `b` ist wahr.
```java
assert addPositive(0, 1) == 0;
```

**Testfall 4**: Beide Bedingungen sind falsch.
```java
assert addPositive(0, 0) == 0;
```

---

Lernziel 55 \[5/6\]: White-Box-Tests: Anweisungstest, Zweigtest, Bedingungstest, Mehrfachbedingungstest und Grenze-Inneres-Test erläutern und für ein Beispiel durchführen können
