# Experiments using Python arrays and vectors
# Practice code added by jmcio 4/24/22


from queue_array import Queue


def array_test():
    ar = [3, 2, 4, 5]
    print("Original: ", ar)

    ar.pop()
    print("Pop: ", ar)

    ar.append(6)
    print("Append: ", ar)

    #print(ar)
    print("Index of 4: ", ar.index(4))  # index of given value

    ar.remove(4)  # remove the first occurrence of item with given value
    print("Removed 4: ", ar)

    ar.reverse()
    print("reversed: ", ar)
    print("sorted return: ", sorted(ar))

    ar.sort()
    print("sorted in place: ", ar)


def vector_practice(size):
    vector = list(range(size))
    print("List with size: ", size, vector)


def main2():
    print()


if __name__ == "__main__":
    main2()
