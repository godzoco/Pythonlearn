import pygame.font
#导入pygame.font模块 把 文本渲染到 屏幕上
class Button():

    def __init__(self, ai_settings, screen, msg):
        """初始化按钮的属性. 接受对象ai_settings, screen, msg"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # 设置按钮尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)#对象为绿色
        self.text_color = (255, 255, 255) #文本为白色
        #导入pygame.font模块 把 文本渲染到 屏幕上
        self.font = pygame.font.SysFont(None, 48)
        
        # 用rect 使对象居中  设置按钮的对象为rect
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # 按钮的标签只需要一次. 把字符串渲染成图片来处理文本 调prep_msg()
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将MSG渲染为图像，且在按钮上居中"""
        #font.render 将文本存为图片
        self.msg_image = self.font.render(msg, True, self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        # 绘制1个用颜色填充的按钮，再绘制文本   draw_button（）显示 这个按钮到屏幕上
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
