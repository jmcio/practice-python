#  Practice code added by jmcio 5/21/2022
#  Print the distribution of a hash function using Counter

#  hash_distribution.py

from collections import Counter
from string import printable


def distribute(items, num_containers, hash_function=hash):
    return Counter([hash_function(item) % num_containers for item in items])


def plot(histogram):
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'■' * count}{padding} ({count})")


# plot(distribute(printable, num_containers=2))
#
# print()
# print()
#
# plot(distribute(printable, num_containers=5))
