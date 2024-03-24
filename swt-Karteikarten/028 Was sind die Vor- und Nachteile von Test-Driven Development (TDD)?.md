# Was sind die Vor- und Nachteile von Test-Driven Development (TDD)?

**Vorteile von TDD:**
- **Bessere Codequalität**: TDD führt zu einer höheren Testabdeckung und dadurch in der Regel zu Code mit weniger Fehlern.
- **Einfache Test-Automatisierung:** Eine hohe Testabdeckung erlaubt Test-Automatisierung, welche [Continuous Integration](029%20Was%20ist%20Continuous%20Integration?.md) ermöglicht.
- **Eindeutige Definition of Done**: Durch das Schreiben von Tests vor dem Code müssen Entwickler über das gewünschte Verhalten der Software genau nachdenken und klare Anforderungen formulieren.
- **Einfachere Wartung**: Code, der mit TDD entwickelt wurde, ist oft modularer und leichter zu verstehen, was die Wartung vereinfacht.
- **Sichere Refaktorisierung**: Da der Code von Anfang an durch Tests abgedeckt wird, kann er zuverlässiger refactored werden, ohne die Funktionalität zu beeinträchtigen.

**Nachteile von TDD:**
- **Lernkurve**: Es kann schwierig sein, sich an den TDD-Prozess zu gewöhnen und das Vorgehen ist für [Stakeholder](052%20Welche%20sind%20die%20wichtigsten%20Stakeholder%20bei%20der%20Softwareentwicklung?.md) oft zu komplex. 
- **Zeitaufwand**: Das Schreiben von Tests vor dem eigentlichen Code kann den Entwicklungsprozess verlangsamen, besonders in den frühen Phasen.
- Nicht alles ist ausreichend testbar und nicht jeder Test ist automatisierbar.
- Es können nur [funktionale Anforderungen](057%20Was%20ist%20der%20Unterschied%20zwischen%20funktionalen%20und%20nicht-funktionalen%20Anforderungen?.md) getestet werden.
- **Design-Einschränkungen**: TDD kann dazu führen, dass Entwickler sich auf das Schreiben von Code beschränken, der leicht zu testen ist, was möglicherweise nicht immer die beste Designentscheidung ist.
- **Fehler in Tests**: Tests sind auch nur Code, und wenn sie Fehler enthalten, kann dies zu falschen Annahmen über die Codekorrektheit führen.

---

Lernziel 13 \[2/2\]: Test-Driven Development erläutern, Vor- und Nachteile nennen können
