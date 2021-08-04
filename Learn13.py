
# Given an array of integers, nums, and three additional integers, a, b, and c, return the total number of compatible triplets.
# Note: Three integers are said to be a compatible triplet if they are three individual numbers in nums and |nums[i] - nums[j]| <= a, |nums[j] - nums[k]| <= b, and |nums[i] - nums[k]| <= c.

# Ex: Given the following nums…

# nums = [1, 2, 3], a = 3, b = 2, c = 5, return 1.


def compatible(nums, a, b, c):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if abs(nums[i] - nums[j]) <= a and abs(nums[j] - nums[k]) <= b and abs(nums[i] - nums[k]) <= c:
                    count += 1
    return count


nums = [1, 2, 3]
a = 3
b = 2
c = 5

print(compatible(nums, a, b, c))