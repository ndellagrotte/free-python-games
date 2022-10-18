
from random import random
from turtle import *

from freegames import line

import pygame
import sys

pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Main Menu')
BG = pygame.image.load('Background.png')
PLAY = pygame.image.load('Background.png')
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
QUIT = pygame.image.load('Background.png')

pygame.init()

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)


def button(screen, position, text, size, colors=(255, 255, 255), font_type='Arial'):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if position[0] + size[0] > mouse[0] > position[0] and position[1] + size[1] > mouse[1] > position[1]:
        pygame.draw.rect(screen, colors, (position[0], position[1], size[0], size[1]))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, colors, (position[0], position[1], size[0], size[1]))
    text = font.render(text, True, (0, 0, 0))
    screen.blit(text, (position[0] + (size[0] / 2 - text.get_width() / 2), position[1] + (size[1] / 2 - text.get_height() / 2)))


def main_menu():
    pygame.display.set_caption('Main Menu')
    button(SCREEN, (SCREEN_WIDTH / 800, SCREEN_HEIGHT / 600), "Play", (200, 100), (255, 255, 255), "Arial")
    button(SCREEN, (SCREEN_WIDTH / 800, SCREEN_HEIGHT / 600), "Quit", (200, 100), (255, 255, 255), "Arial")
    SCREEN.blit(BG, (0, 0))

    pygame.display.update()

    while True:
        SCREEN.blit(BG, (0, 0))
        # SCREEN.blit(PLAY, (SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 - 50))
        # SCREEN.blit(QUIT, (SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 + 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_1:
                    play()
                if event.key == pygame.K_2:
                    pygame.quit()
                    quit()
        pygame.display.update()


def play():  # Play Screen
    pygame.display.set_caption('Play')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_1:
                    print("1")
                if event.key == pygame.K_2:
                    print("2")
                if event.key == pygame.K_3:
                    print("3")


def draw():
    """Draw maze."""
    color('black')
    width(5)

    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            if random() > 0.5:
                line(x, y, x + 40, y + 40)
            else:
                line(x, y + 40, x + 40, y)

    update()


def tap(x, y):
    """Draw line and dot for screen tap."""
    if abs(x) > 198 or abs(y) > 198:
        up()
    else:
        down()

    width(2)
    color('red')
    goto(x, y)
    dot(4)


main_menu()
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
draw()
onscreenclick(tap)
done()
