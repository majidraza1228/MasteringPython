# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321

def reverse(self, x):
    # write your code here
    if x == 0:
        return 0
    sign = (x > 0) - (x < 0)
    x = abs(x)
    result = 0
    while x != 0:
        result = result * 10 + x % 10
        x //= 10
    return result * sign

b = reverse(1, 123)
print(b)
