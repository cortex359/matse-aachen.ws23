# Was sind die Schritte der Konfliktauflösung nach einem »Merge«?

**Schritte der Konfliktauflösung nach einem »Merge«**
1. **Erkennen**: Das Versionskontrollsystem zeigt an, dass ein Konflikt aufgetreten ist. Dies kann während eines Merge-Vorgangs passieren, wenn die gleichen Zeilen von Code in beiden zu mergenden Branches verändert wurden oder wenn eine Datei gelöscht wurde, während in einem anderen Branch daran Änderungen vorgenommen wurden.
   
2. **Analyse**: Überprüfen Sie die betroffenen Codezeilen und verstehen Sie die Änderungen, die in beiden Branches vorgenommen wurden. Dies hilft dabei, den Grund für den Konflikt zu verstehen.

3. **Entscheidung**: Basierend auf dem Verständnis der konfligierenden Änderungen entscheiden Sie, welche Änderungen erhalten bleiben sollen. Manchmal bedeutet dies, einen Kompromiss zwischen den Änderungen zu finden, die Änderungen zusammenzuführen oder eine der Änderungen komplett zu verwerfen.

4. **Auflösung**: Nehmen Sie die gewünschten Änderungen manuell vor, indem Sie den Code so bearbeiten, dass er den gewünschten Zustand nach dem Merge widerspiegelt. Entfernen Sie Markierungen, die das Versionskontrollsystem eingefügt hat, um den Konflikt anzuzeigen.

5. **Test**: Führen Sie Tests durch, um sicherzustellen, dass der Code nach der Konfliktauflösung wie erwartet funktioniert. Dies sollte sowohl manuelle Tests als auch das Ausführen vorhandener automatisierter Tests umfassen.

6. **Commit**: Nach erfolgreicher Konfliktauflösung und Test durchführen Sie einen neuen Commit mit der Auflösung des Konflikts in das Versionskontrollsystem ein. Dies bestätigt, dass der Konflikt behoben wurde.

7. **Kommunikation**: Informieren Sie Ihr Team über die durchgeführte Konfliktauflösung, besonders wenn die Änderungen andere Teile des Projekts beeinflussen können, oder wenn die Auflösung eine Entscheidung war, die andere Teammitglieder betreffen könnte.

8. **Weitermachen**: Fahren Sie mit dem Entwicklungsprozess fort, jetzt mit einem aktualisierten Codebase, der die Änderungen aus beiden Branches enthält.

Es ist wichtig, während des Prozesses sorgfältig vorzugehen und bei Bedarf Rat und Konsens im Team zu suchen, um die besten Entscheidungen zu treffen.

---

Lernziel 67 \[1/1\]: Schritte der Konfliktauflösung nach einem »Merge« erläutern können
