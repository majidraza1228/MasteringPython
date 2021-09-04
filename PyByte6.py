def twoNumberSum(array,targetSum):
    # Write your code here.
    # Return the two number's sum in the form of a list of tuples
    for (i,num) in enumerate(array):
        for (j,num2) in enumerate(array[i+1:]):
            if (num+num2)==targetSum:
                return [num,num2]
            
# Test cases
print(twoNumberSum([1,2,3,4,5,6,7,8,9,10],10))#


        
 

