import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship.加入子弹类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船的位置加入子弹"""
        #super(Bullet, self).__init__() 这个是2.7写法  下面 3.0写法 如下
        super().__init__()
        self.screen = screen
    
#class Foo():   一个子类继承的举例
#    def __init__(self, frob, frotz)
#        self.frobnicate = frob
#        self.frotz = frotz

#class Bar(Foo):
#    def __init__(self, frob, frizzle)
#        super().__init__(frob, 34)
#        self.frazzle = frizzle

        # 先在0.0这里生成一个矩形，然后再设置正确的位置.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # 存储用小数表示子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        #这里子弹 并不是图像 必须用 pygame.rect() 从空白创建一个矩形，
        #这个 实例必须提供左上角的 X Y 坐标  以及 这个 子弹的这个 长度和宽度 从settings 里面获得
        
        #rect.centerx 是子弹从飞船中间发出
        #rect.top 是子弹从飞船顶部上面发出
        
    def update(self):
        """向上移动子弹."""
        # 表示子弹位置的小数值. 依次往上走单位值            子弹的射击速度
        self.y -= self.speed_factor
        # 表示 rect 位置. 和飞船的位置一致
        self.rect.y = self.y

    def draw_bullet(self):
        """屏幕上绘制子弹."""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        #用draw.recct() 使得在self.color中的颜色填充表示rect 占据屏幕的部分
