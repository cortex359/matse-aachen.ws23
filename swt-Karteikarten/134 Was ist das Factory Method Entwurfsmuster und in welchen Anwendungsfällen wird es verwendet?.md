# Was ist das Factory Method Entwurfsmuster und in welchen Anwendungsfällen wird es verwendet?

Das **Factory Method** Entwurfsmuster gehört zur Kategorie der Erzeugungsmuster und dient dazu, die Objekterzeugung von der Nutzung eines Objekts zu trennen, indem die Instanziierung an eine Methode einer Unterklasse delegiert wird. Dies ermöglicht es, dass Klassen in einer Bibliothek oder einem Framework erweitert werden können, ohne die existierende Codebasis zu ändern.

**Anwendungsfälle**:
- Wenn die genaue Typen der zu erstellenden Objekte nicht im Voraus bekannt sind.
- Wenn das System unabhängig von der Objekterzeugung und -komposition bleiben soll.
- Wenn die Erweiterung der Objekterzeugung durch Ableitung von Klassen erforderlich ist.

**Ziele**:
- Bereitstellung einer Schnittstelle für Objekterstellung, während die Unterklassen die konkreten Typen der zu erstellenden Objekte bestimmen.
- Förderung der Lose Kopplung, indem Details der Objekterstellung in Unterklassen verschoben werden.

**Vorteile**:
- Lose Kopplung zwischen Creator-Klasse und konkreten Produktklassen.
- Einfache Erweiterbarkeit des Codes, da neue Produkttypen hinzugefügt werden können, ohne bestehenden Code zu ändern.
- Ermöglicht den Klassen, Unterklassen mit spezifischem Verhalten zu definieren.

**Nachteile**:
- Kann zu einer größeren Anzahl von Klassen im System führen, da für jedes Produkt eine neue Creator-Subklasse benötigt wird.
- Manchmal kann es als Übergeneralisierung wahrgenommen werden, wenn ein einfacherer Ansatz ausreichend wäre.

---

Lernziel 66 \[1/5\]: Anwendungsfälle, Ziele und einige Vor- bzw. Nachteile der folgenden Entwurfsmuster erläutern sowie die Schemata auf ein Beispiel anwenden können: Factory Method, Command, Observer, State, Strategy
