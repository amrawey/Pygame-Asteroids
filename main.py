import pygame

from constants import *
from player import Player
from asteroids import Asteroid
from asteroidsfield import AsteroidField
from shots import Shot
def main():
    pygame.init
    frames_per_second = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Shot.containers = (shots,updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
    #Field = AsteroidField()
    
    #game_over = False
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    #   if game_over:
      #      if event.type == pygame.KEYDOWN:
      #          if event.key == pygame.K_r:  # Imagine 'R' is to restart
      #              # Reset all necessary game variables
      #              game_over = False
      #          elif event.key == pygame.K_q:  # 'Q' to quit
       #             return
       # if not game_over:        
        for obj in updatable:
            obj.update(dt)
            
        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)
            
        for asteroid in asteroids:
            if player.is_colliding(asteroid) :
                print("GAME OVER!!!")
                return
            for shot in shots:
                if asteroid.is_colliding(shot):
                    shot.kill()
                    asteroid.split()
            
        pygame.display.flip()
        
        dt = frames_per_second.tick(60)
        dt /= 1000

        
    
if __name__ == "__main__":
    main()
 