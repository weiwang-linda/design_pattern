#
#***************** Action Adventure Game *******************

# Requirement:
# 1. There are some Characters in the game.
# 2. Each character can use one kind of weapon
# 3. Character can change their weapon during the game.


#Define interface classes for weapon behavier

from abc import ABCMeta, abstractmethod

class WeaponBehavier():
	__metaclass__  = ABCMeta

	@abstractmethod
	def useWeapon(self):
		pass


#Define weapon behavier subclass
class KnifeBehavier(WeaponBehavier):

	def __init__(self):
		print("####### initiate knife behavier ########")

	def useWeapon(self):
		print("Using knife to cut something!...")


class BowAndArrowBehavier(WeaponBehavier):

	def __init__(self):
		print("####### initiate bow and arrow behavier ########")

	def useWeapon(self):
		print("Bow and arrow aim at remote destination!...")


class AxeBehavier(WeaponBehavier):

	def __init__(self):
		print("####### initiate axe behavier ########")

	def useWeapon(self):
		print("Using axe to chop something!...")


class SwordBehavier(WeaponBehavier):

	def __init__(self):
		print("####### initiate sword behavier ########")

	def useWeapon(self):
		print("Using sword to stab something!...")


#Define base class for character
class Character(WeaponBehavier):

	def __init__(self):
		self.weapon = None

	def fight(self):
		self.weapon.useWeapon()

	def setWeapon(self, weapon):
		self.weapon =  weapon


class King(Character):

	def __init__(self):
		print("I am a King!")
		self.weapon = BowAndArrowBehavier()


class Queen(Character):

	def __init__(self):
		print("I am a Queen!")
		self.weapon = KnifeBehavier()


class Troll(Character):

	def __init__(self):
		print("Troll is useful!")
		self.weapon = AxeBehavier()


class Knight(Character):

	def __init__(self):
		print("I am a knight!")
		self.weapon = SwordBehavier()



if __name__ == '__main__':
	king = King()
	king.fight()
	king.setWeapon(SwordBehavier())
	king.fight()

	queen = Queen()
	queen.fight()
	queen.setWeapon(BowAndArrowBehavier())
	queen.fight()

	troll = Troll()
	troll.fight()

	knight = Knight()
	knight.fight()