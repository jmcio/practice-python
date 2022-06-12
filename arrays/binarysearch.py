#  Practice code added by jmcio 5/24/2022
#  Implement different versions of binary search


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
    return min_v + (max_v - min_v) // 2


def template_binary_search(array) -> int:
    def condition(value) -> bool:
        pass
    search_space = array  # depends on the problem
    left, right = min(search_space), max(search_space)  # could be [0,n] or [1,n], depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left  # could be return left - 1mid, depends on problem


def my_sqrt(x: int) -> int:
    left, right = 0, x + 1
    while left < right:
        mid = left + (right - left) // 2
        if mid * mid > x:
            right = mid
        else:
            left = mid + 1
    return left - 1


def search_insert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left


def main():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    target = 61
    found = binary_search(target, primes, 0, len(primes) - 1)
    if found:
        print(f"Target {target} found in position {found}")
    else:
        print(f"Target {target} not found.")

    print(my_sqrt(128))


if __name__ == "__main__":
    main()
