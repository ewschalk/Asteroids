from circleshape import *
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
                           
    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

class shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(velocity)
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (int(self.position.x), int(self.position.y)), SHOT_RADIUS, 1)

    def update(self, dt):
        self.position += (self.velocity * dt)

    