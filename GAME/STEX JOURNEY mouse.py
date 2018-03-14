#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import time
import os
import sys
from pygame.locals import *


#Initialisation de Pygame

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
game_icon = pygame.image.load("pictures/icon_game.png").convert_alpha()
blur_wallpaper = pygame.image.load("pictures/blur_wallpaper.png").convert_alpha()
credits_all = pygame.image.load("pictures/screen_credits.png").convert_alpha()
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

jouer_r = jouer_1.get_rect()
jouer_r.x, jouer_r.y = 0,240
options_r = options_1.get_rect()
options_r.x, options_r.y = 0,320
commandes_r = commandes_1.get_rect()
commandes_r.x, commandes_r.y = 0,405
credits_r = credits_1.get_rect()
credits_r.x, credits_r.y = 0,490


#Ecran d'accueil func
def LoadingMenu():
    screen_wallpaper = screen.blit(wallpaper,(0,-45))
    screen_title = screen.blit(game_title,(0,0))
    play_btn = screen.blit(jouer_1,(0,240))
    options_btn = screen.blit(options_1,(0,320))
    commandes_btn = screen.blit(commandes_1,(0,405))
    credits_btn = screen.blit(credits_1,(0,490))
    print('Loading screen loaded')


#Lancement de la boucle du jeu

n = 0
running = True

if n == 0:
    LoadingMenu()
    pygame.init()

while running:
    pygame.init()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == KEYUP and event.key == pygame.K_ESCAPE:
            n = 0
            print("Echap pressed")

        if credits_r.collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN:
            blur_screen = screen.blit(blur_wallpaper,(0,-45))
            screen_title = screen.blit(game_title,(0,0))
            credits_screen = screen.blit(credits_all,(0,0))
            pygame.display.flip()
            n = 1

    if jouer_r.collidepoint(pygame.mouse.get_pos()) and n is not 1:
        screen_wallpaper = screen.blit(wallpaper,(0,-45))
        screen_title = screen.blit(game_title,(0,0))
        play_btn = screen.blit(jouer_2,(0,240))
        options_btn = screen.blit(options_1,(0,320))
        commandes_btn = screen.blit(commandes_1,(0,405))
        credits_btn = screen.blit(credits_1,(0,490))
        pygame.display.flip()

    if options_r.collidepoint(pygame.mouse.get_pos()) and n is not 1:
        screen_wallpaper = screen.blit(wallpaper,(0,-45))
        screen_title = screen.blit(game_title,(0,0))
        play_btn = screen.blit(jouer_1,(0,240))
        options_btn = screen.blit(options_2,(0,320))
        commandes_btn = screen.blit(commandes_1,(0,405))
        credits_btn = screen.blit(credits_1,(0,490))
        pygame.display.flip()

    if commandes_r.collidepoint(pygame.mouse.get_pos()) and n is not 1:
        screen_wallpaper = screen.blit(wallpaper,(0,-45))
        screen_title = screen.blit(game_title,(0,0))
        play_btn = screen.blit(jouer_1,(0,240))
        options_btn = screen.blit(options_1,(0,320))
        commandes_btn = screen.blit(commandes_2,(0,405))
        credits_btn = screen.blit(credits_1,(0,490))
        pygame.display.flip()

    if credits_r.collidepoint(pygame.mouse.get_pos()) and n is not 1:
        screen_wallpaper = screen.blit(wallpaper,(0,-45))
        screen_title = screen.blit(game_title,(0,0))
        play_btn = screen.blit(jouer_1,(0,240))
        options_btn = screen.blit(options_1,(0,320))
        commandes_btn = screen.blit(commandes_1,(0,405))
        credits_btn = screen.blit(credits_2,(0,490))
        pygame.display.flip()

    time.sleep(0.000000000000000000000000000000000000000000000000000000001)

    pygame.display.flip()









