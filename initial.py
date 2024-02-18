import pygame
from pygame.locals import *
import os

# Game Initialization
pygame.init()
pygame.font.init()
# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

font1 = pygame.font.SysFont("comicsans", 20)



# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Game Fonts
font1 = pygame.font.SysFont("comicsans", 20)

# Game Framerate
clock = pygame.time.Clock()
FPS = 30


# Main Menu
def main_menu():
    menu = True
    selected = "start"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "start"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        print("Start")
                    if selected == "quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        screen.fill(blue)
        title = ("MainMenu", font1, 90, yellow)
        if selected == "start":
            text_start = ("START", font1, 75, white)
        else:
            text_start = ("START", font1, 75, black)
        if selected == "quit":
            text_quit = ("QUIT", font1, 75, white)
        else:
            text_quit = ("QUIT", font1, 75, black)

        title_rect = title()
        start_rect = text_start()
        quit_rect = text_quit()

        # Main Menu Text
        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_start, (screen_width / 2 - (start_rect[2] / 2), 300))
        screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")


# Initialize the Game
main_menu()
pygame.quit()
quit()
