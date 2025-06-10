from min_max_func import list_max, list_min


def main():
    list1 = [-2, 1, 2, -10, 22, -10]
    max_value = list_max(list1)
    print(max_value)
    min_value = list_min(list1)
    print(min_value)
    print(" ")
    list2 = [-20, 123, 112, -10, 22, -120]
    max_value = list_max(list2)
    print(max_value)
    min_value = list_min(list2)
    print(min_value)


if __name__ == "__main__":
    main()
