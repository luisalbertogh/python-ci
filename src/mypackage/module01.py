#!C:\Herramientas\Python\WinPython-64bit-3.4.4.1\python-3.4.4.amd64\python.exe

"""
module01.py

Python module sample.
author: luisalbertogh@hotmail.com
"""

# Abstract classes
import abc;

# Garbage collector
import gc;

#Weak references for cyclic relations
import weakref;

#Sportman superclass with init method.
class Sportbeing(metaclass=abc.ABCMeta):
	"""
	Init method.
	"""
	def __init__(self, gender, nationality):
		self.gender = gender;
		self.nationality = nationality;


#Subclass extends from superclass.
class Cyclist(Sportbeing):
	"""
	Init method.
	"""
	def __init__(self, gender, nationality, name):
		# Invoke superclass init
		super().__init__(gender, nationality);
		self.name = name;

	"""
	Static mehod to create instances.
	"""
	@staticmethod
	def createInstance():
		return Cyclist('male','Spanish','Valverde');

	"""
	Set name.
	"""
	def setName(self, team):
		self.name = name;

	"""
	Print instance details (used in print).
	"""
	def __str__(self):
		return self.gender + '; ' + self.nationality + '; ' + self.name;

	"""
	Format instance details.
	"""
	def __format__(self, spec):
		return self.gender + '; ' + self.nationality + '; ' + self.name;

	"""
	Print instance details.
	"""
	def __repr__(self):
		return "{0}:{1}".format(self.__class__, self.gender + '; ' + self.nationality + '; ' + self.name);

	"""
	Override equlas method
	"""
	def __eq__(self, other):
		if(not isinstance(other, Cyclist)):
			return NotImplemented;

		return (self.gender == other.gender and self.nationality == other.nationality and self.name == other.name);

	"""
	Override hash method
	"""
	def __hash__(self):
		return hash(self.gender) ^ hash(self.nationality) ^ hash(self.name);


#More classes. It inherits from 'list' class.
class Team(list):
	"""
	Init method.
	"""
	def __init__(self, name, *team):
		super().__init__(list(team));
		for rider in self:
			rider.parent = weakref.ref(self);
		self.name = name;

	"""
	Print team
	"""
	def __str__(self):
		riders = self.name + ': ';
		for rider in self:
			riders = riders + rider.__str__() + ';';
		return riders;

	"""
	Lazy property, created when invoked.
	"""
	@property
	def totalriders(self):
		if(self):
			return len(self);

		return 0;

	"""
	Lazy property, created when invoked.
	"""
	@property
	def director(self):
		return self._director;

	"""
	Setter and deleter for riders.
	"""
	@director.setter
	def director(self, director):
		self._director = director;

	@director.deleter
	def director(self):
		self._director = None;


# Composed class.
class Tour:
	"""
	Init method.
	"""
	def __init__(self, *team):
		self.team = list(team);

	"""
	Print tour
	"""
	def __str__(self):
		riders = '';
		for riders in self.team:
			riders = riders + rider.__str__() + ';';
		return riders;

# Strategy class (stateless, no data, only logic).
class StageRules:
	def win(self, rider1, rider2):
		return True;

	def lose(self, rider1, rider2):
		return False;
