import unittest
from palindromo import palindromo

class TestPalindromo(unittest.TestCase):
    
    def test_palindromo_simple_1(self):
            result = palindromo("neuquen")
            self.assertEqual(result,True)

    def test_palindromo_simple_2(self):
            result = palindromo("hola")
            self.assertEqual(result,False)




if __name__ == '__main__':
    unittest.main()