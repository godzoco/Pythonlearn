class GameStats():
    """跟踪游戏的统计信息."""
    
    def __init__(self, ai_settings):
        """初始化 统计信息."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # 让游戏开始时 是静止状态
        self.game_active = False
        #让游戏运行之后 开始时是静止的
        
        #在任何情况下都不能重置最高分数
        self.high_score = 0
    def reset_stats(self):
        """初始化可能变动的信息."""
        self.ships_left = self.ai_settings.ship_limit
        self.score=0
        #加入等级
        self.level=1
        
        #1431初始等分为0
        
        
