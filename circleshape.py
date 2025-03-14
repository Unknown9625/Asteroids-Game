import pygame # type: ignore

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
 

    def collision(self, new_shape):
        if self.position.distance_to(new_shape.position) <= (self.radius + new_shape.radius):
            return True
        else:
            return False

    def draw(self, screen):
        pass

    def update(self, dt):
        pass