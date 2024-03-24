# Was sind die Herausforderungen beim Merging in der Softwareentwicklung?

Beim **Merging** werden Änderungen aus verschiedenen Branches in einen einzigen Branch integriert. Es können dabei verschiedene Probleme auftreten:
- **Merge-Konflikte**: Wenn zwei Branches Änderungen an denselben Codezeilen oder -bereichen vorgenommen haben, kann es beim Zusammenführen zu Konflikten kommen, die manuell gelöst werden müssen.
- **Integrationsschmerz**: Wenn Branches lange isoliert bleiben, kann das Zusammenführen vieler Änderungen komplex und fehleranfällig sein.
- **Build-Fehler**: Merges können zu unbemerkten Fehlern führen, die erst beim Build oder Testen auffallen, vor allem wenn nicht kontinuierlich integriert wird.
- **Feature Creep**: Durch parallele Entwicklung in Branches kann es zu unkoordinierten Feature-Entwicklungen kommen, die den Scope des ursprünglichen Projektplans überschreiten.
- **Verminderung der Codequalität**: Ohne ausreichende Review-Prozesse können Merges zu einer Verschlechterung der Codequalität führen, da inkonsistenter oder schlecht verstandener Code in den Hauptbranch gelangen kann.
  
**Durch den Einsatz von Continuous Integration und regelmäßigen Merges können viele dieser Probleme minimiert werden.**

---

Lernziel 18 \[2/2\]: Bedeutung und Probleme von Branching & Merging erläutern können
