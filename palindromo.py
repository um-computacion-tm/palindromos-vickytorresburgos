import unittest

#recursiva

def palindromo(word):
    word = word.lower()

    word2 = word[::-1]


    if word == word2:
         return True
    
    else:
          return False
    
#iterativa

def palindrome(palabra):
     palabra = palabra.lower()
     for letter in palabra:
           len(palabra)
     

class TestPalindromo(unittest.TestCase):
    
    def test_palindromo_simple_1(self):
            result = palindromo("neuquen")
            self.assertEqual(result,True)

    def test_palindromo_simple_2(self):
            result = palindromo("hola")
            self.assertEqual(result,False)




if __name__ == '__main__':
    unittest.main()