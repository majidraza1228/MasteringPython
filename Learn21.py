<<<<<<< HEAD
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
      
    
    

        
=======
owner='majid'
test =100

#print('Here is, {} is now {} this is learning'.format(owner,test))


a=1

def some_func():
    return a

#print (some_func())

def another_func():
    a=a+1
    return a 
#print (another_func())

def some_closure_func():
    a=1
    def some_inner_func():
        return a    
    return some_inner_func()

#
# print( some_closure_func())

def another_func():
    global a
    a +=1
    return a               

print(another_func())



>>>>>>> e62631bd950cd92afae07d365aca5d3f77280a92
