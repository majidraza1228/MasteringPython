def generate_prime_numbers(n):
    prime_numbers = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers

# Unit test
def test_generate_prime_numbers():
    """
    Unit test for the generate_prime_numbers function.
    """
    # Set n to 10. This is the input that will be passed to the generate_prime_numbers function.
    n = 10
    # The expected output when n is 10 is a list of prime numbers from 2 to 10.
    expected_prime_numbers = [2, 3, 5, 7]
    # The assert statement checks if the output of generate_prime_numbers(n) is equal to expected_prime_numbers.
    # If the output is as expected, the test will pass. If not, the test will fail, and an AssertionError will be raised.
    assert generate_prime_numbers(n) == expected_prime_numbers