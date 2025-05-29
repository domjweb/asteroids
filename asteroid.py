from circleshape import *
from constants import *
import random
from player import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = velocity
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            random_uni = random.uniform(20, 50)
            random_vec1 = self.velocity.rotate(random_uni)
            random_vec2 = self.velocity.rotate(random_uni * -1) 
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            Smol_Asteroid1 = Asteroid(self.position[0], self.position[1], new_radius, random_vec1 * 1.2)
            Smol_Asteroid2 = Asteroid(self.position[0], self.position[1], new_radius, random_vec2 * 1.2)

    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.position[0], self.position[1]), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
