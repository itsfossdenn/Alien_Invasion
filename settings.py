class Settings:
    def __init__(self):
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        # ship settings
        self.ship_speed = 2
        # laser bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 0, 0)
        self.bullets_allowed = 5