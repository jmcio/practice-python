#  Practice code added by jmcio 5/21/2022
#  Implement a hash function


from hash_distribution import plot,distribute
from string import printable


def hash_function(key):
    return sum(ord(character) for character in repr(key))


def hash_function2(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key), start=1)
    )


plot(distribute(printable, 6, hash_function2))
