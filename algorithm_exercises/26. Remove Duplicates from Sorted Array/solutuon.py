def removeDuplicates(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            nums[k] = nums[i]
            k += 1
    return k
