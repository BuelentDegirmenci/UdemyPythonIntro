

def list_max(input_list):               # Mit dem Pameter lassen wir die Funktion für alle Listen gültig
    max_value = input_list[0]
    for i in range(1, len(input_list)):
        if input_list[i] > max_value:   # wenn während der iteration, der gefundene Wert gößer als der aktuelle Wert ist,
            max_value = input_list[i]   # dann update ich den größten gefunden Wert, das mache ich solange bis alle Elemente durch sind

    return max_value         # dann kann ich den gefunden Wert ausgeben.


def test(param1):
    print("test function", param1)


list1 = [-2, 1, 2, -10, 22, -10]
max_value = list_max(list1)
print(max_value)
list2 = [-20, 123, 112, -10, 22, -120]
max_value = list_max(list2)
print(max_value)

test("test-function")

# Positional - Argument: was wir übergeben müssen, sofern man im Funktionsaufruf keine Default-Parameter angegen hat


def test2(param2="hello"):
    print("test function", param2)


test2("byebye")
# man den Default-Parameter überschreiben
