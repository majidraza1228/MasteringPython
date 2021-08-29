import unittest

def isValidSubsequence(array, sequence):
    # Write your code here
    
    if len(array) == 0:
        return False
    
    arrIndx = 0
    seqIndex = 0
    
    while (arrIndx <len(array) and seqIndex < len(sequence)):
        if array[arrIndx] == sequence[seqIndex]:
            seqIndex +=1
        else:
         arrIndx +=1
    
    return seqIndex == len(sequence)


print(isValidSubsequence([1,2,3,4,5], [1,2,3,4,5]))

