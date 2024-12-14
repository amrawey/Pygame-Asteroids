import pygame

from constants import *
from circleshape import *
from player import *


def main():
    pygame.init
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
    frames_per_second = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for player in updatable:
            player.update(dt)
        screen.fill((0,0,0))
        for player in drawable:
            player.draw(screen)
        pygame.display.flip()
        
        dt = frames_per_second.tick(60)
        dt /= 1000

        
    
if __name__ == "__main__":
    main()
 