# Den Inhalt einer Datei, in dem Falle test.txt einlesen
# damit wir pyhton sagen können wo die Datei liegt,wollen wir die Datei kurz abspeichern, den Pfad zu der Datei

input_filepath = "C:/Udemy/UdemyPythonIntro/Chapter4_Intermediate/test.txt"
output_filepath = "C:/Udemy/UdemyPythonIntro/Chapter4_Intermediate/test_out2.txt"

# jetzt wollen wir die Datei öffnen und das geht mit File-Object
# die open Funktion wird ein file Objekt returnen
# with: gibt mehr oder weniger einen Gültigkeitsbereich an, so halbe Wahrheit, so dieses file Objekt gültig ist
# file: Objekt hat verschiedene Funktionalitäten, mit dem wir, in dem Kontext, aus der Datei lesen können
with open(input_filepath, "r") as file:
    content = file.readlines() # in content gespeichert, content ist eine Variable
print(content)

content.append("Buelent\n")
# writelines(): man kann eine iterierbare Objekt der Funktion übergeben
# eine Liste ist ein iterierbares Objekt, d.h. content können wir der Funktion writelines(content) übergeben
with open(output_filepath, "w") as file:
    file.writelines(content)
