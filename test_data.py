import unittest
import firstPython

# ans1 is the answer of dummy1.in file
# ans2 is the answer of dummy2.in file

ans1 = '{\n  "entries": [\n    {\n      "color": "yellow", \n      "firstname": "Quinton", \n      "lastname": "Liptak", \n      "phonenumber": "(653)-889-7235", \n      "zipcode": "70703"\n    }, \n    {\n      "color": "aqua marine", \n      "firstname": "Ria", \n      "lastname": "Tillotson", \n      "phonenumber": "196 910 5548", \n      "zipcode": "97671"\n    }\n  ], \n  "errors": [\n    2\n  ]\n}'

ans2 = '{\n  "entries": [\n    {\n      "color": "blue", \n      "firstname": "Maurita", \n      "lastname": "Awong", \n      "phonenumber": "061 937 1243", \n      "zipcode": "15726"\n    }, \n    {\n      "color": "red", \n      "firstname": "Englebert", \n      "lastname": "G.", \n      "phonenumber": "839 014 8051", \n      "zipcode": "36410"\n    }\n  ], \n  "errors": [\n    0\n  ]\n}'

ans3 = '{\n  "entries": [\n    {\n      "color": "pink", \n      "firstname": "Shela", \n      "lastname": "Mona", \n      "phonenumber": "986 283 6066", \n      "zipcode": "11198"\n    }\n  ], \n  "errors": [\n    0, \n    1, \n    3, \n    4\n  ]\n}'

class TestData(unittest.TestCase):

	def test_data1(self):
		result = firstPython.jsonOutput('dummy1.in')
		self.assertEqual(result, ans1)

	def test_data2(self):
		result = firstPython.jsonOutput('dummy2.in')
		self.assertEqual(result, ans2)

	def test_data3(self):
		result = firstPython.jsonOutput('dummy3.in')
		self.assertEqual(result, ans3)