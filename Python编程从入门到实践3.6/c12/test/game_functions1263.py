import sys

import pygame

def check_events(ship):
    """鼠标事件 126 这里加入ship 调用ship"""
    
    #加入elif event.type == pygame.KEYDOWN:
    #判断按键 如果按了 向右就向右 滑动
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                #event.type == pygame.QUIT: 就是点击了关闭按钮
            sys.exit()
            '''这个地方 注意 1262加入 一直移动到后边时 这个要去掉
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1
            '''
            #这个down 就是键盘 按键一直按下去的意思  按下去 就判断 左右  左 就左一直走 右 就 右一直走
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
                         
def update_screen(ai_settings, screen, ship):
    """更新屏幕内容，切换到新的屏幕"""
    # 每次循环都绘制屏幕
    screen.fill(ai_settings.bg_color)
    
    ship.blitme()
    pygame.display.flip()