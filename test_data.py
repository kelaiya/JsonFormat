import unittest
import firstPython

ans1 = '{\n  "entries": [\n    {\n      "color": "yellow", \n      "firstName": "Quinton", \n      "lastName": "Liptak", \n      "phone": "(653)-889-7235", \n      "zipcode": "70703"\n    }, \n    {\n      "color": "aqua marine", \n      "firstName": "Ria", \n      "lastName": "Tillotson", \n      "phone": "196 910 5548", \n      "zipcode": "97671"\n    }\n  ], \n  "errors": [\n    2\n  ]\n}'

ans2 = '{\n  "entries": [\n    {\n      "color": "blue", \n      "firstName": "Maurita", \n      "lastName": "Awong", \n      "phone": "061 937 1243", \n      "zipcode": "15726"\n    }, \n    {\n      "color": "red", \n      "firstName": "Englebert", \n      "lastName": "G.", \n      "phone": "839 014 8051", \n      "zipcode": "36410"\n    }\n  ], \n  "errors": [\n    0\n  ]\n}'

class TestData(unittest.TestCase):

	def test_data1(self):
		result = firstPython.jsonOutput('dummy1.in')
		self.assertEqual(result, ans1)

	def test_data2(self):
		result = firstPython.jsonOutput('dummy2.in')
		self.assertEqual(result, ans2)