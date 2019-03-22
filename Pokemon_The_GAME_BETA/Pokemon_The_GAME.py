from time import sleep
from random import choice
from random import randint
from pokemons import *
import sys

def cutscena(tekst):
	f = open(tekst, 'r')
	for i in f:
		print(i)
		sleep(1.7)
	f.close()
	
def menu():
	
	print('if you want to play enter "play"')
	sleep(0.5)
	print('if you want to close this game enter "exit"')
	sleep(1)
	a = input('enter here:    ')
	if a == "exit":
		exit(0)
		
def shwhp(player1,player2):
	player1.showhp()
	player2.showhp()

def playerpunch(player1,player2, mana):
	a='smth'
	perem = 0
	while mana>= player1.punch1cost and a!='stop':
		print(' ')
		shwhp(player1,player2)
		print ('                    Your energy:      ', mana)
		print('  ')
		if mana >= player1.punch1cost:
			stroka = 'to use ' + player1.punch1 + ' (-' + str(player1.punch1power) + ' hp, '+str(player1.punch1cost)+ ' energy) press "1"'
			print(stroka)
			sleep(1)
		if mana >= player1.punch2cost and perem == 0:
			stroka = 'to use ' + player1.punch2 + ' (-' + str(player1.punch2power) + ' hp, '+str(player1.punch2cost) +' energy) press "2"'
			print(stroka)
			sleep(1)
		if player1.hp < player1.maxhp and mana>=player1.healcost:
			stroka = 'to heal (+'+str(player1.heal) +' hp, '+str(player1.healcost)+' energy) your pokemon press "3"'
			print(stroka)
			sleep(1)
			
		print('If you want to end your attack enter "stop"')
		sleep(3)
		a = input('enter your attack please:  ')
		sleep(1)
		
		if a == '1' and mana >= player1.punch1cost:
			mana+=-1*player1.punch1cost
			player2.hpchange(player1.punchone())
			
		if a == '2' and mana >= player1.punch2cost and perem==0:
			mana+=-1*player1.punch2cost
			player2.hpchange(player1.punchtwo())
			perem=1
			
		if a=='3' and player1.hp < player1.maxhp and mana>=player1.healcost: 
			mana+=-1*player1.healcost
			player1.healing()
			
	print('your attack ended')
	
def npcpunch(player1,player2):

	if player2.hp >= 0.8*player2.maxhp:
		a=[1, 2]
		
	if player2.hp < 0.8*player2.maxhp and player2.hp>0.4*player2.maxhp:
			a=[2]
			
	if player2.hp<= 0.4*player2.maxhp:
		a = [1,2,3,3,3,3]
		
	i=choice(a)
	
	if i ==1:
		player1.hpchange(player2.punchone())
		
	if i ==2:
		player1.hpchange(player2.punchtwo())
		
	if i ==3:
		player2.healing()

def loading():
	for i in range(randint(1,6)):
		print('loading...')
		sleep(1)
def battle(player1,player2):
	
	counter=0
	mana = player1.punch1cost
	
	while player1.hp > 0 and player2.hp>0:
		
		if counter%2 == 0:
			
			if mana > player1.healcost+player1.punch1cost :
				mana = player1.healcost+player1.punch1cost
			playerpunch(player1,player2,mana)
			mana += 10
		
		if counter%2 == 1:
			npcpunch(player1,player2)
		
		sleep(1)
		counter +=1

	if player1.hp <= 0 :
		player1.hp = 0
		player1.showhp()
		print("                 YOU LOSE")
		cutscena('lose.txt')
		sleep(5)
		sys.exit()
		
	if player2.hp <=0:
		player2.hp  = 0
		player2.showhp()
		print ('                  YOU WIN')

def game():	
	
	sleep(0.5)
	menu()
	loading()
	cutscena('1.txt')
	loading()
	a=input('choose your fighter: Pichu [p] or Charmander [c] or Squirtle [s] or Bulbasaur [b]:    ')
	if a=='c':
		player1 = Charmander()
		player1_2=Charmeleon()
		player1_3 = Charizard()
		player2 = Pichu()
		player2_2 = Ivysaur()
		player2_3 = Blastoise()
	elif a=='p':
		player1 = Pichu()
		player1_2=Pikachu()
		player1_3=Raichu()
		player2 = Charmander()
		player2_2 = Wartotle()
		player2_3 = Venusaur()
	elif a=='s':
		player1 = Squirtle()
		player1_2=Wartotle()
		player1_3 = Blastoise()
		player2 = Bulbasaur()
		player2_2 = Pikachu()
		player2_3 = Charizard()
	elif a=='b':
		player1 = Bulbasaur()
		player1_2 = Ivysaur()
		player1_3 = Venusaur()
		player2 = Squirtle()		
		player2_2 = Charmeleon()
		player2_3 = Raichu()
	player1.catched()
	sleep(0.5)
	cutscena('2.txt')
	loading()
	player1.player()
	sleep(1)
	
	player2.owner = 'Disintegrator'
	player2.deviant()

	loading()
	battle(player1,player2)
	cutscena('3.txt')
	print('your pokemon evolved in   ', player1_2.pokename)
	
	loading()
	print('the nex battle begins.... NOW')
	sleep(1)
	player1_2.owner = player1.owner
	player2_2.owner = 'Jess'
	player2_2.deviant()
	battle(player1_2,player2_2)
	cutscena('4.txt')
	
	
	print('your pokemon evolved in   ', player1_3.pokename)
	
	loading()
	print('the nex battle begins.... NOW')
	sleep(1)
	player1_3.owner = player1.owner
	player2_3.owner = 'Andrew'
	player2_3.deviant()
	battle(player1_3,player2_3)
	cutscena('5.txt')
game()
sleep(10)
