# You are given a code and asked to modify the code to unlock a vault. In addition to the code, you’re also given a value k. To unlock the vault, you must modify each value in code based on the value of k. If k > 0, you must replace the ith value with the sum of the next k values. If k < 0, you must replace the ith value with the sum of the previous k values. If k == 0, you must replace the ith value with the number zero. Return the correct code to unlock the vault. 
# Note: Values in code are circular meaning that the “next” value after the last value in code is the first value in code and similarly, the previous value to the first value in code is the last value in code. 

# Ex: Given the following code and value k…

# code = [1, 2, 3], k = 2, return [5, 4, 3] (2 + 3, 3 + 1, 1 + 2).
# Ex: Given the following code and value k…

# code = [4, 1, 3], k = -1, return [3, 4, 1].

class Solution(object):
    def modifyCode(self, code, k):
        """
    :type code: List[int]
    :type k: int
    :rtype: List[int]
    """
        if k == 0:
            return code
        elif k > 0:
            return [sum(code[i:i+k]) for i in range(len(code))]
        else:
            return [sum(code[i:i+k]) for i in range(k, len(code))]
        

code = [4, 1, 3]
k = -1
result = Solution()

print (result.modifyCode(code, k))


