import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
DARK = (60, 60, 60)

font = pygame.font.SysFont("Arial", 28)
title_font = pygame.font.SysFont("Arial", 32)

def draw_menu(screen):
    screen.fill(WHITE)
    txt = font.render("SNAKE GAME - PRESS SPACE", True, BLACK)
    screen.blit(txt, (120, 180))
    pygame.display.update()


def draw_leaderboard(screen, data):
    screen.fill(WHITE)

    # ================= TITLE =================
    title = title_font.render("LEADERBOARD", True, BLACK)
    screen.blit(title, (200, 20))

    # ================= TABLE SETTINGS =================
    start_x = 80
    start_y = 90

    col_rank = start_x
    col_name = start_x + 80
    col_score = start_x + 300
    col_level = start_x + 420

    row_h = 35

    # ================= HEADER =================
    pygame.draw.line(screen, GRAY, (start_x, start_y - 10), (550, start_y - 10), 2)

    header = font.render("RANK", True, DARK)
    screen.blit(header, (col_rank, start_y))

    header = font.render("NAME", True, DARK)
    screen.blit(header, (col_name, start_y))

    header = font.render("SCORE", True, DARK)
    screen.blit(header, (col_score, start_y))

    header = font.render("LVL", True, DARK)
    screen.blit(header, (col_level, start_y))

    pygame.draw.line(screen, GRAY, (start_x, start_y + 25), (550, start_y + 25), 2)

    # ================= ROWS =================
    y = start_y + 40

    for i, row in enumerate(data):
        username, score, level, _ = row

        # rank (fixed small column)
        rank_text = font.render(str(i + 1), True, BLACK)
        screen.blit(rank_text, (col_rank, y))

        # name (fixed width box)
        name_text = font.render(username[:12], True, BLACK)
        screen.blit(name_text, (col_name, y))

        # score
        score_text = font.render(str(score), True, BLACK)
        screen.blit(score_text, (col_score, y))

        # level
        level_text = font.render(str(level), True, BLACK)
        screen.blit(level_text, (col_level, y))

        # row line
        pygame.draw.line(screen, (220, 220, 220), (start_x, y + 25), (550, y + 25), 1)

        y += row_h

    # ================= FOOTER =================
    hint = font.render("ESC - back to menu", True, (120, 120, 120))
    screen.blit(hint, (180, 350))

    pygame.display.update()


def draw_game_over(screen, font, score, level, best):
    screen.fill((245, 245, 245))

    title = font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(title, (220, 80))

    s = font.render(f"Score: {score}", True, (0, 0, 0))
    l = font.render(f"Level: {level}", True, (0, 0, 0))
    b = font.render(f"Best: {best}", True, (0, 0, 0))

    screen.blit(s, (240, 140))
    screen.blit(l, (240, 170))
    screen.blit(b, (240, 200))

    hint = font.render("R - Retry | M - Menu", True, (100, 100, 100))
    screen.blit(hint, (180, 300))


def draw_settings(screen, font, settings):
    screen.fill((245, 245, 245))

    title = font.render("SETTINGS", True, (0, 0, 0))
    screen.blit(title, (240, 80))

    grid = font.render(f"Grid: {settings['grid']} (G)", True, (0, 0, 0))
    sound = font.render(f"Sound: {settings['sound']} (S)", True, (0, 0, 0))

    screen.blit(grid, (200, 140))
    screen.blit(sound, (200, 170))

    hint = font.render("ESC - Back | G - Toggle Grid | S - Toggle Sound", True, (100, 100, 100))
    screen.blit(hint, (80, 300))