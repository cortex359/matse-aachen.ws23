# Was sind die Komponenten einer Git-Arbeitsumgebung?

Eine Git-Arbeitsumgebung besteht aus mehreren Schlüsselkomponenten, die es Benutzern ermöglichen, an Projekten zu arbeiten und ihre Änderungen zu verwalten:

1. **Workspace / Arbeitsverzeichnis**: Hier befinden sich die aktuellen Arbeitskopien aller Dateien, an denen ein Entwickler Änderungen vornimmt. Dies ist der Bereich, in dem die Dateien bearbeitet und entwickelt werden.

2. **Index / Staging Area**: Der Index, auch als Staging Area bekannt, ist ein Zwischenbereich, in dem Änderungen vor dem Commit in die lokale Repository-Datenbank gesammelt werden. Änderungen im Workspace werden hier zuerst "gestaged", bevor sie in das Repository übernommen werden.

3. **Lokales Repository**: Dies ist die Datenbank auf dem lokalen Computer des Entwicklers, in der Git die Versionen der Dateien und die Änderungshistorie speichert. Es enthält alle Commits und Zweige, die lokal verfügbar sind.

4. **Remote Repository**: Ein Remote Repository ist eine Version des Projekts, die auf einem Server gehostet wird. Es ermöglicht die Zusammenarbeit mit anderen Entwicklern. Änderungen werden von lokalen Repositories zu Remote Repositories gepusht und von dort gefetcht oder gepullt.

5. **Branches (Zweige)**: In Git können parallel verschiedene Entwicklungslinien gepflegt werden, die als Branches bezeichnet werden. Dadurch können Entwickler an neuen Features oder Bugfixes arbeiten, ohne die Hauptentwicklungslinie (in der Regel der `master` oder `main` Branch) zu beeinträchtigen.

6. **Tags**: Tags sind Referenzen auf bestimmte Punkte in der Git-Historie, meistens verwendet, um bestimmte Versionen, wie Releases, zu markieren.

7. **Git Konfiguration**: Die Konfigurationseinstellungen von Git, einschließlich Benutzeridentifikation und Einstellungen für das Verhalten von Git-Befehlen. Diese Einstellungen können auf drei Ebenen erfolgen: lokal für ein Repository (`.git/config`), global für den Benutzer (`~/.gitconfig` oder `~/.config/git/config`), und systemweit für alle Benutzer auf dem Computer (`/etc/gitconfig`).

8. **Hooks**: Skripte, die zu bestimmten Zeitpunkten im Git-Workflow ausgeführt werden, um benutzerdefinierte Aktionen auszuführen, wie Tests vor dem Commit oder Benachrichtigungen nach einem Push.

Diese Komponenten zusammen bilden die Git-Arbeitsumgebung und bieten die Funktionalität, die Entwickler benötigen, um effizient an Softwareprojekten zu arbeiten und ihre Änderungen zu verwalten.

---

Lernziel 64 \[1/1\]: Komponenten einer Git-Arbeitsumgebung erläutern können
