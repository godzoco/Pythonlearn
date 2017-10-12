import sys
import pygame


from settings import Settings

def run_game():
# 初始化游戏并创建一个屏幕对象
    pygame.init()
    #初始化init 初始化背景
    
    ai_settings = Settings()
    screen = pygame.display.set_mode(
     (ai_settings.screen_width,
     ai_settings.screen_height)                                   
                                   )
    

    #screen = pygame.display.set_mode((1200, 800))
    #这个就直接写在Settings 类中了
    #screen = pygame.display.set_mode((1200, 800))
    
    pygame.display.set_caption("爆炸打大佬")
    
    # 设置背景色
    #bg_color = (230, 230, 230)
    #每一个 飞机 等元素 都是一个surface,不停循环绘制这个surface

# 开始游戏的主循环
    #游戏所以的事件,鼠标键盘的运动 移动 都是事件 找到这些事件 ，就是执行
    while True:
# 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #event.type == pygame.QUIT: 就是点击了关闭按钮
                sys.exit()
    # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        #这样 加入了 上面的 230 之后 就是空屏幕变成了 灰白色了
        #这里 只接受 一个实参
                
    #有新的事件加入，不停刷新 显示出这些新的元素 和事件的 变化
        
        pygame.display.flip()

run_game()




