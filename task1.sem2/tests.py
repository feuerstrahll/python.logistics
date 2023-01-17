import unittest
from main.py import pre


class MyTestCase(unittest.TestCase):
    def test_pre(self):
        test = ('1. Котов Алексей: 3\n'
                '2. Бакушкин Даниил: 3\n'
                '3. Шахвалиева Юлиана: 4')
        result = pre(test)
        self.assertEqual((['Бакаушин Даниил, 3', 'Котов Алексей, 3', 'Шахвалиева Юлиана, 4']), result)
        
if __name__ == '__main__':
    unittest.main()
