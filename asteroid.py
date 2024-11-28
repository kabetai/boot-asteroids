import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        # We need screen to draw on
        # Color of asteroid being drawn as RGB tuple
        # Position from parent circkeshape to know where to draw
        # Radius of asteroid circle
        # Thickness of line
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt) 
