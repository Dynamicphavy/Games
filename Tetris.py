import sys
import pygame
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 25

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
COLORS = [RED, BLUE, GREEN]

# Tetromino shapes
SHAPES = [
    [
        ['.....',
         '.....',
         '.....',
         'OOOO.',
         '.....'],
        ['.....',
         '..O..',
         '..O..',
         '..O..',
         '..O..']
    ],
    [
        ['.....',
         '.....',
         '..O..',
         '.OOO.',
         '.....'],
        ['.....',
         '..O..',
         '.OO..',
         '..O..',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '..O..',
         '.....'],
        ['.....',
         '..O..',
         '..OO.',
         '..O..',
         '.....']
    ],
    [
        ['.....',
         '.....',
         '..OO.',
         '.OO..',
         '.....'],
        ['.....',
         '.....',
         '.OO..',
         '..OO.',
         '.....'],
        ['.....',
         '.O...',
         '.OO..',
         '..O..',
         '.....'],
        ['.....',
         '..O..',
         '.OO..',
         '.O...',
         '.....']
    ],
    [
        ['.....',
         '..O..',
         '..O..',
         '..OO.',
         '.....'],
        ['.....',
         '...O.',
         '.OOO.',
         '.....',
         '.....'],
        ['.....',
         '.OO..',
         '..O..',
         '..O..',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '.O...',
         '.....']
    ]
]

class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(COLORS)
        self.rotation = 0

class Tetris:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0

    def new_piece(self):
        shape = random.choice(SHAPES)
        return Tetromino(self.width // 2 - 2, 0, shape)

    def valid_move(self, piece, dx, dy, dr):
        shape = piece.shape[(piece.rotation + dr) % len(piece.shape)]
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell == 'O':
                    x = piece.x + j + dx
                    y = piece.y + i + dy
                    if x < 0 or x >= self.width or y < 0 or y >= self.height:
                        return False
                    if self.grid[y][x]:
                        return False
        return True

    def lock_piece(self, piece):
        shape = piece.shape[piece.rotation % len(piece.shape)]
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell == 'O':
                    self.grid[piece.y + i][piece.x + j] = piece.color
        lines_cleared = self.clear_lines()
        self.score += lines_cleared * 100
        self.current_piece = self.new_piece()
        if not self.valid_move(self.current_piece, 0, 0, 0):
            self.game_over = True

    def clear_lines(self):
        lines_cleared = 0
        new_grid = [row for row in self.grid if any(cell == 0 for cell in row)]
        lines_cleared = self.height - len(new_grid)
        for _ in range(lines_cleared):
            new_grid.insert(0, [0 for _ in range(self.width)])
        self.grid = new_grid
        return lines_cleared

    def update(self):
        if not self.game_over:
            if self.valid_move(self.current_piece, 0, 1, 0):
                self.current_piece.y += 1
            else:
                self.lock_piece(self.current_piece)

    def draw(self, screen):
        # Draw grid
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, cell, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1))

        # Draw current piece
        shape_matrix = self.current_piece.shape[self.current_piece.rotation % len(self.current_piece.shape)]
        for i, row in enumerate(shape_matrix):
            for j, cell in enumerate(row):
                if cell == 'O':
                    pygame.draw.rect(screen, self.current_piece.color,
                                     ((self.current_piece.x + j) * GRID_SIZE,
                                      (self.current_piece.y + i) * GRID_SIZE,
                                      GRID_SIZE - 1, GRID_SIZE - 1))

    @staticmethod
    def draw_score(screen, score, x, y):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(text, (x, y))

    @staticmethod
    def draw_game_over(screen, x, y):
        font = pygame.font.Font(None, 48)
        text = font.render("Game Over", True, RED)
        screen.blit(text, (x, y))

    @staticmethod
    def main():
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Tetris')
        clock = pygame.time.Clock()
        game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)
        fall_time = 0
        fall_speed = 300  # milliseconds

        while True:
            screen.fill(BLACK)
            delta_time = clock.tick()
            fall_time += delta_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if not game.game_over and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and game.valid_move(game.current_piece, -1, 0, 0):
                        game.current_piece.x -= 1
                    if event.key == pygame.K_RIGHT and game.valid_move(game.current_piece, 1, 0, 0):
                        game.current_piece.x += 1
                    if event.key == pygame.K_DOWN and game.valid_move(game.current_piece, 0, 1, 0):
                        game.current_piece.y += 1
                    if event.key == pygame.K_UP and game.valid_move(game.current_piece, 0, 0, 1):
                        game.current_piece.rotation = (game.current_piece.rotation + 1) % len(game.current_piece.shape)
                    if event.key == pygame.K_SPACE:
                        while game.valid_move(game.current_piece, 0, 1, 0):
                            game.current_piece.y += 1
                        game.lock_piece(game.current_piece)

                if game.game_over and event.type == pygame.KEYDOWN:
                    game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)

            if fall_time > fall_speed:
                game.update()
                fall_time = 0

            game.draw(screen)
            Tetris.draw_score(screen, game.score, 10, 10)

            if game.game_over:
                Tetris.draw_game_over(screen, WIDTH // 2 - 100, HEIGHT // 2 - 30)

            pygame.display.flip()


if __name__ == '__main__':
    Tetris.main()
