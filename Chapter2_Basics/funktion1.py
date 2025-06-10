list1 = [-2, 1, 2, -10, 22, -10]

# schreibe eine Funktion die den größe Wert der Liste zurückgibt
# dafür muss man über alle Elemente der Liste iterieren
# zwischen Speichern was der aktuell der größte Wert ist
# wenn man alle Elemente durchgegangen ist, dann hat man den größten Wert gefunden

# schreiben wir die Funktion, die das kann und dann auslagern
# Definiere eine Variable, die mit dem ersten Wert in der Liste initialisiert ist
max_value = list1[0]
# danach iterieren wir über weitere Werte
for i in range(1, len(list1)):
    if list1[i] > max_value: # wenn während der iteration, der gefundene Wert gößer als der aktuelle Wert ist,
        max_value = list1[i] # dann update ich den größten gefunden Wert, das mache ich solange bis alle Elemente durch sind

print(max_value)         # dann kann ich den gefunden Wert ausgeben.

list2 = [-20, 123, 112, -10, 22, -120]
