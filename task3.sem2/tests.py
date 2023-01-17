import unittest
from main import formatted_file, read_file


class Test_task3(unittest.TestCase):
    def test_pre(self):
        
        self.assertEqual(read_file("data.txt")[:2], ['She', 'married'])
        
        prepare = read_file("data.txt")
        self.assertEqual(formatted_file(prepare),   'She married a very\n'
                                                    'nice young architect\n'
                                                    'from Belfast, whom\n'
                                                    'she met on a bus. ')
        
if __name__ == '__main__':
    unittest.main()
