

def three_sum(nums):
    if len(nums) < 3:
        return []

    nums_sorted = sorted(nums)
    list_to_return = []

    for i in range(len(nums_sorted) - 2):
        if i != 0 and (nums_sorted[i] == nums_sorted[i-1]):
            continue
        j = i+1
        k = len(nums_sorted) - 1
        while j < k:
            if k < len(nums_sorted) - 1 and nums_sorted[k] == nums_sorted[k+1]:
                k -= 1

            if nums_sorted[i] + nums_sorted[j] + nums_sorted[k] == 0:
                temp = [nums_sorted[i], nums_sorted[j], nums_sorted[k]]
                list_to_return.append(temp)
                j += 1
                k -= 1

            elif nums_sorted[i] + nums_sorted[j] + nums_sorted[k] > 0:
                k -= 1
            elif nums_sorted[i] + nums_sorted[j] + nums_sorted[k] < 0:
                j += 1
    return list_to_return


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    nums1 = three_sum(nums)
    print(nums1)