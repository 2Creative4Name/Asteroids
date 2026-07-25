import pygame
from constants import *
from logger import log_state
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField

def main() -> None:
    
    pygame.init()
    
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    asteroid_field = AsteroidField()
    dt = 0.0

    
    #Start the game
    while True:
        log_state()
        #Game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
            
        screen.fill("black")
        
        
        
        for i in drawable:
            i.draw(screen)
        
        pygame.display.flip()
            
        dt = clock.tick(60) / 1000 #FPS
            
    

    
if __name__ == "__main__":
    main()
