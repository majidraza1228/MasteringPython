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

