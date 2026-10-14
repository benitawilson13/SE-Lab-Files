import pygame
from game.game_engine import GameEngine

# Initialize pygame/Start application
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake - Pygame Version")

# Colors
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game engine
engine = GameEngine(WIDTH, HEIGHT)


def main():
    running = True

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                # Game Over menu
                if engine.game_over:

                    if event.key == pygame.K_1:
                        engine.restart("easy")

                    elif event.key == pygame.K_2:
                        engine.restart("medium")

                    elif event.key == pygame.K_3:
                        engine.restart("hard")

                    elif event.key == pygame.K_q:
                        running = False

                # Normal game controls
                else:
                    engine.handle_keydown(event.key)

        engine.handle_input()
        engine.update()
        engine.render(SCREEN)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()