import unittest
import nlp


s = 'i drink 3 liters of water a day'
class TestParse(unittest.TestCase):
    def test_all(self):
        action_type, num, unit = nlp.get_type_num_unit(s)
        self.assertEqual(action_type, 'drink-water')
        self.assertEqual(num, 3)
        self.assertEqual(unit, 'liters')

    def test_get_type(self):
        action_type = nlp.get_type(s)
        self.assertEqual(action_type, 'drink-water')
        
    def test_get_unit(self):
        unit = nlp.get_unit(s, nlp.get_type(s))
        self.assertEqual(unit, 'liters')

    def test_get_num(self):
        num = nlp.get_num(s)
        self.assertEqual(num, 3)




if __name__ == '__main__':
    unittest.main()
