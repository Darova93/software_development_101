def removeDuplicates(nums):
    uniqueValues = 1
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            nums[uniqueValues] = nums[i]
            uniqueValues += 1
    return uniqueValues
