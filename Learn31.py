# f = open('car.txt','w')

# cars=['test1','test2']

# for car in cars:
#     f.write(car + '\n')

# import json
# cars = [
#   {"make": "chevy"},
#   {"make": "tesla"},
#   {"make": "porsche"}
# ]
# with open('car.json','w') as f:
#     json.dump(car,f)
    
def sortedSquaredArray(array):
        # Write your code here.
        sortedSquares = [ 0 for _ in array]
        
        for idx in range(len(array)):
            sortedSquares[idx] = array[idx] * array[idx]
            
        sortedSquares.sort()
        
        return sortedSquares
    

print(sortedSquaredArray([-4,-1,0,3,10]))

       