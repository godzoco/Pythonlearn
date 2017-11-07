class GameStats():
    """跟踪游戏的统计信息."""
    
    def __init__(self, ai_settings):
        """初始化 统计信息."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start Alien Invasion in an active state.
        self.game_active = True
        
    def reset_stats(self):
        """初始化可能变动的信息."""
        self.ships_left = self.ai_settings.ship_limit
