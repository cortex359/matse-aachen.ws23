# Was ist das Observer Entwurfsmuster und in welchen Anwendungsfällen wird es verwendet?

Das **Observer** Entwurfsmuster gehört zur Kategorie der Verhaltensmuster und definiert eine ein-zu-viele-Abhängigkeit zwischen Objekten, sodass wenn ein Objekt seinen Zustand ändert, alle seine abhängigen Benachrichtigt werden und automatisch aktualisiert werden.

**Anwendungsfälle**:
- Wenn Änderungen an einem Objekt automatisch eine Reihe von abhängigen Objekten aktualisieren müssen.
- Wenn die Kopplung zwischen dem Kernobjekt und den abhängigen Objekten lose gehalten werden soll.

**Ziele**:
- Aufrechterhaltung der Konsistenz zwischen zusammenarbeitenden Klassen, ohne sie eng zu koppeln.
- Unterstützung für Broadcast-Kommunikation, wobei ein Änderungsnachricht an mehrere Empfänger gesendet wird.

**Vorteile**:
- Lose Kopplung zwischen dem Subjekt (das Objekt, das überwacht wird) und den Beobachtern (die auf Änderungen reagieren).
- Ermöglicht die dynamische Zu- und Abmeldung von Beobachtern.
- Förderung von Wiederverwendung und Erweiterbarkeit.

**Nachteile**:
- Kann schwierig sein, die Abhängigkeiten zu verfolgen, wenn viele Objekte beteiligt sind.
- Wenn Beobachter nicht richtig entfernt werden, können Speicherlecks entstehen (dangling references).
- Benachrichtigungen können sich überlappen und so zu unerwartetem Verhalten führen.

---

Lernziel 66 \[3/5\]: Anwendungsfälle, Ziele und einige Vor- bzw. Nachteile der folgenden Entwurfsmuster erläutern sowie die Schemata auf ein Beispiel anwenden können: Factory Method, Command, Observer, State, Strategy
