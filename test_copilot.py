
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return Trueå

def print_first_100_primes():
    count = 0import unittest
from io import StringIO
import sys

# Assuming your functions are in a module named test_copilot
from test_copilot import is_prime, print_first_100_primes

class TestCopilot(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(15))
        self.assertTrue(is_prime(17))

    def test_print_first_100_primes(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        print_first_100_primes()
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue().strip().split('\n')
        self.assertEqual(len(output), 100)
        self.assertEqual(output[0], '2')
        self.assertEqual(output[-1], '541')  # 541 is the 100th prime number

if __name__ == '__main__':
    unittest.main()
    num = 2
    while count < 100:
        if is_prime(num):
            print(num)
            count += 1
        num += 1
