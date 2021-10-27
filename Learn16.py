x={'a':1,'b':2,'e':5}
y={'d':4,'c':3}

z= dict(x,**y)      

#print(z)


# Different ways to test multiple
# flags at once in Python

x,y,z=0,1,0

if 1 in (x,y,z):
    print('passed 1')
    
if any((x,y,z)):
    print('passed 2')
    
# How to sort a Python dict by value
# (== get a representation sorted by value)

xs={'a':1,'b':4,'c':2,'d':5}
print("Sorted List ")
print(sorted(xs.items(),key=lambda x: x[1]))

import operator
print("Operator sorted")
print(sorted(xs.items(),key=operator.itemgetter(1)))

name_of_user_id = {
    382: "test1",
    383: "test2",
    384: "test3"
    }


def greeting(user_id):
    return "Hi %s !" % name_of_user_id.get(user_id, "there")
            
print(greeting(384))            


            


    
    
    

