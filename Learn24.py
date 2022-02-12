
def print_something(state, metro):
    #print('Printing::', s)
    s = 'Select * %s from xyz wehre state = %s' % state % metro
    return s


output = print_something("NJ","test")
print(output)

