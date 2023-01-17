import unittest
from main import prepare, read_file


class Test_task4(unittest.TestCase):
    def test(self):
        rd = read_file("input.txt")
        self.assertEqual(prepare(rd)[:rd.index(" ")+5], "('i', 3)" )
        
if __name__ == '__main__':
    unittest.main()
