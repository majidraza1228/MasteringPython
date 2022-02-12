# Given a string only containing the following characters (, ), {, }, [, and ] return whether or not the opening and closing characters are in a valid order.

# Ex: Given the following strings...

# "(){}[]", return true
# "(({[]}))", return true
# "{(})", return false

        
def valid_parentheses(string):
    if len(string) == 0:
        return True
    else:
        if string[0] == '(' or string[0] == '{' or string[0] == '[':
            return valid_parentheses(string[1:])
        elif string[0] == ')' or string[0] == '}' or string[0] == ']':
            return True
        else:
            return valid_parentheses(string[1:])

    
print(valid_parentheses("(){"))
      
    
    

        
