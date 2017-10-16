import pygame

class Ship1241():

    def __init__(self,screen):
        """初始化飞船且设置启动初始位置"""
        self.screen = screen

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
    def update(self):
        ''''''
    def blitme(self):
        """在指定位置绘制船"""
        self.screen.blit(self.image, self.rect)
