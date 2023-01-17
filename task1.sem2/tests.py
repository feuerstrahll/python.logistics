import unittest
from tests import pre, sor, out


class Testtask(unittest.TestCase):
    def test_pre(self):
       self.assertEqual(pre("data.txt")[0], 'Котов Алексей: 3')

    def test_sor(self):
        self.assertEqual(sor("data.txt")[0], ['Белова Юлия', '3'])
        
    def test_out(self):
        self.assertEqual(out("data.txt")[0], 'Белова Юлия,3')
        
if __name__ == '__main__':
    unittest.main()
