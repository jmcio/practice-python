# Element Appearing more than 25% in sorted array
# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs
# more than 25% of the time. Return that integer.


def sorted_array(ar):
    qtr_v = round(len(ar) / 4)
    for i in range(len(ar) - qtr_v):
        if ar[i] == ar[i+qtr_v]:
            return ar[i]
    return -1


def main():
    ar = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    print("Element more than 25%: ", sorted_array(ar))


if __name__ == "__main__":
    main()