
def hamming_distance(arr1, arr2):
    """
    Given: length of the arrays is same
    To Find: hamming distance
    """
    count = 0
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            count += 1
    return count


def hamming_int(x, y):

    s = x ^ y
    set_bits = 0
    while s > 0:
        set_bits += s & 1
        s >>= 1
    return set_bits


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4]
    arr2 = [1, 3, 2, 4]

    x = 1
    y = 4
    print(hamming_int(x, y))
    # print(hamming_distance(arr1, arr2))
