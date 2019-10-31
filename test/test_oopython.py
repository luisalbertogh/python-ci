"""
testoopython.py

Unit and integration test suites.
author: luisalbertogh@hotmail.com

Run using:
$ python -m unittest discover test/
"""

import unittest;
"""
Apend module path.
"""
import sys;
import os;
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","src")));
from mypackage import *;

# Test case class
class TestOopython(unittest.TestCase):
	"""
	Test case.
	"""
	#Set up test case
	def setUp(self):
		self.testteam = Team('Test', Cyclist('male','Spanish','Valverde'), Cyclist('male','Colombian','Quintana'), Cyclist('male','Basque','Izagirre'));

	# Test number of raiders
	def test_team_members(self):
		self.assertEqual(3, self.testteam.totalriders);

	# Test included raiders
	def test_raiders(self):
		self.assertEqual(Cyclist('male','Spanish','Valverde'), self.testteam[0]);
		self.assertEqual(Cyclist('male','Colombian','Quintana'), self.testteam[1]);
		self.assertEqual(Cyclist('male','Basque','Izagirre'), self.testteam[2]);

# Test suite with pervious test cases
def testsuite():
	s = unittest.TestSuite();
	load_from = unittest.defaultTestLoader.loadTestsFromTestCase;
	s.addTests(load_from(TestOopython));
	return s;

# Run test suite
if __name__ == "__main__":
	"""
	Run test suite
	"""
	tr = unittest.TextTestRunner();
	tr.run(testsuite());