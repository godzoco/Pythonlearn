class Settings2():
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
        
        #飞船3条命的 船
        self.ship_limit = 3

        # Bullet settings.这下面就是加入的子弹
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 250, 0, 0
        
        #这个限制同时出现3个子弹
        self.bullets_allowed = 30
        
        #外星人人设置
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 10
        #设置向 右移动 为1
        self.fleet_direction = 10
        #1421加入修改速度
        self.speedup_scale = 1.1
        #再加入高难度之后，加高分值
        self.score_scale = 1.5
        
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor =  3
        self.alien_speed_factor =1
                    
        #向右的速度  1为向右
        self.fleet_direction = 1
        
        #记分 1433
        self.alien_points = 50
        
    def increase_speed(self):
        #加高速度和外星人点数
        self.ship_speed_factor *=self.speedup_scale
        self.bullet_speed_factor *=self.speedup_scale
        self.alien_speed_factor *=self.speedup_scale
        
        self.alien_points=int(self.alien_points * self.score_scale)
        
        
     
        

