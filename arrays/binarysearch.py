#  Practice code added by jmcio 5/24/2022
#  Implement binary search


def binary_search(v_key, array_v, min_v, max_v):
    if max_v < min_v:
        return False
    mid_point = find_midpoint(min_v, max_v)
    if array_v[mid_point] < v_key:
        return binary_search(v_key, array_v, mid_point + 1, max_v)
    elif array_v[mid_point] > v_key:
        return binary_search(v_key, array_v, min_v, mid_point - 1)
    else:
        return mid_point


def find_midpoint(min_v, max_v):
    return round((max_v + min_v) / 2)


def main():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    target = 61
    found = binary_search(target, primes, 0, len(primes) - 1)
    if found:
        print(f"Target {target} found in position {found}")
    else:
        print(f"Target {target} not found.")


if __name__ == "__main__":
    main()
