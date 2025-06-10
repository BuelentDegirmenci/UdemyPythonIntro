grades = [1, 2, 3, 4]

# über jedes Element der Liste iterieren und in der Konsole ausgeben

# so geht man über die Werte
for grade in grades:
    print(grade)

print("")

for idx in range(len(grades)):
    print(grades[idx])

print("")

# range(start, stop, step) -> kann die range-funktion entgegen nehmen.
for idx in range(0, 10, 1):
    print(idx)
