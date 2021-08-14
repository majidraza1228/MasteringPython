# Given a positive integer, N, return all flippable numbers between one and N inclusive. 
# Note: A flippable number is a number whose digits can be rotated 180 degrees to form a different number. Digits 0, 1, 6, 8, and 9 become 0, 1, 9, 8, and 6 respectively when rotated. Digits 2, 3, 4, 5, and 7 are invalid when rotated. 

# Ex: Given the following value N…

# N = 10, return 3 (6, 9, and 10 are flippable).
# Ex: Given the following value N…

# N = 17, return 4.

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for i in range(1,N+1):
            s = str(i)
            if '3' in s or '7' in s:
                continue
            if '2' in s or '5' in s or '6' in s or '9' in s:
                count += 1
        return count


N=10
obj = Solution()
print(obj.rotatedDigits(N))



