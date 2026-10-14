import pygame
from .snake import Snake
from .food import Food
from .sounds import create_eat_sound, create_game_over_sound

# Game Engine

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (220, 60, 60)


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cell_size = 20

        self.grid_width = width // self.cell_size
        self.grid_height = height // self.cell_size

        self.score = 0

        self.font = pygame.font.SysFont("Arial", 30)
        self.game_over_font = pygame.font.SysFont("Arial", 60)
        self.game_over_score_font = pygame.font.SysFont("Arial", 35)
        self.menu_font = pygame.font.SysFont("Arial", 28)

        # Difficulty
        self.moves_per_second = 8

        self._frame_counter = 0
        self.game_over = False

        # Create sounds
        self.eat_sound = create_eat_sound()
        self.game_over_sound = create_game_over_sound()

        self.create_game()

    def create_game(self):
        self.snake = Snake(
            self.grid_width // 2,
            self.grid_height // 2,
            self.cell_size
        )

        self.food = Food(
            self.grid_width,
            self.grid_height,
            self.cell_size
        )

        self.score = 0
        self._frame_counter = 0
        self.game_over = False

    def restart(self, difficulty):
        if difficulty == "easy":
            self.moves_per_second = 5

        elif difficulty == "medium":
            self.moves_per_second = 8

        elif difficulty == "hard":
            self.moves_per_second = 12

        self.create_game()

    def handle_keydown(self, key):
        # Do not control the snake during Game Over.
        if self.game_over:
            return

        # Arrow keys and WASD
        if key in (pygame.K_UP, pygame.K_w):
            self.snake.set_direction(0, -1)

        elif key in (pygame.K_DOWN, pygame.K_s):
            self.snake.set_direction(0, 1)

        elif key in (pygame.K_LEFT, pygame.K_a):
            self.snake.set_direction(-1, 0)

        elif key in (pygame.K_RIGHT, pygame.K_d):
            self.snake.set_direction(1, 0)

    def handle_input(self):
        pass

    def update(self):
        # Stop the snake after Game Over.
        if self.game_over:
            return

        self._frame_counter += 1

        frames_per_move = max(
            1,
            60 // self.moves_per_second
        )

        if self._frame_counter < frames_per_move:
            return

        self._frame_counter = 0

        # Move snake
        self.snake.move()

        # Wall collision
        if self.snake.collides_with_wall(
            self.grid_width,
            self.grid_height
        ):
            self.game_over = True

            # Play Game Over sound
            self.game_over_sound.play()

            return

        # Self collision
        if self.snake.collides_with_self():
            self.game_over = True

            # Play Game Over sound
            self.game_over_sound.play()

            return

        # Food collision
        if self.snake.head_rect().colliderect(
            self.food.rect()
        ):
            self.snake.grow()
            self.score += 1
            self.food.respawn(self.snake.body)

            # Play eating sound
            self.eat_sound.play()

    def render(self, screen):
        # Draw food
        pygame.draw.rect(
            screen,
            RED,
            self.food.rect()
        )

        # Draw snake
        for rect in self.snake.segment_rects():
            pygame.draw.rect(
                screen,
                GREEN,
                rect
            )

        # Draw score
        score_text = self.font.render(
            f"Score: {self.score}",
            True,
            WHITE
        )

        screen.blit(score_text, (10, 10))

        # Game Over screen
        if self.game_over:
            game_over_text = self.game_over_font.render(
                "GAME OVER",
                True,
                WHITE
            )

            final_score_text = self.game_over_score_font.render(
                f"Final Score: {self.score}",
                True,
                WHITE
            )

            easy_text = self.menu_font.render(
                "1 - EASY",
                True,
                WHITE
            )

            medium_text = self.menu_font.render(
                "2 - MEDIUM",
                True,
                WHITE
            )

            hard_text = self.menu_font.render(
                "3 - HARD",
                True,
                WHITE
            )

            exit_text = self.menu_font.render(
                "Q - EXIT",
                True,
                WHITE
            )

            screen.blit(
                game_over_text,
                game_over_text.get_rect(
                    center=(self.width // 2, 170)
                )
            )

            screen.blit(
                final_score_text,
                final_score_text.get_rect(
                    center=(self.width // 2, 240)
                )
            )

            screen.blit(
                easy_text,
                easy_text.get_rect(
                    center=(self.width // 2, 320)
                )
            )

            screen.blit(
                medium_text,
                medium_text.get_rect(
                    center=(self.width // 2, 365)
                )
            )

            screen.blit(
                hard_text,
                hard_text.get_rect(
                    center=(self.width // 2, 410)
                )
            )

            screen.blit(
                exit_text,
                exit_text.get_rect(
                    center=(self.width // 2, 455)
                )
            )