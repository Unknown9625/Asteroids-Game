import pygame # type: ignore

from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    CLOCK = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    running = True
    while running:
        dt = CLOCK.tick(60)/1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)    
        screen.fill(BLACK)
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()

