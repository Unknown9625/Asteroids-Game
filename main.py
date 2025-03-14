import pygame # type: ignore
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import * 
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (shots, updatable, drawable)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    CLOCK = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    running = True
    while running:
        dt = CLOCK.tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)    
        screen.fill(BLACK)
        for drawable_object in drawable:
            drawable_object.draw(screen)
        pygame.display.flip()

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
                    
if __name__ == "__main__":
    main()