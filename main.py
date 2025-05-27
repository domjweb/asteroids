import pygame
from constants import *
from player import *

def main():
	pygame.init()
	player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
			 if event.type == pygame.QUIT:
					return
		screen.fill((0,0,0))
		player1.draw(screen)
		pygame.display.flip()

	
	print(f"""Starting Asteroids!
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")


if __name__ == "__main__":
	main()
