import pygame
from pygame.sprite import Sprite


class Lives(Sprite):
    """A class represents the lives remained."""

    def __init__(self, ai_game):
        """Initializes lives attributes."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
		
        # Load the ship image and get the rect.
        self.image = pygame.image.load('images/heart.png')
        self.rect = self.image.get_rect()

        # Store a decimal value for ship's horizontal position.
        
