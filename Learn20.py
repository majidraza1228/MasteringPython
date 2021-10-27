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
