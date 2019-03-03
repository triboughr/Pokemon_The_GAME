import pygame
import sys
from Pokemon_The_GAME import *
from pokemons import *
pygame.init()

screen = pygame.display.set_mode()
clock = pygame.time.Clock()
background_image = pygame.image.load('.background.png')
background_image=pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))

class Button():
	def __init__(self, screen, left, top, width, height, picture, text, outpt):
		
		self.rectngl = pygame.Rect(left, top, width, height)
		self.text = text
		self.outpt = outpt		
		self.btn_image = pygame.image.load(picture)
		self.btn_image = pygame.transform.scale(self.btn_image,(width, height) )
		self.outpt=outpt
		pygame.draw.rect(screen, 1234 ,self.rectngl)

	def pressed(self, anyevent):
		if pygame.mouse.get_focused() == True and  self.rectngl.collidepoint(pygame.mouse.get_pos())==True and anyevent.type == pygame.MOUSEBUTTONDOWN:
			return self.outpt()
mouse_cursor = pygame.image.load('.Pokeball.PNG')
mouse_cursor=pygame.transform.scale(mouse_cursor, (50,50))
pygame.mouse.set_visible(False)
btn = Button(screen, 100, 100, 100, 100, '.pergament.jpg', 'nnnm', game)

while True:
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		btn.pressed(i)
	screen.blit(background_image, (0, 0))
	screen.blit(btn.btn_image, (btn.rectngl.left,btn.rectngl.top))
	mouse_x, mouse_y = pygame.mouse.get_pos()
	screen.blit(mouse_cursor, (mouse_x-25,mouse_y-25))
	pygame.display.update()
	clock.tick(60)
