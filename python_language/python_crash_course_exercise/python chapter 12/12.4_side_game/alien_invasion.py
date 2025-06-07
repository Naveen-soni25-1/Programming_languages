import sys
import pygame

from setting import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self): # construction method 
        """Initialize the game, and create game resources."""
        pygame.init()  # Initialize background settings like sound and graphics
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        # Create a ship instance
        self.ship = Ship(self)

        # Create groups to store bullets and aliens
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()     # Respond to keyboard/mouse input
            self.ship.update()       # Update ship's position
            self._update_bullets()   # Update bullets and remove old ones
            self._update_screen()    # Draw everything on the screen
            self.clock.tick(60)      # limit the frame rate

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # Exit game when wqqqqaq`indow is closed
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)  # Handle key pres
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)    # Handle key released

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True  # Start moving right
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True   # Start moving left
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()            # Fire bullet
        elif event.key == pygame.K_q:
            sys.exit()                     # Quit the game

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False  # Stop moving right
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False   # Stop moving left

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()

        # Remove bullets that have gone off-screen
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.ship.screen_rect.right:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)   # Redraw the background
        self.ship.blitme()                         # Draw the ship

        # Draw each bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
