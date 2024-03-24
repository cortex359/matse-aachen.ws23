# Was ist der Lebenszyklus von Dateien in Git?

Der **Lebenszyklus von Dateien in Git** kann folgendermaßen beschrieben werden:

1. **Untracked**: Die Datei ist neu im Verzeichnis und wurde noch nicht von Git erfasst. Sie existiert ausschließlich im Arbeitsverzeichnis.

2. **Staged**: Die Datei wurde zum Staging-Bereich hinzugefügt, indem der Befehl `git add` verwendet wurde. Sie ist nun für den nächsten Commit vorgemerkt.

3. **Committed**: Nachdem die Datei gestaged wurde, kann sie mit `git commit` in die lokale Repository-Historie übernommen werden. Die Änderungen an der Datei sind nun im lokalen Repository gesichert.

4. **Modified**: Hat die Datei nach einem Commit Änderungen erfahren, gilt sie als modifiziert. Sie befindet sich wieder im Arbeitsverzeichnis mit Änderungen, die noch nicht gestaged oder committed wurden.

Diese Schritte wiederholen sich im Entwicklungsprozess. Dateien können zwischen diesen Zuständen hin- und herwechseln, je nachdem, wie mit ihnen gearbeitet wird. Es ist auch möglich, Änderungen zu verwerfen oder zurückzusetzen, um Dateien auf einen früheren Zustand zurückzubringen.

---

Lernziel 65 \[1/1\]: Lebenszyklus von Dateien in Git kennen
