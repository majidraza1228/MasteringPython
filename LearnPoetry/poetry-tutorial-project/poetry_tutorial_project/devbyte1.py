"""""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


Example 1:

Input: x = 123
Output: 321
"""


class Solution(object):
  
    def reverse(self, x):
      #type x: int
    # rtype: int
  
        if x == 0:
              return 0
                neg = False
        if x < 0:
            neg = True
            x = -x
            x = str(x)
            x = x[::-1]
            x = int(x)
        if neg:
            x = -x
        if x < -2147483648 or x > 2147483647:
            return 0
            
 
    

            print(my_function(123)