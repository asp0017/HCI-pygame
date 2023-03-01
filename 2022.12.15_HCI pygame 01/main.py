import sys
import pygame
from pygame.locals import *

pygame.init()
screen_size = width, height = 1000, 700 #全螢幕
bg =  (255, 255, 255)
speed = [1, 0] 

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("HCI_Project") 		#調用image子模塊的load函數，返回一個對象，起名字爲heroPlane.
heroPlane = pygame.image.load("circular-arrow_small.png")			 #獲取圖像所在的矩形區域rect對象（圖像左上角的座標，圖像大小width*height），總是以（0,0）爲起點。
position = heroPlane.get_rect()				# rect是用來存儲矩形座標的pygame對象，相當於一個優盤。

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	#調用move()函數移動圖像，返回值仍爲rect對象，並再次賦值給position
	position = position.move(speed)
	screen.fill(bg)
	#使用更新後的position繪製對象
	screen.blit(heroPlane, position)
	pygame.display.flip()
