import pygame.font


class Scoreboard():
    """显示分类信息."""
    
    def __init__(self, ai_settings,screen,stats):
        """初始化 统计信息."""
        self.screen=screen
        self.screen_rect = screen.get_rect()
        self.ai_settings= ai_settings
        self.stats = stats
        #显示得分信息使用的字体设置
        
        self.text_color = (30,30,30)
        self.font= pygame.font.SysFont(none,48)
     
     #准备初始的图像
        self.prep_score()
        
        #显示的是文本，导入了字体的模块，设置字体颜色，实例化一个对象
        #然后用 这个字体，转化成图像
        
    def prep_score(self):
        """将得分渲染成图像"""
        score_str = str(self.stats.score)
        self.score_imge = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        
        #将得分放在屏幕右上角
        self.score_rect = self.score_imge.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
        #在
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    