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
		vivod = (" ")*20+self.owner + "'s "+self.pokename+"'s hp:    "+ str(self.hp)
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
		self.roar = 'Cha..mA..DER!'
		
		self.punch1 = 'Fire tail'
		self.punch1power=25
		self.punch1cost = 25
		
		self.punch2 = 'Fire blast'
		self.punch2power=30
		self.punch2cost = 30
		self.heal =10
		self.healcost = 20
		self.hp=70
		self.maxhp=70
		
class Charmeleon (Pokemon): 
	def __init__(self):
		self.pokename ='Charmeleon'
		self.chosen ='You shouted:   Charmeleon, i choose you !!!!!!'
		self.npc = 'Enemy chose Charmeleon '
		self.roar = 'Charry-charry!'
		
		self.punch1 = 'Dragon Rage'
		self.punch1power=30
		self.punch1cost = 30
		
		self.punch2 = 'Fire breath'
		self.punch2power=35
		self.punch2cost = 35
		self.heal =10
		self.healcost = 20
		self.hp=100
		self.maxhp=100
		
class Charizard (Pokemon): 
	def __init__(self):
		self.pokename ='Charizard'
		self.chosen ='You shouted:   Charizard, i choose you !!!!!!'
		self.npc = 'Enemy chose Charizard '
		self.roar = 'Cha..ri..ZARD!'
		
		self.punch1 = 'Fire tail'
		self.punch1power=35
		self.punch1cost = 35
		
		self.punch2 = 'Fire blast'
		self.punch2power=40
		self.punch2cost = 40
		self.heal =15
		self.healcost = 30
		self.hp=150
		self.maxhp=150						

class Pichu (Pokemon): 
	def __init__(self):
		self.pokename ='Pichu'
		self.chosen ='You shouted:   Pichu, i choose you !!!!!!'
		self.npc = 'Enemy chose Pichu '
		self.roar = 'CHU!'
		
		self.punch1 = 'Electric tornado'
		self.punch1power=25
		self.punch1cost = 25
		
		self.punch2 = 'Light flash'
		self.punch2power=30
		self.punch2cost = 30 
		self.heal =5
		self.healcost = 5
		self.hp=50
		self.maxhp=50
		
class Pikachu (Pokemon): 
	def __init__(self):
		self.pokename ='Pikachu'
		self.chosen ='You shouted:   Pikachu, i choose you !!!!!!'
		self.npc = 'Enemy chose Pikachu '
		self.roar = 'Pika... CHU!'
		
		self.punch1 = 'Thunder tail'
		self.punch1power=30
		self.punch1cost = 30
		
		self.punch2 = 'ThunderPunch'
		self.punch2power=35
		self.punch2cost = 35
		self.heal =10
		self.healcost = 20
		self.hp=80
		self.maxhp=80
		
class Raichu (Pokemon): 
	def __init__(self):
		self.pokename ='Raichu'
		self.chosen ='You shouted:   Raichu, i choose you !!!!!!'
		self.npc = 'Enemy chose Raichu '
		self.roar = 'RAY!'
		
		self.punch1 = 'Quick attack'
		self.punch1power=30
		self.punch1cost = 30
		
		self.punch2 = 'Thunderstorm'
		self.punch2power=40
		self.punch2cost = 40 
		self.heal =15
		self.healcost = 20
		self.hp=120
		self.maxhp=120					
		
class Bulbasaur (Pokemon):
		def __init__(self):
			self.pokename ='Bulbasaur'
			self.chosen ='You shouted:   Bulbasaur, i choose you !!!!!!'
			self.npc = 'Enemy chose Bulbasaur '
			self.roar = 'Bolbaa...sauur!'
		
			self.punch1 = 'Deadly creepers'
			self.punch1power=20
			self.punch1cost = 20
		
			self.punch2 = 'Grass choking'
			self.punch2power=25
			self.punch2cost = 25
			self.heal =10
			self.healcost = 20
			self.hp=100
			self.maxhp=100
		

class Ivysaur (Pokemon):
		def __init__(self):
			self.pokename ='Ivysaur'
			self.chosen ='You shouted:   Ivysaur, i choose you !!!!!!'
			self.npc = 'Enemy chose Ivysaur '
			self.roar = 'I-i-i-ivysaaaauur!'
		
			self.punch1 = 'Green ball'
			self.punch1power=25
			self.punch1cost = 25
		
			self.punch2 = 'Floral scent'
			self.punch2power=30
			self.punch2cost = 30
			self.heal =15
			self.healcost = 30
			self.hp=150
			self.maxhp=150
			
class Venusaur (Pokemon):
		def __init__(self):
			self.pokename ='Venusaur'
			self.chosen ='You shouted:   Venusaur, i choose you !!!!!!'
			self.npc = 'Enemy chose Venusaur '
			self.roar = 'VE...NU...SA...UR!'
		
			self.punch1 = 'Flower disputes'
			self.punch1power=30
			self.punch1cost = 30
		
			self.punch2 = 'Green flow'
			self.punch2power=35
			self.punch2cost = 35
			self.heal =20
			self.healcost = 35
			self.hp=200
			self.maxhp=200
			
class Squirtle (Pokemon):
		def __init__(self):
			self.pokename ='Squirtle'
			self.chosen ='You shouted:   Squirtle, i choose you !!!!!!'
			self.npc = 'Enemy chose Squirtle '
			self.roar = 'Squi-squi!'
		
			self.punch1 = 'Water gun'
			self.punch1power=15
			self.punch1cost = 15
		
			self.punch2 = 'Skill bash'
			self.punch2power=25
			self.punch2cost = 25
			self.heal =5
			self.healcost = 10
			self.hp=80
			self.maxhp=80
			
class Wartotle (Pokemon):
		def __init__(self):
			self.pokename ='Wartotle'
			self.chosen ='You shouted:   Wartotle, i choose you !!!!!!'
			self.npc = 'Enemy chose Wartotle'
			self.roar = 'War...tootle!'
		
			self.punch1 = 'Tackle'
			self.punch1power=20
			self.punch1cost = 20
		
			self.punch2 = 'Bubble beam'
			self.punch2power=30
			self.punch2cost = 30
			self.heal =15
			self.healcost = 20
			self.hp=110
			self.maxhp=110
			
class Blastoise (Pokemon):
		def __init__(self):
			self.pokename ='Blastoise'
			self.chosen ='You shouted:   Blastoise, i choose you !!!!!!'
			self.npc = 'Enemy chose Blastoise '
			self.roar = 'Blasty!'
		
			self.punch1 = 'Hydro pump'
			self.punch1power=25
			self.punch1cost = 25
		
			self.punch2 = 'Pain rain'
			self.punch2power=35
			self.punch2cost = 35
			self.heal =15
			self.healcost = 25
			self.hp=150
			self.maxhp=150			
