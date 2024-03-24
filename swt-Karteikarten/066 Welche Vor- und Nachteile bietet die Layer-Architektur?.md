# Welche Vor- und Nachteile bietet die Layer-Architektur?

**Vorteile:**
- **Wartbarkeit**: Durch die klare Trennung von Verantwortlichkeiten ist der Code leichter zu warten.
- **Wiederverwendbarkeit**: Untere Schichten können in verschiedenen Systemen wiederverwendet werden.
- **Austauschbarkeit**: Schichten können unabhängig voneinander ausgetauscht oder modifiziert werden, solange die Schnittstellen erhalten bleiben.

**Nachteile:**
- **Leistung**: Zusätzliche Schichten können die Leistung beeinträchtigen, da Aufrufe durch mehrere Schichten hindurchgehen müssen.
- **Komplexität**: Die Architektur kann durch viele Abstraktionsebenen komplexer und schwieriger zu verstehen werden.
- **Über-Abstraktion**: Zu strikte Schichtenbildung kann Flexibilität einschränken, wenn Funktionen quer über Schichten benötigt werden.

---

Lernziel 37 \[3/4\]: Architekturmuster Layer und Model-View-Controller (MVC) erläutern sowie einige Vor- bzw. Nachteile nennen können
