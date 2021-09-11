print("************************ List Starts ************************")


a=[1,2,3,4,5,6]
# List : Ordered, mmutable, allow duplicate

b=a[1::2]
print(b)


def even(x):
    return x % 2 == 0

for item in a[:]:
    if even(item):
        a.remove(item)
          
print(a)


#mylist=['majid','test',1,2,3,4,5]

#mylist=[0]*5

mylist=[1,2,3,4,5,6,7,8,9,10]

a= mylist[1:5]


print("************************ List End ************************")




print("************************ Tuple Start ************************")
#Tuple Orderd , immutable , allow duplicate

print(a)

mytuple = tuple(["list",2,"syed","raza",5,4])

#print(mylist[:])

#print(mytuple)

for i in mytuple:
    print(i)
    
if "syed" in mytuple:
    print("yes")
else:
    print("no")
    
print("************************ Tuple End ************************")


print("************************ Ditionary Start ************************")

# Dictonary : key value,  unordered, mutable, no duplicate

print("************************ Ditionary End ************************")

# Set : unordered, no duplicate, mutable
print("************************ Set Starts ************************")



print("************************ Set End ************************")


# Strings : Ordered, immutable, text respresentation

print("************************ Strings Starts ************************")

# my_string = """Hello \
# World """

my_string= "Hello world"
char = my_string[1]

print(char)

print("************************ Strings End ************************")

 
# Collections : Counter, namedtuple, OrerderedDict, OrderedSet, deque, defaultdict

print("************************  Collection Starts ************************")

from collections import Counter

a= "aaaaaaaabbbbcccc"

my_Counter = Counter(a)

print(my_Counter.most_common)

print("************************ Collection End ************************")



print("************************ Lambda Function Start ************************")

add10 = lambda x: x+10
print(add10(5))


def add10_func(x):
    return x+10

print(add10_func(25))

point2D={(1,2),(15,1),(5,-1),(10,4)}
point2D_sorted= sorted(point2D)

print(point2D_sorted)





print("************************ Lambda Function End ************************")