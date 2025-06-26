import pygame
from constants import *
from player import Player



def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    playr = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000.0   

        pygame.Surface.fill(screen,(0,0,0))
        playr.update(dt)
        playr.draw(screen)
        pygame.display.flip()
        
        






if __name__ == "__main__":
    main()