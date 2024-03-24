# Was ist ein Kontrollflussgraph und wie erstellt man ihn?

Ein **Kontrollflussgraph (CFG)** ist eine graphische Darstellung der möglichen Pfade, die während der Ausführung eines Programms durchlaufen werden können. Er ermöglicht es, die logische Flusskontrolle der Programmausführung visuell zu untersuchen und wird oft in der Softwareentwicklung verwendet, um die Komplexität von Code zu analysieren und Testfälle zu erstellen.

So erstellen Sie einen Kontrollflussgraphen:

1. **Identifizieren Sie die Knoten**: Jede Anweisung und Entscheidungspunkt im Code wird als separater Knoten im Graphen dargestellt.
2. **Identifizieren Sie die Kanten**: Die Pfeile, die die Knoten verbinden, repräsentieren die möglichen Wege, die bei der Ausführung des Codes genommen werden können. 
3. **Berücksichtigen Sie die Entscheidungspunkte**: Verzweigungen im Code (z.B. if-Statements, Schleifen) führen zu Knoten, von denen mehrere Kanten ausgehen können.
4. **Berücksichtigen Sie den Einstiegspunkt**: Der Startpunkt des Graphen ist der Eingang in die Methode oder das Programm.
5. **Berücksichtigen Sie den Ausstiegspunkt**: Der Endpunkt des Graphen ist der Ausgang aus der Methode oder das Ende des Programms.

Hier ein Beispiel für einen einfachen Code und dessen Kontrollflussgraph:

```java
1. if (a > b) {
2.     a = a + b;
3. } else {
4.     b = a - b;
5. }
6. print(a);
```

**Kontrollflussgraph:**

```
   +---+
   | 1 |
   +---+
    / \
   /   \
 +---+ +---+
 | 2 | | 4 |
 +---+ +---+
   \   /
    \ /
   +---+
   | 6 |
   +---+
```

In diesem Graphen:
- Knoten 1 repräsentiert die `if`-Bedingung.
- Knoten 2 repräsentiert die Anweisung `a = a + b;`.
- Knoten 4 repräsentiert die Anweisung `b = a - b;`.
- Knoten 6 repräsentiert die `print(a);` Anweisung.

Die Kanten zeigen den Fluss von einer Anweisung zur nächsten basierend auf den Bedingungen des Codes.

---

Lernziel 51 \[1/1\]: Kontrollflussgraph für gegebenen Code erstellen können
