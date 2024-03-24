# Wie berechnet man die zyklomatische Komplexität für den folgenden Kontrollflussgraphen?
```
   +---+         +---+         +---+
-->| A |---+---> | B |---+---> | C |---+
   +---+   |     +---+   |     +---+   |
           |             |             |
           |     +---+   |     +---+   |
           +---->| D |<--+<----| E |<--+
                 +---+         +---+
```

Für den gegebenen Kontrollflussgraphen können wir die zyklomatische Komplexität mit der Formel \( V(G) = E - N + 2P \) berechnen:

- E (Anzahl der Kanten) = 6
- N (Anzahl der Knoten) = 5
- P (Anzahl der zusammenhängenden Komponenten) = 1 (weil der Graph zusammenhängend ist)

Setzen wir diese Werte in die Formel ein, erhalten wir:
\( V(G) = 6 - 5 + 2 * 1 \)
\( V(G) = 6 - 5 + 2 \)
\( V(G) = 3 \)

Die zyklomatische Komplexität des Graphen beträgt 3, was bedeutet, dass mindestens drei Testfälle benötigt werden, um alle möglichen Pfade durch den Code abzudecken.

---

Lernziel 52 \[2/2\]: Zyklomatische Komplexität für einen Kontrollflussgraphen berechnen können
