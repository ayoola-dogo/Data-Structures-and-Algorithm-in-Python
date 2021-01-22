from random import randint
import time


nums = list()

for i in range(20000):
    nums.append(randint(0, 100))

t = time.process_time()
# start = time.time()

for i in range(len(nums)):
    for j in range(1, len(nums)-i):
        if nums[j-1] > nums[j]:
            temp = nums[j-1]
            nums[j-1] = nums[j]
            nums[j] = temp

elapse_time = time.process_time() - t
# end = time.time()

print("Algorithm takes time to finish: ", elapse_time, " ms")
