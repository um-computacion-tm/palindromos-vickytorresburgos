import unittest

def fibonacci(number):
    if number <=1:
        return number
    return fibonacci(number - 2) + fibonacci(number - 1)


class TestFibonacci(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(1, fibonacci(1))
    
    def test_2(self):
        self.assertEqual(1, fibonacci(2))

    def test_3(self):
        self.assertEqual(2, fibonacci(3))

    def test_4(self):
        self.assertEqual(3, fibonacci(4))
    
    def test_5(self):
        self.assertEqual(5, fibonacci(5))
    
    def test_6(self):
        self.assertEqual(8, fibonacci(6))

    def test_7(self):
        self.assertEqual(13, fibonacci(7))

    def test_8(self):
        self.assertEqual(21, fibonacci(8))

    def test_9(self):
        self.assertEqual(34, fibonacci(9))

    def test_10(self):
        self.assertEqual(55, fibonacci(10))
    


if __name__ == '__main__':
    unittest.main()
