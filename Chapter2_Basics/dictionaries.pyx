# es wäre schön einen Namen zu Noten zu speichern

           # key (links) - value (rechts)
students = {"Ben": 1, "Jan": 2, "Peter": 1, "Melissa": 4}
print(students)

# wie kann ich auf einen Wert im Dictionary zugrefen
student1 = students["Peter"]
print(student1)

# wie kann man den Wert updaten
students["Ben"] = 6
print(students)

# wie kann ich einen Wert hinzufügen, wenn es noch keinen Eintrag zu hinzufügenden Element gibt, dann wird er erstellt
students["Julia"] = 1
print(students)

# Ein Element löschen, den Key muss jedoch geben, er muss exitieren
students.pop("Julia")
print(students)

# wie kann man über die Datenstruktur Dictionary iterieren
for student_name in students:
    print(student_name)

# über Values iterieren
for student_grade in students.values():
    print(student_grade)

# Keys und Values
for key, value in students.items():
    print(key, value)
