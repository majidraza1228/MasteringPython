a=[1,2,3,4,56,78,9]

#print(a[2:4])

b = []
id(b)

b.append(3)

a= 4
a =a+1
#
# 
# print(id(a))

# print(3/4)
# # print(3//4)

# print("The ball is red".endswith("is red"))
# print("The ball is red".find("is"))

# help("will".rstrip)

# print("".join(["the ", "ball ","is ", "red"]))

# print("will".isupper())
# print(help("foo".upper))
#print(dir("will"))


animals = {'monkey', 'bear', 'dog', 'monkey', 'cat', 'bear', 'gorilla'}

if 'monkey' in animals:
    print('yes')
else:
    print('no')
    
print(animals)


fish = set()

fish.add('cat')
fish.add('dog')

print(fish)

print(fish.union(animals))




try :
    print(1/2)
except ValueError as e:
    print("ZeroDivisionError")
    