# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:

# Input: s = "()"
# Output: true
class Solution(object):  
    def isValid(self, s):

        if len(s) == 0:
            return True
        else:
            if len(s)%2 != 0:
                return False
            else:
                if s[0] == '(' or s[0] == '{' or s[0] == '[':
                    return self.isValid(s[1:])
                else:
                    return False
    
ls = Solution()
a= ls.isValid("()")

print(a)
               
                # isValid("(]")
                # isValid("([)]")
                # isValid("{[]}")
                # isValid("")
                # isValid("()")
                # isValid("(])")
                # isValid("([])")
                # isValid("{[]}")
                # isValid("{[(])}")
                # isValid("{[}")