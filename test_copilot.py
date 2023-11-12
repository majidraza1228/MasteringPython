
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def print_first_100_primes():
    count = 0
    num = 2
    while count < 100:
        if is_prime(num):
            print(num)
            count += 1
        num += 1
