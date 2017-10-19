import sys

import pygame

from bullet import  Bullet
from alien1321 import  Alien1321
# 对编组bullets调用update() 时，自动对所有精灵调用 把编组遍历出的bullet 都update()一次
def check_keydown_events(event, ai_settings, screen,ship,bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:    
        fire_bullet(ai_settings, screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def fire_bullet(ai_settings, screen,ship,bullets):       
        #加入空格键功能 开火 按了空格键，新建一个子弹 ，然后add 增加到bullets 这个编组里面
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
            
                         
def update_screen(ai_settings, screen, ship,aliens,bullets):
    """更新屏幕内容，切换到新的屏幕"""
    # 每次循环都绘制屏幕
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    
    #加入显示外星人
    aliens.draw(screen)
    
    pygame.display.flip()
    
    
    
    
    
    
def update_bullets(bullets):
    bullets.update()
        #加入函数 删除  已经出去屏幕的 子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
            
            
def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
    
def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
    
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien, and place it in the row."""
    alien = Alien1321(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien, and find number of aliens in a row.
    alien = Alien1321(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)
    
    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                row_number)
"""            
def get_number_aliens_x(ai_settings,alien_width):        
    #计算可以容纳多少外星人
    available_space_x = ai_settings.screen_width - 2 * alien_width   
    number_aliens_x=int(available_space_x/(2 * alien_width)) 
    return number_aliens_x

def create_alien(ai_settings, screen, aliens,alien_number):   
    #创建一个外星人并放在当前行
    alien = Alien1321(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x=alien_width + 2 * alien_width * alien_number
    ailen.rect.x=alien.x
    aliens.add(alien)
    
    
    
def create_fleet(ai_settings, screen, aliens):            
    alien = Alien1321(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens,alien_number)
"""         