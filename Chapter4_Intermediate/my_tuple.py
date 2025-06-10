# tupple hat ein rundes Klammerpaar
# die Länge des Tupels ist fest
# die Tuplevariable kann man nicht verändern
# Beim Tuple muss kan kein Klammerpaar angegeben, die Werte sind durch Kommata aufgezählt
# Klammer ist optional, damit symbolisiert man, dass es eine Tupel ist
tuple_a = (1, 2, 3)

list_a = [100.0, 200.0, -10.0]
list_b = [False, False, True] # wenn die Person pleite ist, dann true

# Zu dem Kontostand ausgeben, ob die Person pleite ist
for idx in range(len(list_a)): # so kann man über die beide Listen iterieren, in dem wir eine index Variable idx verwenden
    # wenn wir den aktuellen Wert an den Index haben wollen, aus der Liste, dann muss die Ausgabe wie in der Printanweisung
    # mit den eckigen Klammern folgen
    # print(list_a[idx], list_b[idx])
    pass

# Es gibt eine Funktion aus der Standardlibrary die einem es deutlich vereinfacht
# die Funktion zip, die gibt nach jeder Iteration ein Tupel zurück
# das Tupel hat in dem Falle unten zwei Werte, weil wir der Funktion zwei iterierbare Objekte übergeben haben
# d.h. _, _ da bekommen wir zwei Werte pro Iteration zurück
# for _, _ in zip(list_a, list_b):
print(" ")
for val_a, val_b in zip(list_a, list_b, strict=False):
    # print(val_a, val_b)
    pass

print(" ")

# wenn man den Index und die Werte haben möchte, was bei zip nicht geht, dann gereift man auf die Funktion enumarate
for idx, val in enumerate(list_a):
    pass
    # print(idx, val)

print(" ")
for idx, (val_a, val_b) in enumerate(zip(list_a, list_b, strict=False)):
    print(idx, val_a, val_b)
    # print(list_a[idx], list_b[idx])
