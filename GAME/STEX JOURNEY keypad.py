#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import time
import os
import sys
from pygame.locals import *

#Initialisation de Pygame

pygame.init()
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('STEX JOURNEY')
clock = pygame.time.Clock()

#Chargement des données du jeu

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

wallpaper = pygame.image.load("pictures/wallpaper.png").convert()
blur_wallpaper = pygame.image.load("pictures/blur_wallpaper.png").convert()
credits_screen = pygame.image.load("pictures/screen_credits.png").convert_alpha()
game_icon = pygame.image.load("pictures/icon_game.png").convert_alpha()
screen_icon = pygame.display.set_icon(game_icon)

game_title = pygame.image.load("buttons/home_title.png").convert_alpha()
jouer_1 = pygame.image.load("buttons/jouer_1.png").convert_alpha()
jouer_2 = pygame.image.load("buttons/jouer_2.png").convert_alpha()
options_1 = pygame.image.load("buttons/options_1.png").convert_alpha()
options_2 = pygame.image.load("buttons/options_2.png").convert_alpha()
commandes_1 = pygame.image.load("buttons/commandes_1.png").convert_alpha()
commandes_2 = pygame.image.load("buttons/commandes_2.png").convert_alpha()
credits_1 = pygame.image.load("buttons/credits_1.png").convert_alpha()
credits_2 = pygame.image.load("buttons/credits_2.png").convert_alpha()

n = 0


#Lancement de la boucle du menu

intro = True

while intro:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if n == 0:
            screen_wallpaper = screen.blit(wallpaper,(0,-45))
            screen_title = screen.blit(game_title,(0,0))
            play_btn = screen.blit(jouer_2,(0,240))
            options_btn = screen.blit(options_1,(0,320))
            commandes_btn = screen.blit(commandes_1,(0,405))
            credits_btn = screen.blit(credits_1,(0,490))
            pygame.display.flip()

        if event.type == KEYDOWN and event.key == K_DOWN:
            n = n+1

        if event.type == KEYDOWN and event.key == K_UP:
            n = n-1

        if n > 3:
            n = 0

        if n < 0:
            n = 3

        if n == 1:
            screen_wallpaper = screen.blit(wallpaper,(0,-45))
            screen_title = screen.blit(game_title,(0,0))
            play_btn = screen.blit(jouer_1,(0,240))
            options_btn = screen.blit(options_2,(0,320))
            commandes_btn = screen.blit(commandes_1,(0,405))
            credits_btn = screen.blit(credits_1,(0,490))
            pygame.display.flip()

        if n == 2:
            screen_wallpaper = screen.blit(wallpaper,(0,-45))
            screen_title = screen.blit(game_title,(0,0))
            play_btn = screen.blit(jouer_1,(0,240))
            options_btn = screen.blit(options_1,(0,320))
            commandes_btn = screen.blit(commandes_2,(0,405))
            credits_btn = screen.blit(credits_1,(0,490))
            pygame.display.flip()

        if n == 3:
            screen_wallpaper = screen.blit(wallpaper,(0,-45))
            screen_title = screen.blit(game_title,(0,0))
            play_btn = screen.blit(jouer_1,(0,240))
            options_btn = screen.blit(options_1,(0,320))
            commandes_btn = screen.blit(commandes_1,(0,405))
            credits_btn = screen.blit(credits_2,(0,490))
            pygame.display.flip()

            if event.type == KEYUP and event.key == K_RETURN:
                screen_wallpaper = screen.blit(blur_wallpaper,(0,-45))
                screen_title = screen.blit(game_title,(0,0))
                screen_credits = screen.blit(credits_screen,(0,0))
                pygame.display.flip()







