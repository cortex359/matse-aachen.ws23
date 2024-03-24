# Was ist die zyklomatische Komplexität und wie wird sie berechnet?

**Zyklomatische Komplexität** ist ein Maß für die Anzahl der linear unabhängigen Pfade durch den Quellcode. Sie wird verwendet, um die Komplexität eines Programms zu messen. Die Berechnung erfolgt üblicherweise anhand des Kontrollflussgraphen des Programms. Es gibt mehrere Methoden, um die zyklomatische Komplexität V(G) zu berechnen:

- **Kanten, Knoten und Regionen**: \( V(G) = E - N + 2P \), wobei E die Anzahl der Kanten, N die Anzahl der Knoten im Graphen und P die Anzahl der zusammenhängenden Komponenten (in der Regel ist P = 1 für zusammenhängende Programme) ist.
- **Entscheidungspunkte**: \( V(G) = D + 1 \), wobei D die Anzahl der Entscheidungspunkte (wie if, for, while, case, etc.) im Programm ist.
- **Regions**: \( V(G) = R \), wobei R die Anzahl der Regionen im Kontrollflussgraphen ist. Jede Region wird durch einen unabhängigen Zyklus definiert.

Ein Kontrollflussgraph wird gezeichnet, indem jeder eindeutige Pfad durch das Programm als eine Kante und jeder Entscheidungspunkt oder jede Aktion als ein Knoten dargestellt wird. Die zyklomatische Komplexität gibt dann an, wie viele unabhängige Testfälle mindestens nötig sind, um alle Pfade durch das Programm zu testen.

---

Lernziel 52 \[1/2\]: Zyklomatische Komplexität für einen Kontrollflussgraphen berechnen können
