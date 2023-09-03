from pdb import lasti2lineno


def remove_even(lst):
    
    odds = []
    
    for number in lst:
        
        if number % 2 !=0:
            odds.append(number)
    
    return odds


lst2 = [3, 2, 41, 3, 34]
print(remove_even(lst2))
