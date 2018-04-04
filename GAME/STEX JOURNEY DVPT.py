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
game_icon = pygame.image.load("pictures/icon_game.png").convert_alpha()
screen_icon = pygame.display.set_icon(game_icon)
pygame.display.set_caption('STEX JOURNEY')
clock = pygame.time.Clock()
pygame.init()


#Chargement des données du jeu

wallpaper = pygame.image.load("pictures/wallpaper.png").convert()
blur_wallpaper = pygame.image.load("pictures/blur_wallpaper.png").convert_alpha()
blur_menu1 = pygame.image.load("pictures/blur_menu_out.png").convert_alpha()
credits_screen = pygame.image.load("pictures/screen_credits.png").convert_alpha()
commands_screen = pygame.image.load("pictures/screen_commands.png").convert_alpha()
fondingame = pygame.image.load("pictures/fondingame.png").convert()
game_intro = pygame.image.load("pictures/game_intro.png").convert()
loading_1 = pygame.image.load("pictures/loading_1.png").convert()
loading_2 = pygame.image.load("pictures/loading_2.png").convert()
loading_3 = pygame.image.load("pictures/loading_3.png").convert()

luffy_d = pygame.image.load("pictures/avatar/luffy_d.png").convert_alpha()
luffy_d_blur = pygame.image.load("pictures/avatar/luffy_d_blur.png").convert_alpha()
luffy_d1 = pygame.image.load("pictures/avatar/luffy_d1.png").convert_alpha()
luffy_d2 = pygame.image.load("pictures/avatar/luffy_d2.png").convert_alpha()
luffy_d3 = pygame.image.load("pictures/avatar/luffy_d3.png").convert_alpha()
luffy_d4 = pygame.image.load("pictures/avatar/luffy_d4.png").convert_alpha()

luffy_u = pygame.image.load("pictures/avatar/luffy_u.png").convert_alpha()
luffy_u1 = pygame.image.load("pictures/avatar/luffy_u1.png").convert_alpha()
luffy_u2 = pygame.image.load("pictures/avatar/luffy_u2.png").convert_alpha()
luffy_u3 = pygame.image.load("pictures/avatar/luffy_u3.png").convert_alpha()
luffy_u4 = pygame.image.load("pictures/avatar/luffy_u4.png").convert_alpha()

luffy_r = pygame.image.load("pictures/avatar/luffy_r.png").convert_alpha()
luffy_r1 = pygame.image.load("pictures/avatar/luffy_r1.png").convert_alpha()
luffy_r2 = pygame.image.load("pictures/avatar/luffy_r2.png").convert_alpha()
luffy_r3 = pygame.image.load("pictures/avatar/luffy_r3.png").convert_alpha()
luffy_r4 = pygame.image.load("pictures/avatar/luffy_r4.png").convert_alpha()

luffy_l = pygame.image.load("pictures/avatar/luffy_l.png").convert_alpha()
luffy_l1 = pygame.image.load("pictures/avatar/luffy_l1.png").convert_alpha()
luffy_l2 = pygame.image.load("pictures/avatar/luffy_l2.png").convert_alpha()
luffy_l3 = pygame.image.load("pictures/avatar/luffy_l3.png").convert_alpha()
luffy_l4 = pygame.image.load("pictures/avatar/luffy_l4.png").convert_alpha()

villager = pygame.image.load("pictures/avatar/bot.png").convert_alpha()

game_title = pygame.image.load("buttons/home_title.png").convert_alpha()
play_1 = pygame.image.load("buttons/jouer_1.png").convert_alpha()
play_2 = pygame.image.load("buttons/jouer_2.png").convert_alpha()
settings_1 = pygame.image.load("buttons/options_1.png").convert_alpha()
settings_2 = pygame.image.load("buttons/options_2.png").convert_alpha()
commands_1 = pygame.image.load("buttons/commandes_1.png").convert_alpha()
commands_2 = pygame.image.load("buttons/commandes_2.png").convert_alpha()
credits_1 = pygame.image.load("buttons/credits_1.png").convert_alpha()
credits_2 = pygame.image.load("buttons/credits_2.png").convert_alpha()
back_button = pygame.image.load("buttons/retour.png").convert_alpha()
son_on = pygame.image.load("buttons/son_on.png").convert_alpha()
son_off = pygame.image.load("buttons/son_off.png").convert_alpha()

play_r = play_1.get_rect()
play_r.x, play_r.y = 0,240
settings_r = settings_1.get_rect()
settings_r.x, settings_r.y = 0,320
commands_r = commands_1.get_rect()
commands_r.x, commands_r.y = 0,405
credits_r = credits_1.get_rect()
credits_r.x, credits_r.y = 0,490
back_r = back_button.get_rect()
back_r.x, back_r.y = 925,25
son_r = son_on.get_rect()
son_r.x, son_r.y = 325,200


#Fontions

def LoadingMenu():
    screen_wallpaper = screen.blit(wallpaper,(0,-45))
    screen_title = screen.blit(game_title,(0,0))
    play_btn = screen.blit(play_1,(0,240))
    options_btn = screen.blit(settings_1,(0,320))
    commandes_btn = screen.blit(commands_1,(0,405))
    credits_btn = screen.blit(credits_1,(0,490))
    global CurrentMenu
    CurrentMenu = "LoadingMenu"
    print(CurrentMenu + ' loaded')

def Play_intro():
    screen_wallpaper = screen.blit(game_intro,(0,0))
    screen_luffy = screen.blit(luffy_d,(xluffy,yluffy))
    pygame.mouse.set_visible(False)
    pygame.key.set_repeat(True)
    pygame.display.flip()
    global CurrentMenu
    CurrentMenu = "PlayMenu"
    print(CurrentMenu + 'loaded')

def Settings_on():
    screen_blur = screen.blit(blur_wallpaper,(0,-45))
    screen_title = screen.blit(game_title,(0,0))
    screen_back = screen.blit(back_button,(925,25))
    screen_sonon = screen.blit(son_on,(325,200))
    pygame.display.flip()
    global CurrentMenu
    CurrentMenu = "SettingsMenu_on"
    print(CurrentMenu + ' loaded')

def Settings_off():
    screen_blur = screen.blit(blur_wallpaper,(0,-45))
    screen_title = screen.blit(game_title,(0,0))
    screen_back = screen.blit(back_button,(925,25))
    screen_sonoff = screen.blit(son_off,(325,200))
    pygame.display.flip()
    global CurrentMenu
    CurrentMenu = "SettingsMenu_off"
    print(CurrentMenu + ' loaded')

def Commands():
    screen_blur = screen.blit(blur_wallpaper,(0,-45))
    screen_commands = screen.blit(commands_screen,(0,0))
    screen_title = screen.blit(game_title,(0,0))
    screen_back = screen.blit(back_button,(925,25))
    pygame.display.flip()
    global CurrentMenu
    CurrentMenu = "CommandsMenu"
    print(CurrentMenu + ' loaded')

def Credits():
    screen_blur = screen.blit(blur_wallpaper,(0,-45))
    screen_credits = screen.blit(credits_screen,(0,0))
    screen_title = screen.blit(game_title,(0,0))
    screen_back = screen.blit(back_button,(925,25))
    pygame.display.flip()
    global CurrentMenu
    CurrentMenu = "CreditsMenu"
    print(CurrentMenu + ' loaded')

def WhichOneIsOnHover():
    if play_r.collidepoint(pygame.mouse.get_pos()) and n != 1:
        screen_wallpaper = screen.blit(wallpaper,(0,-45))
        screen_title = screen.blit(game_title,(0,0))
        play_btn = screen.blit(play_2,(0,240))
        options_btn = screen.blit(settings_1,(0,320))
        commandes_btn = screen.blit(commands_1,(0,405))
        credits_btn = screen.blit(credits_1,(0,490))
        pygame.display.flip()

    if settings_r.collidepoint(pygame.mouse.get_pos()) and n != 1:
        screen_wallpaper = screen.blit(wallpaper,(0,-45))
        screen_title = screen.blit(game_title,(0,0))
        play_btn = screen.blit(play_1,(0,240))
        options_btn = screen.blit(settings_2,(0,320))
        commandes_btn = screen.blit(commands_1,(0,405))
        credits_btn = screen.blit(credits_1,(0,490))
        pygame.display.flip()

    if commands_r.collidepoint(pygame.mouse.get_pos()) and n != 1:
        screen_wallpaper = screen.blit(wallpaper,(0,-45))
        screen_title = screen.blit(game_title,(0,0))
        play_btn = screen.blit(play_1,(0,240))
        options_btn = screen.blit(settings_1,(0,320))
        commandes_btn = screen.blit(commands_2,(0,405))
        credits_btn = screen.blit(credits_1,(0,490))
        pygame.display.flip()

    if credits_r.collidepoint(pygame.mouse.get_pos()) and n != 1:
        screen_wallpaper = screen.blit(wallpaper,(0,-45))
        screen_title = screen.blit(game_title,(0,0))
        play_btn = screen.blit(play_1,(0,240))
        options_btn = screen.blit(settings_1,(0,320))
        commandes_btn = screen.blit(commands_1,(0,405))
        credits_btn = screen.blit(credits_2,(0,490))
        pygame.display.flip()

def PairImpair(x):
    if x%2 == 0:
        return True
    if x%2 !=0:
        return False

def LoadingGame():
    for nb in range(3):
        screen_load_1 = screen.blit(loading_1,(0,0))
        pygame.display.flip()
        time.sleep(0.4)
        screen_load_2 = screen.blit(loading_2,(0,0))
        pygame.display.flip()
        time.sleep(0.4)
        screen_load_3 = screen.blit(loading_3,(0,0))
        pygame.display.flip()
        time.sleep(0.4)

def LuffyPos():
    if luffy_pos == luffy_d:
        screen_luffy = screen.blit(luffy_d_blur,(xluffy,yluffy))


#Lancement de la boucle Menu

menu_run = True
n = 0
x = 0
o = 0

if n == 0:
    LoadingMenu()

while menu_run:
    for event in pygame.event.get():
        if event.type == QUIT:
            menu_run = False
            pygame.quit()
            sys.exit()

        if back_r.collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN and n == 1:
            LoadingMenu()
            n = 0

        if play_r.collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN and n != 1:
            menu_run = False
            n = 2

        if settings_r.collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN and n != 1:
            if PairImpair(x) == False:
                Settings_on()
            if PairImpair(x) == True:
                Settings_off()
            n = 1
            o = 1

        if commands_r.collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN and n != 1:
            Commands()
            n = 1

        if credits_r.collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN and n != 1:
            Credits()
            n = 1

        if son_r.collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN and o == 1:
            if PairImpair(x) == True:
                Settings_on()
            if PairImpair(x) == False:
                Settings_off()
            x += 1
            print(x)

        if n == 0:
            o = 0

    WhichOneIsOnHover()
    pygame.display.flip()

#Chargement du jeu

LoadingGame()

#Lancemant de la boucle du jeu "In Game"

ingame = True
i = 0
xluffy = 824
yluffy = 349
luffy_pos = luffy_d

if i == 0:
    Play_intro()

while ingame:
    for event in pygame.event.get():
        if event.type == QUIT:
            ingame = False
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_RIGHT:
            luffy_pos = luffy_r
            xluffy += 8
            screen_wallpaper = screen.blit(game_intro,(0,0))
            screen_luffy = screen.blit(luffy_r1,(xluffy,yluffy))
            pygame.display.flip()
            time.sleep(0.075)

            if event.type == KEYDOWN and event.key == K_RIGHT:
                xluffy += 8
                screen_wallpaper = screen.blit(game_intro,(0,0))
                screen_luffy = screen.blit(luffy_r2,(xluffy,yluffy))
                pygame.display.flip()
                time.sleep(0.075)

                if event.type == KEYDOWN and event.key == K_RIGHT:
                    xluffy += 8
                    screen_wallpaper = screen.blit(game_intro,(0,0))
                    screen_luffy = screen.blit(luffy_r1,(xluffy,yluffy))
                    pygame.display.flip()
                    time.sleep(0.075)

                    if event.type == KEYDOWN and event.key == K_RIGHT:
                        xluffy += 8
                        screen_wallpaper = screen.blit(game_intro,(0,0))
                        screen_luffy = screen.blit(luffy_r,(xluffy,yluffy))
                        pygame.display.flip()
                        time.sleep(0.075)

                        if event.type == KEYDOWN and event.key == K_RIGHT:
                            xluffy += 8
                            screen_wallpaper = screen.blit(game_intro,(0,0))
                            screen_luffy = screen.blit(luffy_r3,(xluffy,yluffy))
                            pygame.display.flip()
                            time.sleep(0.075)

                            if event.type == KEYDOWN and event.key == K_RIGHT:
                                xluffy += 8
                                screen_wallpaper = screen.blit(game_intro,(0,0))
                                screen_luffy = screen.blit(luffy_r4,(xluffy,yluffy))
                                pygame.display.flip()
                                time.sleep(0.075)

                                if event.type == KEYDOWN and event.key == K_RIGHT:
                                    xluffy += 8
                                    screen_wallpaper = screen.blit(game_intro,(0,0))
                                    screen_luffy = screen.blit(luffy_r3,(xluffy,yluffy))
                                    pygame.display.flip()
                                    time.sleep(0.075)

                                    if event.type == KEYDOWN and event.key == K_RIGHT:
                                        xluffy += 8
                                        screen_wallpaper = screen.blit(game_intro,(0,0))
                                        screen_luffy = screen.blit(luffy_r,(xluffy,yluffy))
                                        pygame.display.flip()
                                        time.sleep(0.075)


        if event.type == KEYDOWN and event.key == K_LEFT:
            luffy_pos = luffy_l
            xluffy -= 8
            screen_wallpaper = screen.blit(game_intro,(0,0))
            screen_luffy = screen.blit(luffy_l1,(xluffy,yluffy))
            pygame.display.flip()
            time.sleep(0.075)

            if event.type == KEYDOWN and event.key == K_LEFT:
                xluffy -= 8
                screen_wallpaper = screen.blit(game_intro,(0,0))
                screen_luffy = screen.blit(luffy_l2,(xluffy,yluffy))
                pygame.display.flip()
                time.sleep(0.075)

                if event.type == KEYDOWN and event.key == K_LEFT:
                    xluffy -= 8
                    screen_wallpaper = screen.blit(game_intro,(0,0))
                    screen_luffy = screen.blit(luffy_l1,(xluffy,yluffy))
                    pygame.display.flip()
                    time.sleep(0.075)

                    if event.type == KEYDOWN and event.key == K_LEFT:
                        xluffy -= 8
                        screen_wallpaper = screen.blit(game_intro,(0,0))
                        screen_luffy = screen.blit(luffy_l,(xluffy,yluffy))
                        pygame.display.flip()
                        time.sleep(0.075)

                        if event.type == KEYDOWN and event.key == K_LEFT:
                            xluffy -= 8
                            screen_wallpaper = screen.blit(game_intro,(0,0))
                            screen_luffy = screen.blit(luffy_l3,(xluffy,yluffy))
                            pygame.display.flip()
                            time.sleep(0.075)

                            if event.type == KEYDOWN and event.key == K_LEFT:
                                xluffy -= 8
                                screen_wallpaper = screen.blit(game_intro,(0,0))
                                screen_luffy = screen.blit(luffy_l4,(xluffy,yluffy))
                                pygame.display.flip()
                                time.sleep(0.075)

                                if event.type == KEYDOWN and event.key == K_LEFT:
                                    xluffy -= 8
                                    screen_wallpaper = screen.blit(game_intro,(0,0))
                                    screen_luffy = screen.blit(luffy_l3,(xluffy,yluffy))
                                    pygame.display.flip()
                                    time.sleep(0.075)

                                    if event.type == KEYDOWN and event.key == K_LEFT:
                                        xluffy -= 8
                                        screen_wallpaper = screen.blit(game_intro,(0,0))
                                        screen_luffy = screen.blit(luffy_l,(xluffy,yluffy))
                                        pygame.display.flip()
                                        time.sleep(0.075)


        if event.type == KEYDOWN and event.key == K_UP:
            luffy_pos = luffy_u
            yluffy -= 5
            screen_wallpaper = screen.blit(game_intro,(0,0))
            screen_luffy = screen.blit(luffy_u1,(xluffy,yluffy))
            pygame.display.flip()
            time.sleep(0.075)

            if event.type == KEYDOWN and event.key == K_UP:
                yluffy -= 5
                screen_wallpaper = screen.blit(game_intro,(0,0))
                screen_luffy = screen.blit(luffy_u2,(xluffy,yluffy))
                pygame.display.flip()
                time.sleep(0.075)

                if event.type == KEYDOWN and event.key == K_UP:
                    yluffy -= 5
                    screen_wallpaper = screen.blit(game_intro,(0,0))
                    screen_luffy = screen.blit(luffy_u1,(xluffy,yluffy))
                    pygame.display.flip()
                    time.sleep(0.075)

                    if event.type == KEYDOWN and event.key == K_UP:
                        yluffy -= 5
                        screen_wallpaper = screen.blit(game_intro,(0,0))
                        screen_luffy = screen.blit(luffy_u,(xluffy,yluffy))
                        pygame.display.flip()
                        time.sleep(0.075)

                        if event.type == KEYDOWN and event.key == K_UP:
                            yluffy -= 5
                            screen_wallpaper = screen.blit(game_intro,(0,0))
                            screen_luffy = screen.blit(luffy_u3,(xluffy,yluffy))
                            pygame.display.flip()
                            time.sleep(0.075)

                            if event.type == KEYDOWN and event.key == K_UP:
                                yluffy -= 5
                                screen_wallpaper = screen.blit(game_intro,(0,0))
                                screen_luffy = screen.blit(luffy_u4,(xluffy,yluffy))
                                pygame.display.flip()
                                time.sleep(0.075)

                                if event.type == KEYDOWN and event.key == K_UP:
                                    yluffy -= 5
                                    screen_wallpaper = screen.blit(game_intro,(0,0))
                                    screen_luffy = screen.blit(luffy_u3,(xluffy,yluffy))
                                    pygame.display.flip()
                                    time.sleep(0.075)

                                    if event.type == KEYDOWN and event.key == K_UP:
                                        yluffy -= 5
                                        screen_wallpaper = screen.blit(game_intro,(0,0))
                                        screen_luffy = screen.blit(luffy_u,(xluffy,yluffy))
                                        pygame.display.flip()
                                        time.sleep(0.075)


        if event.type == KEYDOWN and event.key == K_DOWN:
            luffy_pos = luffy_d
            yluffy += 5
            screen_wallpaper = screen.blit(game_intro,(0,0))
            screen_luffy = screen.blit(luffy_d1,(xluffy,yluffy))
            pygame.display.flip()
            time.sleep(0.075)

            if event.type == KEYDOWN and event.key == K_DOWN:
                yluffy += 5
                screen_wallpaper = screen.blit(game_intro,(0,0))
                screen_luffy = screen.blit(luffy_d2,(xluffy,yluffy))
                pygame.display.flip()
                time.sleep(0.075)

                if event.type == KEYDOWN and event.key == K_DOWN:
                    yluffy += 5
                    screen_wallpaper = screen.blit(game_intro,(0,0))
                    screen_luffy = screen.blit(luffy_d1,(xluffy,yluffy))
                    pygame.display.flip()
                    time.sleep(0.075)

                    if event.type == KEYDOWN and event.key == K_DOWN:
                        yluffy += 5
                        screen_wallpaper = screen.blit(game_intro,(0,0))
                        screen_luffy = screen.blit(luffy_d,(xluffy,yluffy))
                        pygame.display.flip()
                        time.sleep(0.075)

                        if event.type == KEYDOWN and event.key == K_DOWN:
                            yluffy += 5
                            screen_wallpaper = screen.blit(game_intro,(0,0))
                            screen_luffy = screen.blit(luffy_d3,(xluffy,yluffy))
                            pygame.display.flip()
                            time.sleep(0.075)

                            if event.type == KEYDOWN and event.key == K_DOWN:
                                yluffy += 5
                                screen_wallpaper = screen.blit(game_intro,(0,0))
                                screen_luffy = screen.blit(luffy_d4,(xluffy,yluffy))
                                pygame.display.flip()
                                time.sleep(0.075)

                                if event.type == KEYDOWN and event.key == K_DOWN:
                                    yluffy += 5
                                    screen_wallpaper = screen.blit(game_intro,(0,0))
                                    screen_luffy = screen.blit(luffy_d3,(xluffy,yluffy))
                                    pygame.display.flip()
                                    time.sleep(0.075)

                                    if event.type == KEYDOWN and event.key == K_DOWN:
                                        yluffy += 5
                                        screen_wallpaper = screen.blit(game_intro,(0,0))
                                        screen_luffy = screen.blit(luffy_d,(xluffy,yluffy))
                                        pygame.display.flip()
                                        time.sleep(0.075)
