<<<<<<< HEAD
#  Given a string, reverse all of its characters and return the resulting string.

# Ex: Given the following strings...

# “Cat”, return “taC”
# “The Daily Byte”, return "etyB yliaD ehT”
# “civic”, return “civic”


def reverse(sreverse):
    if len(sreverse) == 1:
        return sreverse
    else:
        return reverse(sreverse[1:]) + sreverse[0]
    if len(sreverse) == 0:
        return sreverse
    else:
        return reverse(sreverse[1:]) + sreverse[0]
        

print(reverse("Cat"))

# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

=======
def some_func():
    try:
        return "from try func"
    finally:
        return "from finally func"

def another_func():
     for _ in range(3):
         try:
             continue 
         finally:
             print("Finally another func")
             
def one_more_func():
    try:
        for i in range(3):
            try:
                1/i      
            except ZeroDivisionError:
                raise ZeroDivisionError("zero erro ")
            finally:
                print("Iteration",i)
                break 
    except ZeroDivisionError as e:
        print("Division Erro ",e)
        
        
        

# print(some_func())
# print(another_func())

print(one_more_func())
>>>>>>> e62631bd950cd92afae07d365aca5d3f77280a92
