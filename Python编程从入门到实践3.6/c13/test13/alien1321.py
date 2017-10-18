import pygame
from pygame.sprite import Sprite

class Alien1321(Sprite):
    """单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """初始化 外星人并设置起始 位置"""
        #super(Alien, self).__init__()
        #3.0写法
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人的图像，且设置其rect属性.
        self.image = pygame.image.load('../images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人设置在屏幕 左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        
    
    def blitme(self):
        """显示出外星人."""
        self.screen.blit(self.image, self.rect)
