import sys
import pygame

background_image_filename = "images/background.jpg"  


#最新的ship文件是重构的3个实参，现在用2个 所以直接使用了ship1241的类Ship1241
from settings1264 import Settings1264
from ship1265 import Ship1265

import game_functions1263 as gf

def run_game():
# 初始化游戏并创建一个屏幕对象
    pygame.init()
    #初始化init 初始化背景
    
    ai_settings = Settings1264()
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
    
    # 设置背景色
    #bg_color = (230, 230, 230)
    #每一个 飞机 等元素 都是一个surface,不停循环绘制这个surface

# 开始游戏的主循环
    #游戏所以的事件,鼠标键盘的运动 移动 都是事件 找到这些事件 ，就是执行
    while True:
        gf.check_events(ship)
        #1262不断右一直移动 就是加入这个ship.update
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        
run_game()




