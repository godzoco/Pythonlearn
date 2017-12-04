import sys

import pygame

from bullet import  Bullet
from alien1341 import  Alien1341

from time import sleep
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

def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)
def check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    "点击开始play按钮开始游戏"
    "再次点击的时候PLAY 开始新的游戏"
    
    
    #这里加入 一条判断 让只有 游戏 关闭的时候 才能使用 play按键  为非活动状态
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #再加入隐藏光标
        #加入1421新开始程序速度变快
        ai_settings.initialize_dynamic_settings()
        
        
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        
        #重置游戏统计信息
        stats.game_active = True   #这样游戏开始 
        #清空外星人列表和子弹
        aliens.empty()

        bullets.empty()
        #加新的外星人，并让飞船居中
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        
        #然后再去修改 check_events
                
def ship_hit(ai_settings, stats,screen, ship,aliens,bullets):
     #响应 外星人撞到飞船  飞船数量减1
    if stats.ships_left > 0:
        stats.ships_left -= 1
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
     #清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()
     
     #创建一群新的外星人，并放飞船在中央
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
    
    #暂停
    sleep(0.5)
    
    
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
                                 
def update_screen(ai_settings, screen,stats,sb ,ship,aliens,bullets,play_button):
    """更新屏幕内容，切换到新的屏幕"""
    # 每次循环都绘制屏幕
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    
    #加入显示外星人
    aliens.draw(screen)
    
    sb.show_score()
        #非活动时出现play 按键
    if not stats.game_active:
        play_button.draw_button()
     
     
        
    pygame.display.flip()
    
    #检测外星人和飞船碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings, stats,screen,ship,aliens,bullets)
    
    

    
    
    
    
def update_bullets(ai_settings, screen,ship,aliens,bullets):
    bullets.update()
        #加入函数 删除  已经出去屏幕的 子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen,ship,aliens,bullets)
    
def check_bullet_alien_collisions(ai_settings, screen,ship,aliens,bullets):    
    
    collisions=pygame.sprite.groupcollide(bullets, aliens, True,True)
    
    if len(aliens) == 0:
        #删除子弹建新的外星人群
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen,ship,aliens)
    #检测是否击中了外星人
    #击中了就删除子弹和这个外星人
            
def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
        
def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet, and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    """
    Check if the fleet is at an edge,
      then update the postions of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
        
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)    
                   
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
    alien = Alien1341(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien, and find number of aliens in a row.
    alien = Alien1341(ai_settings, screen)
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