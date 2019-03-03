from time import sleep
from random import choice
from random import randint
from pokemons import *
import pygame
import sys
pygame.init()
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
		shwhp(player1,player2)
		print ('Your energy:      ', mana)
		
		if mana >= player1.punch1cost:
			stroka = 'to use ' + player1.punch1 + ' (-' + str(player1.punch1power) + ' hp, '+str(player1.punch1cost)+ ' energy) press "1"'
			print(stroka)
		
		if mana >= player1.punch2cost and perem == 0:
			stroka = 'to use ' + player1.punch2 + ' (-' + str(player1.punch2power) + ' hp, '+str(player1.punch2cost) +' energy) press "2"'
			print(stroka)
		
		if player1.hp < player1.maxhp and mana>=player1.healcost:
			stroka = 'to heal (+'+str(player1.heal) +' hp, '+str(player1.healcost)+' energy) your pokemon press "3"'
			print(stroka)
			
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
		print("YOU LOSE")
		
	if player2.hp <=0:
		player2.hp  = 0
		player2.showhp()
		print ('YOU WIN')

def game():	
	
	screen = pygame.display.set_mode()
	clock = pygame.time.Clock()
	background_image = pygame.image.load('.background.png')
	background_image=pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))
	mouse_cursor = pygame.image.load('.Pokeball.PNG')
	mouse_cursor=pygame.transform.scale(mouse_cursor, (50,50))
	pygame.mouse.set_visible(False)
	
	sleep(0.5)
	menu()
	loading()
	a=input('choose your fighter: Pikachu [p] or Charmander [c]:    ')
	if a=='c':
		player1 = Charmander()
		player2 = Pikachu()
	if a=='p':
		player1 = Pikachu()
		player2 = Charmander()
	player1.catched()
	sleep(0.5)
	player1.player()
	sleep(1)
	
	player2.owner = 'NPC'
	player2.deviant()

	loading()
	battle(player1,player2)
	
	
	
#game()
sleep(10)
