class Pokemon:
	
	def __init__ (self):
		self.pokename = 'Pokemon'
		self.owner = 'owner'
		self.roar = 'roar'
		
		self.punch1='punchone_name'
		self.punch1power = 0
		self.punch1cost = 0
		self.punch2='punchtwo_name'
		self.punch2power = 0
		self.punch2cost = 0
		self.hp = 100
		self.heal=0
		self.maxhp=100
		self.chosen = 'f'
		
	def catched(self):
		self.owner = input('enter your name please: ')
		vivod=self.owner+ " catched "+ self.pokename	
		
	def roaring(self):
		print(self.roar)
		
	def punchone(self):
		vivod=self.owner +"'s "+self.pokename  + ' use '+ self.punch1 
		print(vivod)
		print(self.roar)                           #заменить потом на аудио
		return int(self.punch1power)
		
	def punchtwo(self):
		vivod=self.owner +"'s "+self.pokename + ' use '+ self.punch2
		print(vivod)
		print(self.roar)                           #заменить потом на аудио
		return int(self.punch2power)
		
	def hpchange(self, m):
		self.hp +=-int(m)
		
	def showhp(self):
		vivod = self.owner + "'s "+self.pokename+"'s hp:    "+ str(self.hp)
		print(vivod)
		
	def player(self):
		print(self.chosen)
		
	def deviant(self):
		print(self.npc)
		
	def healing(self):
		vivod = self.owner+"'s " + self.pokename +" is being treated"
		print(vivod)
		self.hp+= self.heal
		
		
class Charmander (Pokemon):
	def __init__(self):
		self.pokename ='Charmander'
		self.chosen ='You shouted:   Charmander, i choose you !!!!!!'
		self.npc = 'Enemy chose Charmander '
		self.roar = 'Cha..mA..DER'
		
		self.punch1 = 'Fire tail'
		self.punch1power=20
		self.punch1cost = 20
		
		self.punch2 = 'Fire blast'
		self.punch2power=30
		self.punch2cost = 30
		self.heal =10
		self.healcost = 30
		self.hp=100
		self.maxhp=100

class Pikachu (Pokemon):
	def __init__(self):
		self.pokename ='Pikachu'
		self.chosen ='You shouted:   Pikachu, i choose you !!!!!!'
		self.npc = 'Enemy chose Pikachu '
		self.roar = 'Pika... CHU'
		
		self.punch1 = 'Thunder tail'
		self.punch1power=20
		self.punch1cost = 20
		
		self.punch2 = 'ThunderPunch'
		self.punch2power=40
		self.punch2cost = 40
		self.heal =20
		self.healcost = 40
		self.hp=100
		self.maxhp=100

