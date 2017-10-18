import sys

import pygame

from bullet import  Bullet

# 对编组bullets调用update() 时，自动对所有精灵调用 把编组遍历出的bullet 都update()一次
def check_keydown_events(event, ai_settings, screen,ship,bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        
        #加入空格键功能 开火 按了空格键，新建一个子弹 ，然后add 增加到bullets 这个编组里面
    elif event.key == pygame.K_SPACE:
        if len(bullets)<ai_settings.bullets_allowed:
        #创建一个子弹 ，加入编组 bullets中
            new_bullet =Bullet(ai_settings, screen,ship)
            bullets.add(new_bullet)
        
def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen,ship,bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
                         
def update_screen(ai_settings, screen, ship,bullets):
    """更新屏幕内容，切换到新的屏幕"""
    # 每次循环都绘制屏幕
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()