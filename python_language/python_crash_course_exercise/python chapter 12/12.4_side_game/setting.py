class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0) # black

        # Ship settings
        self.ship_limit = 3
        self.ship_speed = 4

        # Bullet settings
        self.bullet_width = 18
        self.bullet_height = 3
        self.bullet_color = (0, 183, 250)
        self.bullets_allowed = 4
        self.bullet_speed = 5

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represent right ; -1 represent left
        self.fleet_direction = 1
