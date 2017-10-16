import sys
import pygame
'''
def check_events():
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                #event.type == pygame.QUIT: 就是点击了关闭按钮
            sys.exit()
'''          
def check_events(ship):
    """鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                #event.type == pygame.QUIT: 就是点击了关闭按钮
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.Key == pygame.K_RIGHT:
                #向右移动 飞船
                ship.rect.centerx += 1
        
def update_screen(ai_settings, screen, ship):
    """更新屏幕内容，切换到新的屏幕"""
    # 每次循环都绘制屏幕
    screen.fill(ai_settings.bg_color)
    
    ship.blitme()
    pygame.display.flip()
