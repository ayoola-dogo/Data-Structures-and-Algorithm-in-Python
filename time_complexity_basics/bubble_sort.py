nums = [1, 6, 3, 8, 12, 34, 2, 4]


for i in range(len(nums)):
    for j in range(1, (len(nums))-i, 1):
        if nums[j-1] > nums[j]:
            temp = nums[j-1]
            nums[j-1] = nums[j]
            nums[j] = temp
print(nums)
