import unittest
from data import sort_and_out, read_file


class Test_task2(unittest.TestCase):
    def test(self):
        rf = read_file("input.txt")
        self.assertEqual(sort_and_out(rf), 'KP2.2-01 - Vedomost\n'
                                                    'KP2.2-01.1 - Vedomost\n'
                                                    'KP2.2-01.2 - Vedomost\n'
                                                    'KP2.2-01.3 - Vedomost\n'
                                                    'KP2.2-2 - Schema\n')
        
if __name__ == '__main__':
    unittest.main()
