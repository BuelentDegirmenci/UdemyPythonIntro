# Ein abstrahierter Datentyp bilden
# __init__: Konstruktur in Pyhton
#: self : = this in Java, C++
class Animal:
    def __init__(self, weight, height):
        # Hat die Klasse oben, e.g. Körpergröße und Gewicht als Attribtue, damit die Attribute der Klasse gehören,
        # müssen wir self verwenden
        self.weight = weight
        self.height = height
        # d.h. ich habe in der Klasse zwei Instanzattribute, height u. weight definiert, innerhalb der Klasse kann ich
        # mit self.weight, self.hight auf die Attribute zugreifen.
        # Außerhalb der Klasse, e.g. dog unten, kann ich  mit dem Objektnamen, also Instanznamen und .height oder weight
        # drauf zugreifen
        # innerhalb der Klasse = self, ausserhalb der Klasse Objektname (dog) selber
        # da wir die beiden Attribute nicht immer mit Null intialisieren willen, geben wir es bei der Objekterstellung
        # ein.

# wenn jedes Tier eine gemeinsame Funktionalität hat,
# d.h. wir wollen dieser Klasse eine Methode definieren
# Eine Methode ist eine Funktion innerhalb einer Klasse
# jede Methode muss einmal self übergeben bekommen, damit intern Zugehörigkeit einer Instanz vorliegt.
# wenn wir unten sagen, dog.jump() dann ist dieses dog, ist diese Instanz self
    def jump(self):
        print("Es sprint")



# wie kann ich ein Objekt dieser Klasse erstellen?
def main():
    # hier wird ein Animal Objekt erstellt
    dog = Animal(10.0, 30.0)  # ein Objekt, eine  Instanz von der Animal Klasse
                    # mit der runden Klamme von der Animal-Funktion ruft man den Konstruktor oben auf
                    # ob im Konstruktor ist self, hier bei der Animal Funktion haben wir kein Agument übergeben
                    # ist es richtig?
                    # self ist immer implizit mit angegeben. Das gibt man nicht mit an.
    # print(dog)      # was passiert wenn ich die dog-Variable ausgeben will, in dieser Form, bekommen wir nur die
                    # Speicheradresse zurück.
# wenn ich auf weight und hight zugreifen möchte, dann schreibe da an der Stelle wo ich drauf zugreifen möchte
    print(dog.weight, " ", dog.height)

# wir können beliebig viele Objekte dieser Klasse erstellen, e.g. cat
    cat = Animal(50.0, 20.3)
    print(cat.weight, " ", cat.height)


# wie kann ich die Methode (jump()) oben aufrufen?
    dog.jump()
    cat.jump()


if __name__ == "__main__":
    main()
