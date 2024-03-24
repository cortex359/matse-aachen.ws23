# Was ist der Unterschied zwischen zentraler und verteilter Versionsverwaltung?

**Unterschied zwischen zentraler und verteilter Versionsverwaltung**

**Zentrale Versionsverwaltung:**
- Es gibt einen **zentralen Server**, der das Repository hält.
- Nutzer **checken** Dateien aus diesem zentralen Repository aus und **committen** Änderungen direkt darauf zurück.
- Ohne Verbindung zum zentralen Server können keine neuen Commits gemacht werden. Nur die Arbeitskopie ist lokal verfügbar.
- Beispiele: **Subversion (SVN)**, **Concurrent Versions System (CVS)**.

**Verteilte Versionsverwaltung:**
- Jeder Entwickler besitzt eine **lokale Kopie** des Repositories, inklusive der gesamten Historie.
- Änderungen werden lokal committet und können später mit dem Repository anderer Nutzer synchronisiert werden.
- Man kann unabhängig vom Netzwerkstatus arbeiten und muss nur zum Synchronisieren eine Verbindung herstellen.
- Bessere Unterstützung für [Branching](014%20Was%20bedeutet%20Branching%20im%20Kontext%20der%20Softwareentwicklung?.md) und [Merging](015%20Was%20sind%20die%20Herausforderungen%20beim%20Merging%20in%20der%20Softwareentwicklung?.md).
- Beispiele: **Git**, **Mercurial**.

---

Lernziel 17 \[2/2\]: Ziele der Versionsverwaltung nennen, Unterschied zentrale & verteilte Versionsverwaltung erläutern können
