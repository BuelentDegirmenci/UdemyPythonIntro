# Ein abstrahierter Datentyp bilden
# __init__: Konstruktur in Pyhton
#: self : = this in Java, C++
class Animal:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

# wir können der Animal - Klasse eine weitere Methode verpassen, da sie aber in der Elternklasse definiert ist, kann sie
# von den Objekten der Kinder-Klasse aufgerufen werden
    def print_data(self):
        print("Height: ", self.height)
        print("Weight: ", self.weight)

# Neben der Klasse Animal, wollenw wir zwei weitere Klassen erstellen.
class Dog(Animal): # Hier in Klammern geben wir den Namen der Klasse von der wir erben wollen, haben wir in den unteren
    # classen weight und height, die vererben wir dann.
    # Das ist die Gemeinsamkeit (weight, heigth), die sich Cat und Dog teilen
    # damit es funktioniert müssen wir noch in der Konstruktur der Kinderklasse, den Konstruktor der Elternklasse aufrufen
    # das geht mit dem folgenden Ausdruck, das geschiet über "super().__init__(weight, height)"
    def __init__(self, weight, height):
        super().__init__(weight, height)

# die Hunde Classe hat ihre eigene Funktion bark hat
    def bark(self):
        print("Bark!")




class Cat(Animal):
    def __init__(self, weight, height):
        super().__init__(weight, height)

    def meow(self):
        print("Meow!")

# Ein Hund und eine Katze haben gemeinsame Eigenschaften. Diese gemeinsame Eigenschaften bleiben in der Klasse Animal.
# Das ist die Base classe, von der Hunde und Katzen classen erben.
# Vererbung bedeutet einfach: ich übernehme alles aus der Klasse von der ich erbe, kann aber zusätzlich für mich selber
# weitere Eigenschaften definieren.



def main():
    dog = Dog(10.0, 30.0)
    dog.bark()
    dog.print_data()

    cat = Cat(50.0, 20.3)
    cat.meow()
    cat.print_data()



if __name__ == "__main__":
    main()
