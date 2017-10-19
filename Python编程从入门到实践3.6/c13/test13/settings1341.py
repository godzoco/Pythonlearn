class Settings1341():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,206,209)
        #背景色  青色
        # Ship settings.
        self.ship_speed_factor = 1.5

        # Bullet settings.这下面就是加入的子弹
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 250, 0, 0
        
        #这个限制同时出现3个子弹
        self.bullets_allowed = 3
        
        #外星人人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #设置向 右移动 为1
        self.fleet_direction = 1
        

