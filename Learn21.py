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



