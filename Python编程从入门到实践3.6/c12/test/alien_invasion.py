import sys
import pygame


def run_game():
    pygame.init()
    # Start the main loop for the game.屏幕
    screen=pygame.display.set_mode((600,500))
    #打飞机
    pygame.display.set_caption('打飞机')
    
    while True:
       #监视鼠标事件
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               sys.exit()
               
    pygame.display.flip()
run_game()
