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
first_house = pygame.image.load("pictures/first_house.png").convert()
second_house = pygame.image.load("pictures/second_house.png").convert()
up_house = pygame.image.load("pictures/up_house.png").convert()

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

mcdo = pygame.image.load("pictures/items/mcdo.png").convert_alpha()
mcdo2 = pygame.image.load("pictures/items/mcdo2.png").convert_alpha()
mcdo3 = pygame.image.load("pictures/items/mcdo3.png").convert_alpha()
mcdo4 = pygame.image.load("pictures/items/mcdo4.png").convert_alpha()

potion = pygame.image.load("pictures/items/potion.png").convert_alpha()
potion2 = pygame.image.load("pictures/items/potion2.png").convert_alpha()
potion3 = pygame.image.load("pictures/items/potion3.png").convert_alpha()
potion4 = pygame.image.load("pictures/items/potion4.png").convert_alpha()

shield = pygame.image.load("pictures/items/shield.png").convert_alpha()
shield2 = pygame.image.load("pictures/items/shield2.png").convert_alpha()
shield3 = pygame.image.load("pictures/items/shield3.png").convert_alpha()
shield4 = pygame.image.load("pictures/items/shield4.png").convert_alpha()

sword = pygame.image.load("pictures/items/sword.png").convert_alpha()
sword2 = pygame.image.load("pictures/items/sword2.png").convert_alpha()
sword3 = pygame.image.load("pictures/items/sword3.png").convert_alpha()
sword4 = pygame.image.load("pictures/items/sword4.png").convert_alpha()

nothing = pygame.image.load("pictures/nothing.png").convert_alpha()

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
    sword_display = screen.blit(sword,(254,128))
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

xleft_upforest1 = 56
xleft_upforest2 = 184
yleft_upforest = 229

xleft_house1 = 248
xleft_house2 = 568
yleft_house = 189

xstairs = 504
ystairs = 109

xright_house1 = 632
xright_house2 = 824
yright_house = 269

xleft_stairs = 504
yleft_stairs = 149

xleft_downforest1 = 56
xleft_downforest2 = 120
yleft_downforest = 349

xmiddle_downforest1 = 184
xmiddle_downforest2 = 760
ymiddle_downforest = 469

xright_downforest = 824
yright_downforest = 349

yleft_forestborder1_1 = 229
yleft_forestborder1_2 = 349
xleft_forestborder1 = 56

yleft_forestborder2_1 = 389
yleft_forestborder2_2 = 469
xleft_forestborder2 = 184

yleft_forestborder3_1 = 109
yleft_forestborder3_2 = 189
xleft_forestborder3 = 248

yright_righthouse1 = 189
yright_righthouse2 = 229
xright_righthouse = 568

yright_forest1 = 389
yright_forest2 = 469
xright_forest = 760

yright_map1 = 269
yright_map2 = 349
xright_map = 824

def left_upforest():
    if xluffy >= xleft_upforest1 and xluffy <= xleft_upforest2 and yluffy > yleft_upforest:
        return True
    else:
        return False

def left_house():
    if xluffy >= xleft_house1 and xluffy <= xleft_house2 and yluffy > yleft_house:
        return True
    else:
        return False

def stairs():
    if xluffy == xstairs and yluffy > ystairs:
        return True
    else:
        return False

def right_house():
    if xluffy >= xright_house1 and xluffy <= xright_house2 and yluffy > yright_house:
        return True
    else:
        return False

def left_downforest():
    if xluffy >= xleft_downforest1 and xluffy <= xleft_downforest2 and yluffy < yleft_downforest:
        return True
    else:
        return False

def middle_downforest():
    if xluffy >= xmiddle_downforest1 and xluffy <= xmiddle_downforest2 and yluffy < ymiddle_downforest:
        return True
    else:
        return False

def right_downforest():
    if xluffy == xright_downforest and yluffy < yright_downforest:
        return True
    else:
        return False

def left_stairs():
    if xluffy == xleft_stairs and yluffy == yleft_stairs:
        return False

def left_forestborder1():
    if yluffy >= yleft_forestborder1_1 and yluffy <= yleft_forestborder1_2 and xluffy > xleft_forestborder1:
        return True
    else:
        return False

def left_forestborder2():
    if yluffy >= yleft_forestborder2_1 and yluffy <= yleft_forestborder2_2 and xluffy > xleft_forestborder2:
        return True
    else:
        return False

def left_forestborder3():
    if yluffy >= yleft_forestborder3_1 and yluffy <= yleft_forestborder3_2 and xluffy > xleft_forestborder3:
        return True
    else:
        return False

def right_righthouse():
    if yluffy >= yright_righthouse1 and yluffy <= yright_righthouse2 and xluffy < xright_righthouse:
        return True
    else:
        return False

def right_forest():
    if yluffy >= yright_forest1 and yluffy <= yright_forest2 and xluffy < xright_forest:
        return True
    else:
        return False

def right_map():
    if yluffy >= yright_map1 and yluffy <= yright_map2 and xluffy < xright_map:
        return True
    else:
        return False

def inHouse1():
    global lc
    if lc == 1:
        potion_display = screen.blit(potion,(542,163))

def inHouse2():
    global lc
    if lc == 2:
        mcdo_display = screen.blit(mcdo,(371,140))

def inUphouse():
    global lc
    if lc == 3:
        shield_display = screen.blit(shield,(400,207))

def outdoor():
    global lc
    if lc == 0:
        sword_display = screen.blit(sword,(254,128))

mcdo_list = [mcdo2, mcdo3, mcdo4]
potion_list = [potion2, potion3, potion4]
shield_list = [shield2, shield3, shield4]
sword_list = [sword2, sword3, sword4]

def mcdo_found():
    for i in range(3):
        screen_wallpaper = screen.blit(game_intro,(0,0))
        screen.blit(mcdo_list[i],(371,140))
        screen_luffy = screen.blit(luffy_u,(xluffy,yluffy))
        pygame.display.update()
        time.sleep(0.2)
    screen_wallpaper = screen.blit(game_intro,(0,0))
    screen_luffy = screen.blit(luffy_u,(xluffy,yluffy))
    pygame.display.update()

def potion_found():
    for i in range(3):
        screen_wallpaper = screen.blit(game_intro,(0,0))
        screen.blit(potion_list[i],(542,163))
        screen_luffy = screen.blit(luffy_u,(xluffy,yluffy))
        pygame.display.update()
        time.sleep(0.2)
    screen_wallpaper = screen.blit(game_intro,(0,0))
    screen_luffy = screen.blit(luffy_u,(xluffy,yluffy))
    pygame.display.update()

def shield_found():
    for i in range(3):
        screen_wallpaper = screen.blit(game_intro,(0,0))
        screen.blit(shield_list[i],(400,207))
        screen_luffy = screen.blit(luffy_u,(xluffy,yluffy))
        pygame.display.update()
        time.sleep(0.2)
    screen_wallpaper = screen.blit(game_intro,(0,0))
    screen_luffy = screen.blit(luffy_u,(xluffy,yluffy))
    pygame.display.update()

def sword_found():
    for i in range(3):
        screen_wallpaper = screen.blit(game_intro,(0,0))
        screen.blit(sword_list[i],(254,128))
        screen_luffy = screen.blit(luffy_u,(xluffy,yluffy))
        pygame.display.update()
        time.sleep(0.2)
    screen_wallpaper = screen.blit(game_intro,(0,0))
    screen_luffy = screen.blit(luffy_u,(xluffy,yluffy))
    pygame.display.update()


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
s1 = 0
lc = 0
itm_mcdo = 0
itm_potion = 0
itm_shield = 0
itm_sword = 0
xluffy = 824
yluffy = 349
luffy_pos = luffy_d

Play_intro()

while ingame:
    for event in pygame.event.get():
        if event.type == QUIT:
            ingame = False
            pygame.quit()
            sys.exit()

        if xluffy == 56 and yluffy == 309 or yluffy == 349 and event.type == KEYDOWN and event.key == K_LEFT:
            if itm_mcdo and itm_potion and itm_shield and itm_sword == 1:
                LoadingGame()
                ingame = False
                pygame.quit()
                sys.exit()

        if xluffy == 371 and yluffy == 173 and lc == 2 and itm_mcdo == 0:
            mcdo_found()
            itm_mcdo = 1
            mcdo = nothing

        if xluffy == 540 and yluffy == 174 and lc == 1 and itm_potion == 0:
            potion_found()
            itm_potion = 1
            potion = nothing

        if xluffy == 400 and yluffy == 230 and lc == 3 and itm_shield == 0:
            shield_found()
            itm_shield = 1
            shield = nothing

        if xluffy == 248 and yluffy == 149 and lc == 0 and itm_sword == 0:
            sword_found()
            itm_sword = 1
            sword = nothing

        if xluffy == 696 and yluffy == 269 and event.type == KEYDOWN and event.key == K_UP:
            s1 += 1
            lc = 2

            xleft_upforest1 = 243
            xleft_upforest2 = 691
            yleft_upforest = 173

            xleft_house1 = 243
            xleft_house2 = 691
            yleft_house = 173

            xstairs = 0
            ystairs = 0

            xright_house1 = 243
            xright_house2 = 691
            yright_house = 173

            xleft_downforest1 = 243
            xleft_downforest2 = 243
            yleft_downforest = 333

            xmiddle_downforest1 = 307
            xmiddle_downforest2 = 627
            ymiddle_downforest = 413

            xright_downforest = 691
            yright_downforest = 333

            xleft_stairs = 0
            yleft_stairs = 0

            yleft_forestborder1_1 = 373
            yleft_forestborder1_2 = 413
            xleft_forestborder1 = 307

            yleft_forestborder2_1 = 173
            yleft_forestborder2_2 = 333
            xleft_forestborder2 = 243

            yleft_forestborder3_1 = 173
            yleft_forestborder3_2 = 333
            xleft_forestborder3 = 243

            yright_righthouse1 = 373
            yright_righthouse2 = 413
            xright_righthouse = 627

            yright_forest1 = 173
            yright_forest2 = 333
            xright_forest = 691

            yright_map1 = 173
            yright_map2 = 333
            xright_map = 691

            if s1 == 1:
                game_intro = second_house
                screen_wallpaper = screen.blit(game_intro,(0,0))
                mcdo_display = screen.blit(mcdo,(371,140))
                xluffy = 435
                yluffy = 413
                screen_luffy = screen.blit(luffy_u,(xluffy,yluffy))
                pygame.display.flip()

        if xluffy == 435 and yluffy == 413 and event.type == KEYDOWN and event.key == K_DOWN and s1 == 1:
            s1 = 0
            lc = 0

            xleft_upforest1 = 56
            xleft_upforest2 = 184
            yleft_upforest = 229

            xleft_house1 = 248
            xleft_house2 = 568
            yleft_house = 189

            xstairs = 504
            ystairs = 109

            xright_house1 = 632
            xright_house2 = 824
            yright_house = 269

            xleft_downforest1 = 56
            xleft_downforest2 = 120
            yleft_downforest = 349

            xmiddle_downforest1 = 184
            xmiddle_downforest2 = 760
            ymiddle_downforest = 469

            xright_downforest = 824
            yright_downforest = 349

            xleft_stairs = 504
            yleft_stairs = 149

            yleft_forestborder1_1 = 229
            yleft_forestborder1_2 = 349
            xleft_forestborder1 = 56

            yleft_forestborder2_1 = 389
            yleft_forestborder2_2 = 469
            xleft_forestborder2 = 184

            yleft_forestborder3_1 = 109
            yleft_forestborder3_2 = 189
            xleft_forestborder3 = 248

            yright_righthouse1 = 189
            yright_righthouse2 = 229
            xright_righthouse = 568

            yright_forest1 = 389
            yright_forest2 = 469
            xright_forest = 760

            yright_map1 = 269
            yright_map2 = 349
            xright_map = 824

            game_intro = pygame.image.load("pictures/game_intro.png").convert()
            screen_wallpaper = screen.blit(game_intro,(0,0))
            sword_display = screen.blit(sword,(254,128))
            xluffy = 696
            yluffy = 269
            screen_luffy = screen.blit(luffy_d,(xluffy,yluffy))
            pygame.display.flip()

        if xluffy == 376 and yluffy == 189 and event.type == KEYDOWN and event.key == K_UP:
            s1 += 1
            lc = 1

            xleft_upforest1 = 284
            xleft_upforest2 = 668
            yleft_upforest = 174

            xleft_house1 = 284
            xleft_house2 = 668
            yleft_house = 174

            xstairs = 0
            ystairs = 0

            xright_house1 = 284
            xright_house2 = 668
            yright_house = 174

            xleft_downforest1 = 284
            xleft_downforest2 = 284
            yleft_downforest = 334

            xmiddle_downforest1 = 348
            xmiddle_downforest2 = 668
            ymiddle_downforest = 414

            xright_downforest = 0
            yright_downforest = 0

            xleft_stairs = 0
            yleft_stairs = 0

            yleft_forestborder1_1 = 374
            yleft_forestborder1_2 = 414
            xleft_forestborder1 = 348

            yleft_forestborder2_1 = 174
            yleft_forestborder2_2 = 334
            xleft_forestborder2 = 284

            yleft_forestborder3_1 = 174
            yleft_forestborder3_2 = 334
            xleft_forestborder3 = 284

            yright_righthouse1 = 174
            yright_righthouse2 = 414
            xright_righthouse = 668

            yright_forest1 = 174
            yright_forest2 = 414
            xright_forest = 668

            yright_map1 = 174
            yright_map2 = 414
            xright_map = 668

            if s1 == 1:
                game_intro = first_house
                screen_wallpaper = screen.blit(game_intro,(0,0))
                potion_display = screen.blit(potion,(542,163))
                xluffy = 540
                yluffy = 414
                screen_luffy = screen.blit(luffy_u,(xluffy,yluffy))
                pygame.display.flip()

        if xluffy == 540 and yluffy == 414 and event.type == KEYDOWN and event.key == K_DOWN and s1 == 1:
            s1 = 0
            lc = 0

            xleft_upforest1 = 56
            xleft_upforest2 = 184
            yleft_upforest = 229

            xleft_house1 = 248
            xleft_house2 = 568
            yleft_house = 189

            xstairs = 504
            ystairs = 109

            xright_house1 = 632
            xright_house2 = 824
            yright_house = 269

            xleft_downforest1 = 56
            xleft_downforest2 = 120
            yleft_downforest = 349

            xmiddle_downforest1 = 184
            xmiddle_downforest2 = 760
            ymiddle_downforest = 469

            xright_downforest = 824
            yright_downforest = 349

            xleft_stairs = 504
            yleft_stairs = 149

            yleft_forestborder1_1 = 229
            yleft_forestborder1_2 = 349
            xleft_forestborder1 = 56

            yleft_forestborder2_1 = 389
            yleft_forestborder2_2 = 469
            xleft_forestborder2 = 184

            yleft_forestborder3_1 = 109
            yleft_forestborder3_2 = 189
            xleft_forestborder3 = 248

            yright_righthouse1 = 189
            yright_righthouse2 = 229
            xright_righthouse = 568

            yright_forest1 = 389
            yright_forest2 = 469
            xright_forest = 760

            yright_map1 = 269
            yright_map2 = 349
            xright_map = 824

            game_intro = pygame.image.load("pictures/game_intro.png").convert()
            screen_wallpaper = screen.blit(game_intro,(0,0))
            sword_display = screen.blit(sword,(254,128))
            xluffy = 376
            yluffy = 189
            screen_luffy = screen.blit(luffy_d,(xluffy,yluffy))
            pygame.display.flip()

        if xluffy == 504 and yluffy == 109 and event.type == KEYDOWN and event.key == K_LEFT:
            s1 += 1
            lc = 3

            xleft_upforest1 = 272
            xleft_upforest2 = 592
            yleft_upforest = 230

            xleft_house1 = 272
            xleft_house2 = 592
            yleft_house = 230

            xstairs = 656
            ystairs = 270

            xright_house1 = 272
            xright_house2 = 592
            yright_house = 230

            xleft_stairs = 0
            yleft_stairs = 0

            xleft_downforest1 = 272
            xleft_downforest2 = 592
            yleft_downforest = 430

            xmiddle_downforest1 = 272
            xmiddle_downforest2 = 592
            ymiddle_downforest = 430

            xright_downforest = 656
            yright_downforest = 310

            yleft_forestborder1_1 = 230
            yleft_forestborder1_2 = 440
            xleft_forestborder1 = 272

            yleft_forestborder2_1 = 230
            yleft_forestborder2_2 = 440
            xleft_forestborder2 = 272

            yleft_forestborder3_1 = 230
            yleft_forestborder3_2 = 440
            xleft_forestborder3 = 272

            yright_righthouse1 = 230
            yright_righthouse2 = 230
            xright_righthouse = 592

            yright_forest1 = 350
            yright_forest2 = 430
            xright_forest = 592

            yright_map1 = 270
            yright_map2 = 310
            xright_map = 656

            if s1 == 1:
                game_intro = up_house
                screen_wallpaper = screen.blit(game_intro,(0,0))
                shield_display = screen.blit(shield,(400,207))
                xluffy = 592
                yluffy = 230
                screen_luffy = screen.blit(luffy_l,(xluffy,yluffy))
                pygame.display.flip()

        if xluffy == 592 and yluffy == 230 and event.type == KEYDOWN and event.key == K_RIGHT and s1 == 1:
            s1 = 0
            lc = 0

            xleft_upforest1 = 56
            xleft_upforest2 = 184
            yleft_upforest = 229

            xleft_house1 = 248
            xleft_house2 = 568
            yleft_house = 189

            xstairs = 504
            ystairs = 109

            xright_house1 = 632
            xright_house2 = 824
            yright_house = 269

            xleft_downforest1 = 56
            xleft_downforest2 = 120
            yleft_downforest = 349

            xmiddle_downforest1 = 184
            xmiddle_downforest2 = 760
            ymiddle_downforest = 469

            xright_downforest = 824
            yright_downforest = 349

            xleft_stairs = 504
            yleft_stairs =149

            yleft_forestborder1_1 = 229
            yleft_forestborder1_2 = 349
            xleft_forestborder1 = 56

            yleft_forestborder2_1 = 389
            yleft_forestborder2_2 = 469
            xleft_forestborder2 = 184

            yleft_forestborder3_1 = 109
            yleft_forestborder3_2 = 189
            xleft_forestborder3 = 248

            yright_righthouse1 = 189
            yright_righthouse2 = 229
            xright_righthouse = 568

            yright_forest1 = 389
            yright_forest2 = 469
            xright_forest = 760

            yright_map1 = 269
            yright_map2 = 349
            xright_map = 824

            game_intro = pygame.image.load("pictures/game_intro.png").convert()
            screen_wallpaper = screen.blit(game_intro,(0,0))
            sword_display = screen.blit(sword,(254,128))
            xluffy = 504
            yluffy = 109
            screen_luffy = screen.blit(luffy_d,(xluffy,yluffy))
            pygame.display.flip()

        if event.type == KEYDOWN and event.key == K_RIGHT:
            if right_righthouse() or right_forest() or right_map():
                luffy_pos = luffy_r
                xluffy += 8
                screen_wallpaper = screen.blit(game_intro,(0,0))
                inHouse1()
                inHouse2()
                inUphouse()
                outdoor()
                screen_luffy = screen.blit(luffy_r1,(xluffy,yluffy))
                pygame.display.flip()
                time.sleep(0.075)

                if event.type == KEYDOWN and event.key == K_RIGHT:
                    xluffy += 8
                    screen_wallpaper = screen.blit(game_intro,(0,0))
                    inHouse1()
                    inHouse2()
                    inUphouse()
                    outdoor()
                    screen_luffy = screen.blit(luffy_r2,(xluffy,yluffy))
                    pygame.display.flip()
                    time.sleep(0.075)

                    if event.type == KEYDOWN and event.key == K_RIGHT:
                        xluffy += 8
                        screen_wallpaper = screen.blit(game_intro,(0,0))
                        inHouse1()
                        inHouse2()
                        inUphouse()
                        outdoor()
                        screen_luffy = screen.blit(luffy_r1,(xluffy,yluffy))
                        pygame.display.flip()
                        time.sleep(0.075)

                        if event.type == KEYDOWN and event.key == K_RIGHT:
                            xluffy += 8
                            screen_wallpaper = screen.blit(game_intro,(0,0))
                            inHouse1()
                            inHouse2()
                            inUphouse()
                            outdoor()
                            screen_luffy = screen.blit(luffy_r,(xluffy,yluffy))
                            pygame.display.flip()
                            time.sleep(0.075)

                            if event.type == KEYDOWN and event.key == K_RIGHT:
                                xluffy += 8
                                screen_wallpaper = screen.blit(game_intro,(0,0))
                                inHouse1()
                                inHouse2()
                                inUphouse()
                                outdoor()
                                screen_luffy = screen.blit(luffy_r3,(xluffy,yluffy))
                                pygame.display.flip()
                                time.sleep(0.075)

                                if event.type == KEYDOWN and event.key == K_RIGHT:
                                    xluffy += 8
                                    screen_wallpaper = screen.blit(game_intro,(0,0))
                                    inHouse1()
                                    inHouse2()
                                    inUphouse()
                                    outdoor()
                                    screen_luffy = screen.blit(luffy_r4,(xluffy,yluffy))
                                    pygame.display.flip()
                                    time.sleep(0.075)

                                    if event.type == KEYDOWN and event.key == K_RIGHT:
                                        xluffy += 8
                                        screen_wallpaper = screen.blit(game_intro,(0,0))
                                        inHouse1()
                                        inHouse2()
                                        inUphouse()
                                        outdoor()
                                        screen_luffy = screen.blit(luffy_r3,(xluffy,yluffy))
                                        pygame.display.flip()
                                        time.sleep(0.075)

                                        if event.type == KEYDOWN and event.key == K_RIGHT:
                                            xluffy += 8
                                            screen_wallpaper = screen.blit(game_intro,(0,0))
                                            inHouse1()
                                            inHouse2()
                                            inUphouse()
                                            outdoor()
                                            screen_luffy = screen.blit(luffy_r,(xluffy,yluffy))
                                            pygame.display.flip()
                                            time.sleep(0.075)

        print(xluffy)
        print(yluffy)


        if event.type == KEYDOWN and event.key == K_LEFT:
            if left_forestborder1() or left_forestborder2() or left_forestborder3() or left_stairs():
                luffy_pos = luffy_l
                xluffy -= 8
                screen_wallpaper = screen.blit(game_intro,(0,0))
                inHouse1()
                inHouse2()
                inUphouse()
                outdoor()
                screen_luffy = screen.blit(luffy_l1,(xluffy,yluffy))
                pygame.display.flip()
                time.sleep(0.075)

                if event.type == KEYDOWN and event.key == K_LEFT:
                    xluffy -= 8
                    screen_wallpaper = screen.blit(game_intro,(0,0))
                    inHouse1()
                    inHouse2()
                    inUphouse()
                    outdoor()
                    screen_luffy = screen.blit(luffy_l2,(xluffy,yluffy))
                    pygame.display.flip()
                    time.sleep(0.075)

                    if event.type == KEYDOWN and event.key == K_LEFT:
                        xluffy -= 8
                        screen_wallpaper = screen.blit(game_intro,(0,0))
                        inHouse1()
                        inHouse2()
                        inUphouse()
                        outdoor()
                        screen_luffy = screen.blit(luffy_l1,(xluffy,yluffy))
                        pygame.display.flip()
                        time.sleep(0.075)

                        if event.type == KEYDOWN and event.key == K_LEFT:
                            xluffy -= 8
                            screen_wallpaper = screen.blit(game_intro,(0,0))
                            inHouse1()
                            inHouse2()
                            inUphouse()
                            outdoor()
                            screen_luffy = screen.blit(luffy_l,(xluffy,yluffy))
                            pygame.display.flip()
                            time.sleep(0.075)

                            if event.type == KEYDOWN and event.key == K_LEFT:
                                xluffy -= 8
                                screen_wallpaper = screen.blit(game_intro,(0,0))
                                inHouse1()
                                inHouse2()
                                inUphouse()
                                outdoor()
                                screen_luffy = screen.blit(luffy_l3,(xluffy,yluffy))
                                pygame.display.flip()
                                time.sleep(0.075)

                                if event.type == KEYDOWN and event.key == K_LEFT:
                                    xluffy -= 8
                                    screen_wallpaper = screen.blit(game_intro,(0,0))
                                    inHouse1()
                                    inHouse2()
                                    inUphouse()
                                    outdoor()
                                    screen_luffy = screen.blit(luffy_l4,(xluffy,yluffy))
                                    pygame.display.flip()
                                    time.sleep(0.075)

                                    if event.type == KEYDOWN and event.key == K_LEFT:
                                        xluffy -= 8
                                        screen_wallpaper = screen.blit(game_intro,(0,0))
                                        inHouse1()
                                        inHouse2()
                                        inUphouse()
                                        outdoor()
                                        screen_luffy = screen.blit(luffy_l3,(xluffy,yluffy))
                                        pygame.display.flip()
                                        time.sleep(0.075)

                                        if event.type == KEYDOWN and event.key == K_LEFT:
                                            xluffy -= 8
                                            screen_wallpaper = screen.blit(game_intro,(0,0))
                                            inHouse1()
                                            inHouse2()
                                            inUphouse()
                                            outdoor()
                                            screen_luffy = screen.blit(luffy_l,(xluffy,yluffy))
                                            pygame.display.flip()
                                            time.sleep(0.075)

        print(xluffy)
        print(yluffy)


        if event.type == KEYDOWN and event.key == K_UP:
            if left_upforest() or left_house() or right_house() or stairs():
                luffy_pos = luffy_u
                yluffy -= 5
                screen_wallpaper = screen.blit(game_intro,(0,0))
                inHouse1()
                inHouse2()
                inUphouse()
                outdoor()
                screen_luffy = screen.blit(luffy_u1,(xluffy,yluffy))
                pygame.display.flip()
                time.sleep(0.075)

                if event.type == KEYDOWN and event.key == K_UP:
                    yluffy -= 5
                    screen_wallpaper = screen.blit(game_intro,(0,0))
                    inHouse1()
                    inHouse2()
                    inUphouse()
                    outdoor()
                    screen_luffy = screen.blit(luffy_u2,(xluffy,yluffy))
                    pygame.display.flip()
                    time.sleep(0.075)

                    if event.type == KEYDOWN and event.key == K_UP:
                        yluffy -= 5
                        screen_wallpaper = screen.blit(game_intro,(0,0))
                        inHouse1()
                        inHouse2()
                        inUphouse()
                        outdoor()
                        screen_luffy = screen.blit(luffy_u1,(xluffy,yluffy))
                        pygame.display.flip()
                        time.sleep(0.075)

                        if event.type == KEYDOWN and event.key == K_UP:
                            yluffy -= 5
                            screen_wallpaper = screen.blit(game_intro,(0,0))
                            inHouse1()
                            inHouse2()
                            inUphouse()
                            outdoor()
                            screen_luffy = screen.blit(luffy_u,(xluffy,yluffy))
                            pygame.display.flip()
                            time.sleep(0.075)

                            if event.type == KEYDOWN and event.key == K_UP:
                                yluffy -= 5
                                screen_wallpaper = screen.blit(game_intro,(0,0))
                                inHouse1()
                                inHouse2()
                                inUphouse()
                                outdoor()
                                screen_luffy = screen.blit(luffy_u3,(xluffy,yluffy))
                                pygame.display.flip()
                                time.sleep(0.075)

                                if event.type == KEYDOWN and event.key == K_UP:
                                    yluffy -= 5
                                    screen_wallpaper = screen.blit(game_intro,(0,0))
                                    inHouse1()
                                    inHouse2()
                                    inUphouse()
                                    outdoor()
                                    screen_luffy = screen.blit(luffy_u4,(xluffy,yluffy))
                                    pygame.display.flip()
                                    time.sleep(0.075)

                                    if event.type == KEYDOWN and event.key == K_UP:
                                        yluffy -= 5
                                        screen_wallpaper = screen.blit(game_intro,(0,0))
                                        inHouse1()
                                        inHouse2()
                                        inUphouse()
                                        outdoor()
                                        screen_luffy = screen.blit(luffy_u3,(xluffy,yluffy))
                                        pygame.display.flip()
                                        time.sleep(0.075)

                                        if event.type == KEYDOWN and event.key == K_UP:
                                            yluffy -= 5
                                            screen_wallpaper = screen.blit(game_intro,(0,0))
                                            inHouse1()
                                            inHouse2()
                                            inUphouse()
                                            outdoor()
                                            screen_luffy = screen.blit(luffy_u,(xluffy,yluffy))
                                            pygame.display.flip()
                                            time.sleep(0.075)


        print(xluffy)
        print(yluffy)


        if event.type == KEYDOWN and event.key == K_DOWN:
            if left_downforest() or middle_downforest() or right_downforest():
                luffy_pos = luffy_d
                yluffy += 5
                screen_wallpaper = screen.blit(game_intro,(0,0))
                inHouse1()
                inHouse2()
                inUphouse()
                outdoor()
                screen_luffy = screen.blit(luffy_d1,(xluffy,yluffy))
                pygame.display.flip()
                time.sleep(0.075)

                if event.type == KEYDOWN and event.key == K_DOWN:
                    yluffy += 5
                    screen_wallpaper = screen.blit(game_intro,(0,0))
                    inHouse1()
                    inHouse2()
                    inUphouse()
                    outdoor()
                    screen_luffy = screen.blit(luffy_d2,(xluffy,yluffy))
                    pygame.display.flip()
                    time.sleep(0.075)

                    if event.type == KEYDOWN and event.key == K_DOWN:
                        yluffy += 5
                        screen_wallpaper = screen.blit(game_intro,(0,0))
                        inHouse1()
                        inHouse2()
                        inUphouse()
                        outdoor()
                        screen_luffy = screen.blit(luffy_d1,(xluffy,yluffy))
                        pygame.display.flip()
                        time.sleep(0.075)

                        if event.type == KEYDOWN and event.key == K_DOWN:
                            yluffy += 5
                            screen_wallpaper = screen.blit(game_intro,(0,0))
                            inHouse1()
                            inHouse2()
                            inUphouse()
                            outdoor()
                            screen_luffy = screen.blit(luffy_d,(xluffy,yluffy))
                            pygame.display.flip()
                            time.sleep(0.075)

                            if event.type == KEYDOWN and event.key == K_DOWN:
                                yluffy += 5
                                screen_wallpaper = screen.blit(game_intro,(0,0))
                                inHouse1()
                                inHouse2()
                                inUphouse()
                                outdoor()
                                screen_luffy = screen.blit(luffy_d3,(xluffy,yluffy))
                                pygame.display.flip()
                                time.sleep(0.075)

                                if event.type == KEYDOWN and event.key == K_DOWN:
                                    yluffy += 5
                                    screen_wallpaper = screen.blit(game_intro,(0,0))
                                    inHouse1()
                                    inHouse2()
                                    inUphouse()
                                    outdoor()
                                    screen_luffy = screen.blit(luffy_d4,(xluffy,yluffy))
                                    pygame.display.flip()
                                    time.sleep(0.075)

                                    if event.type == KEYDOWN and event.key == K_DOWN:
                                        yluffy += 5
                                        screen_wallpaper = screen.blit(game_intro,(0,0))
                                        inHouse1()
                                        inHouse2()
                                        inUphouse()
                                        outdoor()
                                        screen_luffy = screen.blit(luffy_d3,(xluffy,yluffy))
                                        pygame.display.flip()
                                        time.sleep(0.075)

                                        if event.type == KEYDOWN and event.key == K_DOWN:
                                            yluffy += 5
                                            screen_wallpaper = screen.blit(game_intro,(0,0))
                                            inHouse1()
                                            inHouse2()
                                            inUphouse()
                                            outdoor()
                                            screen_luffy = screen.blit(luffy_d,(xluffy,yluffy))
                                            pygame.display.flip()
                                            time.sleep(0.075)

            print(xluffy)
            print(yluffy)
