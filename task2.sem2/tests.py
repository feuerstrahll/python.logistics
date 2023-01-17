import unittest
from data import sort_and_out, read_file


class Test_task2(unittest.TestCase):
    def test(self):
        rf = read_file("input.txt")
        self.assertEqual(sort_and_out(rf), read_file("output.txt"))
        
if __name__ == '__main__':
    unittest.main()
