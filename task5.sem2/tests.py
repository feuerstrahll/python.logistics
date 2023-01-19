import unittest
from tests import formatted_to_anagrams


class Test_task5(unittest.TestCase):
    def test(self):
        desired = [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]
        data = ["eat","tea","tan","ate","nat","bat"]
        self.assertEqual(formatted_to_anagrams(data), desired)
        
if __name__ == '__main__':
    unittest.main()
    

--------------------------------------------------------------



import unittest
from tests import formatted_to_anagrams


class Test_task5(unittest.TestCase):
    def test(self):
        desired = [['bar', 'bra', 'rab'], ['com', 'moc'], ['llo', 'lol', 'oll']]
        data = ["bra","bar","com","rab","lol","moc", "llo", "oll"]
        self.assertEqual(formatted_to_anagrams(data), desired)
        
if __name__ == '__main__':
    unittest.main()
