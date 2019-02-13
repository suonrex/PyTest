#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-08 17:33:37
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

class Person:

	# class attribute
	species="human"

	# instance attribute
	def __init__(self,name,age):
		self.name=name
		self.age=age
		print("Person initialized!")

	# instance methond 
	def fire(self,weapon):
		return "{0} fires in {1}.".format(self.name,weapon)

	def fight(self):
		return "{0} is in a fight".format(self.name)

# instantiate the Person class
Ada=Person("ada","25")
Leon=Person("leon","19")

# access the class attributes
print("{0} is {1}.".format(Ada.name,Ada.__class__.species))

# access the instance attributes
print("{0} is {1} years old.".format(Leon.name,Leon.age))

# call our instance methods
print(Ada.fire("P50"))
print(Leon.fight())

# inheritance
class Zombie(Person):

	def __init__(self,name,age):
		# call super()function
		super().__init__(name,age)
		print("Zombie borned!")

	def whoisThis(self):
		print(self.name)

	def run(self):
		print("Run faster")

zombieA=Zombie("zombieA","0")
print(zombieA.__class__.species)
print(zombieA.fire("hand"))
print(zombieA.fight())
zombieA.whoisThis()
zombieA.run()

# Encapsulation
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c=Computer()
c.sell()

# change the price
c.__maxprice=1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

# Polymorphism
class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)



