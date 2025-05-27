import pygame
from constants import *
from player import *

def main():
	pygame.init()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	fps_clock = pygame.time.Clock()
	updateable = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	Player.containers = (updateable, drawables)
	player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	while True:
		for event in pygame.event.get():
			 if event.type == pygame.QUIT:
					return
		screen.fill((0,0,0))
		updateable.update(dt)
		for drawable in drawables:
			drawable.draw(screen)
		pygame.display.flip()
		dt = fps_clock.tick(60) / 1000



	
	print(f"""Starting Asteroids!
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")


if __name__ == "__main__":
	main()
