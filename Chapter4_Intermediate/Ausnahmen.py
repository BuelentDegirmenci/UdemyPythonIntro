d = {"Jan": 27, "Peter": 33}

# was passiert wenn ich mich vertippe oder auf den Key zugreifen möchte, den es in d nicht gibt?

# print(d["Yann"])

# wenn es so ein Fehler auftritt, wollen wir nicht das Programm beendet wird
# wie würde dann ein Fallback - Lösung aussehen? -> try except
# try: ausprobieren

try:
    print(d["Yann"])
except KeyError as e:
    print(e)

print(" ")

l = [1, 2, 3]
try:
    print(l[3])
except IndexError as e:
    print(e)
