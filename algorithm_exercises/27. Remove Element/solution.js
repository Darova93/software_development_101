export const removeElement = (nums, val) => {
    const length = nums.length
    let i = 0
    while (i < length) {
        if (nums[i] === val) {
            nums.splice(i, 1)
        }
        else {
            i++
        }
    }
    return nums.length
};
