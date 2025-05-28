import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
	pygame.init()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	fps_clock = pygame.time.Clock()
	updatable = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updatable, drawables)
	Asteroid.containers = (asteroids, updatable, drawables)
	AsteroidField.containers = (updatable)
	player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			 if event.type == pygame.QUIT:
					return
		screen.fill((0,0,0))
		updatable.update(dt)
		for drawable in drawables:
			drawable.draw(screen)
		pygame.display.flip()
		dt = fps_clock.tick(60) / 1000



	
	print(f"""Starting Asteroids!
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")


if __name__ == "__main__":
	main()
