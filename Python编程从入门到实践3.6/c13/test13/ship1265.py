import pygame

class Ship1265():
    #1264加入ai_settings 来控制加入的 速度
    def __init__(self,ai_settings,screen):
        """初始化飞船且设置启动初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船且获取其外接矩形
        self.image = pygame.image.load('../images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect =self.screen.get_rect()

        #放每个船在中间  和最底部
        #如果这2条 都注释 就会直接到最左上角 为原点 0 0
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
       #Ship类的方法 接2个参数 SCREEN决定 飞船飞到什么地方
       #加载pygame.image.load 得到这个飞船的surface 存储到image
       
       #image.get_rect得到了相应元素的rect对象
       #rect 对象可以 上下左右来定位 bottom center
       
       #在pygame 原点在屏幕左上角， 右下角坐标值 慢慢增大 1200*800中 右下角坐标（1200,800）
       
       
       
       
       #在飞机 属性 center 中存储最小值 rect.centerx只能 存储 整数值
        self.center = float(self.rect.centerx)
       #移动标志
       #加入 2个 是左右的移动
        self.moving_right = False
        
        self.moving_left = False
    def update(self):
        """根据移动标志 调整飞船的位置"""
        """按住右键 不放 就一直 向右进行移动"""
        #不是一直 按住 就是 按一下走 一下
        """设置距离限制 超过范围不动了"""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # Update rect object from self.center.
        self.rect.centerx = self.center
            
         #更新rect对象  更新到最新的值 速度
        self.rect.centerx = self.center   
    def blitme(self):
        """在指定位置绘制船"""
        self.screen.blit(self.image, self.rect)
    def center_ship(self):    
        #在屏幕上 飞机上居中
        self.center = self.screen_rect.centerx 