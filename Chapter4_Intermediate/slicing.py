list_a = [i for i in range(10)]
print(list_a)

# wenn ich die ersten drei Elemente der Liste abpeichern möchte, in list_b
# list_b = []
# for i in range(3):
#     list_b.append(list_a[i])
# print(list_b)

# alternativ mit list_comprehension
list_b = [list_a[i] for i in range(3)]
print(list_b)

# Alternativ noch, slicing
list_c = list_a[0:3]
print(list_c)
