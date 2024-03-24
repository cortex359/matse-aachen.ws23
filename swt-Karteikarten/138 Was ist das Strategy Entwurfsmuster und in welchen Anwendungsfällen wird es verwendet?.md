# Was ist das Strategy Entwurfsmuster und in welchen Anwendungsfällen wird es verwendet?

Das **Strategy** Entwurfsmuster gehört zur Kategorie der Verhaltensmuster und definiert eine Familie von Algorithmen, kapselt jeden einzelnen davon und macht sie austauschbar. Strategy ermöglicht es dem Algorithmus, unabhängig vom nutzenden Client zu variieren.

**Anwendungsfälle**:
- Wenn verschiedene Varianten eines Algorithmus benötigt werden.
- Wenn ein Objekt verschiedene Verhaltensweisen aufweisen soll, die zur Laufzeit ausgewählt werden können.
- Wenn viele bedingte Anweisungen in mehreren Funktionen die verschiedenen Varianten eines Algorithmus steuern.

**Ziele**:
- Definition einer Familie von Algorithmen.
- Kapselung jedes Algorithmus in einer eigenen Klasse, mit einer gemeinsamen Schnittstelle.
- Austauschbarkeit der Algorithmen innerhalb des Objekts.

**Vorteile**:
- Isolierung der Implementierungsdetails der Algorithmen vom Code, der sie nutzt.
- Erleichterung des Austauschs von Algorithmen zur Laufzeit.
- Förderung der Wiederverwendbarkeit von Code und der Prinzipien von offen/geschlossen (open/closed principles).

**Nachteile**:
- Kann zu einer Vielzahl von Strategy-Klassen führen, was die Komplexität erhöht.
- Klienten müssen die verschiedenen Strategien kennen, um die richtige Auswahl treffen zu können.
- Zusätzlicher Aufwand für die Kommunikation zwischen Strategie und Kontext, wenn sie Daten austauschen müssen.

---

Lernziel 66 \[5/5\]: Anwendungsfälle, Ziele und einige Vor- bzw. Nachteile der folgenden Entwurfsmuster erläutern sowie die Schemata auf ein Beispiel anwenden können: Factory Method, Command, Observer, State, Strategy
