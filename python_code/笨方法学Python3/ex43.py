# 本章为第45章
# 类(class)和对象(object)的区别


class Animal(object):
	"""docstring for ClassName"""
	pass

class Dog(Animal):
	"""docstring for ClassName"""
	def __init__(self, name):
		self.name = name
		
class Cat(Animal):
	def __init__(self, name): 
		self.name = name

class Person(object):
	def __init__(self, name):
		self.name = name
		self.pet = None

class Employee(Person):
	def __init__(self, name, salary):

		super(Employee, self).__init__(name) 
		self.salary = salary

class Fish(object): 
	pass

class Salmon(Fish): 
	pass

class Halibut(Fish): 
	pass
## rover is-a Dog
rover = Dog("Rover")
## satan is-a cat
satan = Cat("Satan")
## mary is-a Person
mary = Person("Mary")
## mary 的宠物是satan，一只猫
mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()