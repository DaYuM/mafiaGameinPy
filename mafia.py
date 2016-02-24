import random
import math
import simplegui

# consider that there are 10 people in a room and they would all like to play the game
# an instance would be creating the villagers first, then reassigning them to different status types
# do we only need to create one class object and then call other objects created onto it


village = [] #[#name: #type]
villageCasualty = [] #[#name:#type]
class Villager(Object):
	# define the class for the villager
	status = "alive"
	type = "villager"
	def __init__(self, name):
		self.name = name
		village[self.name] = self.type
	
	
	def initVote(townInput):
		trial = 
		
class Mafia(Villager):
	#define the mafia and create the functions for them to run on
	type = "mafia"
	def __init__(self, mafia):
		self.mafia = mafia
		village[self.name] = self.type
		
		
	def targetHit(Villager):
		mafiaCount = 0
		for townie in village:
			#select at random random.randint(1, 10)
			if townie.type = "mafia":
				mafiaCount+=1
			return mafiaCount
		#count the occurences of mafia
		
		
		#if there is 3 mafia 2 kills are allowed 
		if mafiaCount >= 3:
			killCount = 2
		elif mafiaCount =< 2 and mafiaCount > 0:
			killCount = 1
			
		# if there is 2 or less mafia 1 kill is allowed
		
	
	
	
class Vigil(Villager):
	#define the vigil and create formula to determine who the vigi is
	type = "vigilante"
	def __init__(self, vigi):
		self.vigi = vigi
		village[self.name] = self.type

class Medic(Villager):
	#
	type = "medic"
	count = 0
	
	def __init__(self, medic):
		self.medic = medic
		village[self.name] = self.type
	
	if count == 0:
		#random generate a medic player
		return count += 1
	else:
		#have maximum amount of medics
	
	
	
def villageVote(target, townInput):	
	# define a function to create a poll and gather the results and if its greater then 60% of people voting
	target = raw_input()
	tally = count("yes")
	tallyAverage = (tally/(5/3))/len(village)
	if tallyAverage >= .6:
		target.status = "dead"
		del village[target]
		print "Thanks for playing " + target
		

def statusType(villager):
	global mafiaCount
	global copCount
	global vigiCount
	global medicCount
	
	for i in village
		randi = random.randint(1, 4)
		if randi == 1:
			if mafiaCount > 0:
				village[i] = "Mafia" 
				mafiaCount =-
			else:
				village[i] = "Villager"
		elif randi == 2:
			if copCount > 0:
				village[i] = "Sheriff" 
				copCount =-
			else:
				village[i] = "Villager"
		elif randi == 3:
			if vigiCount > 0:
				village[i] = "Vigilante" 
				vigiCount =-
			else:
				village[i] = "Villager"
		elif randi == 4:
			if medicCount > 0:
				village[i] = "Medic" 
				medicCount =-
			else:
				village[i] = "Villager"
		else:
			village[i] = "Villager"
		
				
def villageCount(villa):
	global mafiaCount
	global vigiCount
	global copCount
	global medicCount
	townCount = villa.len()
	
	if villa.len() > 10:
		
	
	

	
		

