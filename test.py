import unittest
import nlp
import json


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
        num = nlp.get_num(s, nlp.get_accept_nw_or_not(nlp.get_type(s)))
        self.assertEqual(num, 3)


class TestDataJsonStructure(unittest.TestCase):
	def setUp(self):
		with open('data/data.json') as f:
			self.d = json.load(f)

	def test_each_action_type_has_dict_value(self):
		for val in self.d.values():
			self.assertEqual(type(val), dict)

	def test_each_dict_has_proper_generic(self):
		for val in self.d.values():
			self.assertTrue('generic' in val)
			self.assertEqual(type(val['generic']), dict)


class TestNumberWordsJson(unittest.TestCase):
	def test_load(self):
		with open('data/number_words.json') as f:
			try:
				json.load(f)
			except json.decoder.JSONDecodeError as e:
				self.fail(f'test_load failed with {e}')


if __name__ == '__main__':
    unittest.main()
