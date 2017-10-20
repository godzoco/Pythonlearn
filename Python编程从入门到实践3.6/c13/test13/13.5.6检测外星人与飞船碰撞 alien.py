import sys
import pygame
from pygame.sprite import Group

#pygame.sprite.Group类 类似于列表 提供额外功能 

#最新的ship文件是重构的3个实参，现在用2个 所以直接使用了ship1241的类Ship1241
from settings1341 import Settings1341
from ship1265 import Ship1265

import game_functions1356 as gf

from alien1341 import Alien1341

def run_game():
# 初始化游戏并创建一个屏幕对象
    pygame.init()
    #初始化init 初始化背景
    
    ai_settings = Settings1341()
    screen = pygame.display.set_mode(
     (ai_settings.screen_width,
     ai_settings.screen_height)                                   
                                   )
    

    #screen = pygame.display.set_mode((1200, 800))
    #这个就直接写在Settings 类中了
    #screen = pygame.display.set_mode((1200, 800))
    
    pygame.display.set_caption("爆炸打大佬")
    
    #新加入的
    ship = Ship1265(ai_settings,screen)
    
    bullets = Group()
    aliens = Group()
    #加外星人 群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # 设置背景色
    #bg_color = (230, 230, 230)
    #每一个 飞机 等元素 都是一个surface,不停循环绘制这个surface

    
# 开始游戏的主循环
    #游戏所以的事件,鼠标键盘的运动 移动 都是事件 找到这些事件 ，就是执行
    while True:
        gf.check_events(ai_settings, screen, ship,bullets)
        #1262不断右一直移动 就是加入这个ship.update
        ship.update()
        gf.update_bullets(ai_settings, screen, ship,aliens,bullets)
        #外星人移动
        gf.update_aliens(ai_settings,ship,aliens) 
        gf.update_screen(ai_settings, screen, ship,aliens,bullets)
        
        
        
run_game()




