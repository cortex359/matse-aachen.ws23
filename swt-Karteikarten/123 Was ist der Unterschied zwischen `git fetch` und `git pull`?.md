# Was ist der Unterschied zwischen `git fetch` und `git pull`?

`git pull` ist eine Kombination aus `git fetch` und `git merge`. Es holt die neuesten Informationen vom entfernten Repository und führt diese Änderungen mit dem aktuellen Branch zusammen.

Beispiel:
```bash
git pull origin master
```
Dies lädt Änderungen vom `master`-Branch des `origin`-Repositories herunter und führt sie mit dem lokalen `master`-Branch zusammen.

---

Lernziel 66 \[6/7\]: Git-Befehle »clone«, »status«, »add«, »commit«, »fetch«, »pull« und »push« kennen und anwenden können
