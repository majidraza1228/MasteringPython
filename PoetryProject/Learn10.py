# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        min_len = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])
        for i in range(min_len):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][:min_len]
    
    
strs = ["flower","flow","flight"]
abc=Solution()
test = abc.longestCommonPrefix(strs)

print(test)
    
    
        
        
    