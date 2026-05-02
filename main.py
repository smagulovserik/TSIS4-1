import pygame
from game import game_loop
from db import get_top, get_or_create_player, init_db
from screens import draw_leaderboard

pygame.init()

init_db()

screen = pygame.display.set_mode((600, 400))
font = pygame.font.SysFont("Arial", 30)

state = "MENU"

username = ""
player_id = None

running = True

while running:
    screen.fill((25, 25, 35))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # MENU
        if state == "MENU":
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    if username.strip() != "":
                        player_id = get_or_create_player(username)
                        state = "GAME"

                elif event.key == pygame.K_l:
                    state = "LEADERBOARD"

                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]

                else:
                    username += event.unicode

        #  LEADERBOARD 
        elif state == "LEADERBOARD":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = "MENU"

    #  RENDER MENU
    if state == "MENU":
        title = font.render("SNAKE GAME", True, (0, 200, 120))
        screen.blit(title, (210, 100))

        txt = font.render("Enter username: " + username, True, (255, 255, 255))
        screen.blit(txt, (50, 180))

        hint = font.render("ENTER - Play | L - Leaderboard", True, (180, 180, 180))
        screen.blit(hint, (50, 230))

    #  GAME 
    elif state == "GAME":
        game_loop(player_id)
        state = "MENU"

    #  LEADERBOARD 
    elif state == "LEADERBOARD":
        data = get_top()
        draw_leaderboard(screen, data)

    pygame.display.update()

pygame.quit()