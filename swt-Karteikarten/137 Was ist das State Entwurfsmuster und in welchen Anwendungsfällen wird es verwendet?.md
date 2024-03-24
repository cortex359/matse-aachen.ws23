# Was ist das State Entwurfsmuster und in welchen Anwendungsfällen wird es verwendet?

Das **State** Entwurfsmuster gehört zur Kategorie der Verhaltensmuster und ermöglicht einem Objekt, sein Verhalten zu ändern, wenn sein interner Zustand sich ändert. Das Objekt wird so erscheinen, als hätte es seine Klasse geändert.

**Anwendungsfälle**:
- Wenn das Verhalten eines Objekts aufgrund seines Zustands dynamisch geändert werden muss.
- Wenn komplexe bedingte Operationen mit vielen Verzweigungen vereinfacht werden sollen.

**Ziele**:
- Trennung der zustandsabhängigen Verhaltensweisen in verschiedene Zustandsklassen.
- Reduzierung von bedingten Anweisungen, die das Verhalten abhängig vom Zustand des Objekts steuern.

**Vorteile**:
- Organisiert den Code rund um die verschiedenen Zustände eines Objekts.
- Vereinfacht die Wartung, da Änderungen an den Verhaltensweisen eines Zustands nur in einer Klasse gemacht werden müssen.
- Erleichtert das Hinzufügen neuer Zustände.

**Nachteile**:
- Kann zu einer erhöhten Anzahl von Klassen führen, da für jeden Zustand eine eigene Klasse erstellt wird.
- Die Klassenstruktur kann komplex werden, wenn Zustände hinzugefügt oder geändert werden.

---

Lernziel 66 \[4/5\]: Anwendungsfälle, Ziele und einige Vor- bzw. Nachteile der folgenden Entwurfsmuster erläutern sowie die Schemata auf ein Beispiel anwenden können: Factory Method, Command, Observer, State, Strategy
