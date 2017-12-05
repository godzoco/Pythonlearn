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
        self.font= pygame.font.SysFont(None,48)
     
     #准备初始的图像
        self.prep_score()
        
        #显示的是文本，导入了字体的模块，设置字体颜色，实例化一个对象
        #然后用 这个字体，转化成图像
        
        #上面的是当前得分，下面的是最高得分
        self.prep_high_score()
        
        self.prep_level()
        
    def prep_score(self):
        """将得分渲染成图像"""
        
        #1436将显示的分数 做分位的 处理
        #round()设置参数 设置成正就是精确小数，设置成负数，就是化最近的10 100 1000倍数
   
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
        self.ai_settings.bg_color)
        
        
        score_str = str(self.stats.score)
        self.score_imge = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        
        #将得分放在屏幕右上角
        self.score_rect = self.score_imge.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
        #在prep_score() 把sstats.score 变成字符串 传给 创建图像的render
        
        #用一个rect 在屏幕右边相聚20像素 锚定在屏幕右边  创建方法show_score()用于渲染好的 得分图像
        
        
        
        
        
        
        
        
        
    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
        self.ai_settings.bg_color)
        
        
        
        
        #将得分放在屏幕右上角    最高分在最中间
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def show_score(self):
        '''屏幕显示得分'''
        self.screen.blit(self.score_imge,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
    def prep_level(self):
        '''将等级转化渲染成图像'''
        self.level_image = self.font.render(str(self.stats.level),True,self.text_color,
            self.ai_settings.bg_color)    
        
        #将等级放在得分下面
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def show_score(self):
        """在屏幕上显示飞机和得分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    