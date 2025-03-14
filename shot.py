import pygame # type: ignore

from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, SHOT_RADIUS, 0)

    def update(self, dt):
        self.position  += (self.velocity * dt)