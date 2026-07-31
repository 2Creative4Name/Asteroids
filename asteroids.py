from circleshape import *
import pygame
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        
    def split(self) -> None:
        
        pygame.sprite.Sprite.kill(self)
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
            
        new_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius / 2)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius / 2)
        
        new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
        new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, - angle) * 1.2