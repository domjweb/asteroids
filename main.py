import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import * 
from shot import *


def main():
	pygame.init()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	fps_clock = pygame.time.Clock()
	updatable = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots_taken = pygame.sprite.Group()
	Player.containers = (updatable, drawables)
	Asteroid.containers = (asteroids, updatable, drawables)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawables)
	player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 0, shots_taken)
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			 if event.type == pygame.QUIT:
					return
		screen.fill((0,0,0))
		updatable.update(dt)
		shots_copy = shots_taken.copy()
		for asteroid in asteroids:
			for shot in shots_copy:
				if asteroid.collision_check(shot) == True:
					asteroid.split()
					shot.kill()
			if player1.collision_check(asteroid) == True:
				print("Game Over!")
				sys.exit()
		for drawable in drawables:
			drawable.draw(screen)
		pygame.display.flip()
		dt = fps_clock.tick(60) / 1000



	
	print(f"""Starting Asteroids!
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")


if __name__ == "__main__":
	main()
