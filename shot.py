from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS
        self.velocity = velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.position[0], self.position[1]), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt