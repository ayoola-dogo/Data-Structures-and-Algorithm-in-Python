nums = [1, 4, 5, 6, 10, -4, 67, 100]

for i in nums:      # This has a running time complexity of O(n)
    if nums[i] == 10:      # This has a running time complexity of O(1)
        print("Index of the  item you are looking for is ", i)
        break

# We will end up with a linear time complexity algorithm
