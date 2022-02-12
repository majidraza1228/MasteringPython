def fun(a,b):
    str = "geeksforgeeks"+" "+a + " " +b
    x = 20
    return str, x;  # Return tuple, we could also
                    # write (str, x)
   
# Driver code to test above method
str, x = fun("syed","raza") # Assign returned tuple
print(str)
print(x)

print("%d %s cost $%.2f" %(6, "bananas", 1.74))

fruits=["bananas","apples","oranges"]

print(fruits[2])
print(len(fruits))

print(10==10)

print("%05d" % 123)
