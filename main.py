import pygame
import math

from hex_engine import HexPosition


def draw_hexagon(screen, center, size, color):
    """
    Draw a hexagon on the screen with the given center, size, and color.
    """
    x, y = center
    points = []
    for i in range(6):
        angle = math.pi / 3 * i
        px = x + size * math.cos(angle)
        py = y + size * math.sin(angle)
        points.append((px, py))
    pygame.draw.polygon(screen, color, points, 0)
    pygame.draw.polygon(screen, (0, 0, 0), points, 1)


def play_game(game, screen):
    while game.winner == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x, y = pos
                # calculate which hexagon was clicked on
                q = int(round((x - 40) / 52.0))
                r = int(round((y - 40) / 60.0 - q / 2.0))
                if q < 0 or q >= game.size or r < 0 or r >= game.size:
                    continue
                if game.board[r][q] != 0:
                    continue
                game.move((r, q))

        # Draw the board
        screen.fill((255, 255, 255))
        for r in range(game.size):
            for q in range(game.size):
                x = 40 + 52 * q
                y = 40 + 60 * r + 30 * q
                if game.board[r][q] == 1:
                    draw_hexagon(screen, (x, y), 20, (0, 0, 255))
                elif game.board[r][q] == -1:
                    draw_hexagon(screen, (x, y), 20, (255, 0, 0))
                else:
                    draw_hexagon(screen, (x, y), 20, (255, 255, 255))

        pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Show the winning player
        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        text = font.render("Player {} wins!".format(game.winner), True, (0, 0, 0))
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, text_rect)

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    game = HexPosition()
    screen = pygame.display.set_mode(((game.size + 1) * 52, (game.size + 1) * 60))
    pygame.display.set_caption("Hex Game")
    play_game(game, screen)
    pygame.quit()
