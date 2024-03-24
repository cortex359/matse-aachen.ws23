# Was ist das Command Entwurfsmuster und in welchen Anwendungsfällen wird es verwendet?

Das **Command** Entwurfsmuster gehört zur Kategorie der Verhaltensmuster und kapselt eine Anfrage als Objekt, wodurch es ermöglicht wird, Clients mit verschiedenen Anfragen zu parametrisieren, Anfragen in Warteschlangen zu stellen oder Operationen rückgängig zu machen.

**Anwendungsfälle**:
- Wenn die Historie von Anfragen aufgezeichnet und rückgängig gemacht werden soll (z.B. Undo in Texteditoren).
- Wenn Anfragen in Warteschlangen und Threads ausgeführt werden sollen.
- Wenn komplexe Kommandos aus einfacheren zusammengesetzt werden sollen.

**Ziele**:
- Trennung zwischen dem Objekt, das eine Operation ausführt, und der Funktionalität, die ausgeführt wird.
- Ermöglichung der Speicherung, Weitergabe und Rücknahme von Befehlen.

**Vorteile**:
- Entkoppelt den Sender des Befehls vom Empfänger, der die Operation ausführt.
- Ermöglicht die Zusammenstellung von Befehlen zu komplexen Sequenzen (Makros).
- Unterstützt die Implementierung von Rückgängig-Operationen (Undo).

**Nachteile**:
- Kann zu einer erhöhten Komplexität führen, wenn viele spezifische Command-Klassen erstellt werden müssen.
- Jedes einzelne Command kann wenig Funktionalität enthalten, was bei einer Großzahl von Commands zu einer Aufblähung des Codes führen kann.

---

Lernziel 66 \[2/5\]: Anwendungsfälle, Ziele und einige Vor- bzw. Nachteile der folgenden Entwurfsmuster erläutern sowie die Schemata auf ein Beispiel anwenden können: Factory Method, Command, Observer, State, Strategy
