# Wie erstellt man einen einfachen Komponententest mit JUnit und welches Namensschema sollte dabei für Testklassen und Testmethoden angewendet werden?

**JUnit Komponententest Erstellung**
Zunächst benötigen Sie eine Testklasse, die mit der Annotation `@Test` versehen ist, um anzuzeigen, dass es sich um eine Testmethode handelt. Die Testklasse sollte nach der Konvention `NameDerZuTestendenKlasseTest` benannt sein, und die Testmethoden sollten ein klares Namensschema haben, das das Verhalten beschreibt, das getestet wird, oft im Format `sollteErwartetesVerhaltenWennBedingung`.

```java
import static org.junit.Assert.*;

import org.junit.Test;

public class RechnerTest {

    @Test
    public void sollteSummeZurueckgebenBeimAddierenZweierZahlen() {
        // Arrange
        Rechner rechner = new Rechner();
        int zahl1 = 5;
        int zahl2 = 10;

        // Act
        int ergebnis = rechner.addiere(zahl1, zahl2);

        // Assert
        assertEquals("Die Summe von 5 und 10 sollte 15 sein", 15, ergebnis);
    }
}
```
In diesem Beispiel ist `Rechner` die Klasse, die getestet wird, und `addiere` ist die Methode, die getestet wird. Der Testfall `sollteSummeZurueckgebenBeimAddierenZweierZahlen` überprüft die Methode `addiere` der Klasse `Rechner`. 

Die Testmethode beginnt mit der Initialisierung der Testumgebung (**Arrange**), dann wird die Aktion durchgeführt (**Act**), und schließlich wird das Ergebnis überprüft (**Assert**).

**Namensschema für Testklassen und Testmethoden**
Das Namensschema für eine Testklasse ist in der Regel `NameDerZuTestendenKlasseTest`. Im obigen Beispiel ist `Rechner` die zu testende Klasse, daher ist der Name der Testklasse `RechnerTest`.

Für Testmethoden gibt es verschiedene Konventionen, aber eine gängige Praxis ist es, Namen zu verwenden, die sowohl das erwartete Ergebnis als auch den Kontext beschreiben. Ein gutes Schema ist `sollteErwartetesVerhaltenWennBedingung`, da es hilft, die Absicht des Tests klar zu kommunizieren. Ein Beispiel hierfür ist `sollteSummeZurueckgebenBeimAddierenZweierZahlen`, was ausdrückt, dass die Testmethode das Verhalten der `addiere`-Methode überprüft, indem sie sicherstellt, dass die Summe der übergebenen Zahlen korrekt zurückgegeben wird.

---

Lernziel 68 \[1/1\]: Einen einfachen Komponententests mit JUnit erstellen und das Namensschema für Testklassen und Testmethoden anwenden können
