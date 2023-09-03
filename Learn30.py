x= lambda a,b : a+b
y=x(5,6)

print(y)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(len(thisdict))
#NOT a tuple
thistuple = ("apple",)
print(type(thistuple))

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3= tuple1+tuple2

# print(tuple3)

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)