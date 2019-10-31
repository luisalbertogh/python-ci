"""
testoopython.py

Unit and integration test suites.
author: luisalbertogh@hotmail.com

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
class TestOopython2(unittest.TestCase):
	"""
	Test case.
	"""
	#Set up test case
	def setUp(self):
		self.testteam = Team('Test', Cyclist('male','Spanish','Valverde'), Cyclist('male','Colombian','Quintana'), Cyclist('male','Basque','Izagirre'));

	# Test number of raiders
	def test_team_name(self):
		self.assertEqual("Test", self.testteam.name);


