from pygame import *
import os
import sys
from Colors import *
import pygame

pygame.init()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    print(fullname)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print("Impossible de charger l'image :", name)
        raise SystemExit
    if '.png' in name:
        image = image.convert_alpha()
    else:
        image = image.convert()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key, RLEACCEL)
    return image


def load_sound(name):
    class NoneSound:
        def play(self): pass

    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', name)
    print(fullname)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print('Impossible de charger le son :', name)
        raise SystemExit
    return sound


class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, speed):
        self.move_x = 0
        self.move_y = 0
        self.speed = speed
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_alpha(0)
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.last_pressed = 'NONE'
        self.direction = 'NONE'

        self.counter = 0
        self.move_up = [load_image("pictures/avatar/luffy_u.png"), load_image("pictures/avatar/luffy_u1.png"),
                        load_image("pictures/avatar/luffy_u2.png"), load_image("pictures/avatar/luffy_u3.png"),
                        load_image("pictures/avatar/luffy_u4.png")]
        self.move_down = [load_image("pictures/avatar/luffy_d.png"), load_image("pictures/avatar/luffy_d1.png"),
                          load_image("pictures/avatar/luffy_d2.png"), load_image("pictures/avatar/luffy_d3.png"),
                          load_image("pictures/avatar/luffy_d4.png")]
        self.move_right = [load_image("pictures/avatar/luffy_r.png"), load_image("pictures/avatar/luffy_r1.png"),
                           load_image("pictures/avatar/luffy_r2.png"), load_image("pictures/avatar/luffy_r3.png"),
                           load_image("pictures/avatar/luffy_r4.png")]
        self.move_left = [load_image("pictures/avatar/luffy_l.png"), load_image("pictures/avatar/luffy_l1.png"),
                          load_image("pictures/avatar/luffy_l2.png"), load_image("pictures/avatar/luffy_l3.png"),
                          load_image("pictures/avatar/luffy_l4.png")]

    def move(self, x=False, y=False):
        if x:
            self.rect.x += self.move_x
            self.direction = 'x'
        elif y:
            self.rect.y += self.move_y
            self.direction = 'y'
        else:
            print('Cant move if no x nor y')

    def move_character(self, screen, direction):
        if self.counter + 1 >= 25:
            self.counter = 0
        screen.blit(game.map, (0, 0))
        screen.blit(game.object, game.object_coordonates)
        if game.sword and game.potion and game.shield and game.mc_do and game.map_name is 'outside':
            screen.blit(game.boss_image, (500, 250))
        if direction is 'NONE':
            screen.blit(self.move_up[self.counter // 5], (self.rect.x, self.rect.y))
        if direction is not 'REMAKE':
            self.last_pressed = direction
        if direction is 'UPPER':
            screen.blit(self.move_up[self.counter // 5], (self.rect.x, self.rect.y))
            self.move_y = -self.speed + 2
            self.counter += 1
            self.move(y=True)
        elif direction is 'LOWER':
            screen.blit(self.move_down[self.counter // 5], (self.rect.x, self.rect.y))
            self.move_y = self.speed - 1
            self.counter += 1
            self.move(y=True)
        elif direction is 'RIGHT':
            screen.blit(self.move_right[self.counter // 5], (self.rect.x, self.rect.y))
            self.move_x = self.speed
            self.counter += 1
            self.move(x=True)
        elif direction is 'LEFT':
            screen.blit(self.move_left[self.counter // 5], (self.rect.x, self.rect.y))
            self.move_x = -self.speed
            self.counter += 1
            self.move(x=True)
        elif direction is 'REMAKE':
            if self.last_pressed == 'UPPER':
                screen.blit(self.move_up[0], (self.rect.x, self.rect.y))
                self.move_y = 0
            elif self.last_pressed == 'LOWER':
                screen.blit(self.move_down[0], (self.rect.x, self.rect.y))
                self.move_y = 0
            elif self.last_pressed == 'LEFT':
                screen.blit(self.move_left[0], (self.rect.x, self.rect.y))
                self.move_x = 0
            elif self.last_pressed == 'RIGHT':
                screen.blit(self.move_right[0], (self.rect.x, self.rect.y))
                self.move_x = 0
            else:
                screen.blit(self.move_down[0], (self.rect.x, self.rect.y))
                self.move_x = 0
                self.move_y = 0
        pygame.display.update()


class Wall(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        # self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA, 32)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def collision(self, player):
        if self.rect.colliderect(player.rect):
            if player.move_x > 0 and player.direction is 'x' and player.direction is not 'y':
                # moving right
                player.rect.right = self.rect.left

            elif player.move_x < 0 and player.direction is 'x' and player.direction is not 'y':
                # moving left
                player.rect.left = self.rect.right

            elif player.move_y < 0 and player.direction is 'y' and player.direction is not 'x':
                # moving up
                player.rect.top = self.rect.bottom

            elif player.move_y > 0 and player.direction is 'y' and player.direction is not 'x':
                # moving down
                player.rect.bottom = self.rect.top


class MainMenu:
    def __init__(self, x, y, fps):
        self.screen = pygame.display.set_mode((x, y))
        self.running = True

        self.x = x
        self.y = y

        self.clock = pygame.time.Clock()
        self.fps = fps
        self.fpsFont = pygame.font.SysFont('mono', 22)

        pygame.display.set_icon(load_image("pictures/icon_game.png"))
        pygame.display.set_caption('STEX JOURNEY')

        self.wallpaper = load_image("pictures/wallpaper.png")
        self.blur_wallpaper = load_image("pictures/blur_wallpaper.png")
        self.blur_menu1 = load_image("pictures/blur_menu_out.png")
        self.credits_screen = load_image("pictures/screen_credits.png")
        self.commands_screen = load_image("pictures/screen_commands.png")
        self.fondingame = load_image("pictures/fondingame.png")

        self.game_title = load_image("pictures/home_title.png")
        self.play_1 = load_image("buttons/jouer_1.png")
        self.play_2 = load_image("buttons/jouer_2.png")
        self.settings_1 = load_image("buttons/options_1.png")
        self.settings_2 = load_image("buttons/options_2.png")
        self.commands_1 = load_image("buttons/commandes_1.png")
        self.commands_2 = load_image("buttons/commandes_2.png")
        self.credits_1 = load_image("buttons/credits_1.png")
        self.credits_2 = load_image("buttons/credits_2.png")
        self.back_button = load_image("buttons/retour.png")
        self.son_on = load_image("buttons/son_on.png")
        self.son_off = load_image("buttons/son_off.png")
        self.son = False
        self.son_counter = 0

        self.in_menu = False
        self.sound_menu = False
        self.counter = 0

        self.play_r = self.play_1.get_rect()
        self.play_r.x, self.play_r.y = 0, 240
        self.settings_r = self.settings_1.get_rect()
        self.settings_r.x, self.settings_r.y = 0, 320
        self.commands_r = self.commands_1.get_rect()
        self.commands_r.x, self.commands_r.y = 0, 405
        self.credits_r = self.credits_1.get_rect()
        self.credits_r.x, self.credits_r.y = 0, 490
        self.back_r = self.back_button.get_rect()
        self.back_r.x, self.back_r.y = 925, 25
        self.son_r = self.son_on.get_rect()
        self.son_r.x, self.son_r.y = 325, 200

    def refresh_screen(self, x=False):
        if x:
            self.screen.blit(self.blur_wallpaper, (0, -45))
        else:
            self.screen.blit(self.wallpaper, (0, -45))
        self.screen.blit(self.game_title, (0, 0))

    def loading_menu(self):
        self.refresh_screen()
        self.screen.blit(self.play_1, (0, 240))
        self.screen.blit(self.settings_1, (0, 320))
        self.screen.blit(self.commands_1, (0, 405))
        self.screen.blit(self.credits_1, (0, 490))

    def fade(self, width, height):
        fade = pygame.Surface((width, height))
        for alpha in range(0, 300):
            fade.set_alpha(alpha)
            self.loading_menu()
            self.screen.blit(fade, (0, 0))
            pygame.display.update()

    def sound(self, on=True):
        self.refresh_screen(True)
        self.screen.blit(self.back_button, (925, 25))
        if on:
            self.screen.blit(self.son_on, (325, 200))
            self.son = True
        else:
            self.screen.blit(self.son_off, (325, 200))
            self.son = False
        pygame.display.update()

    def commands(self):
        self.refresh_screen(True)
        self.screen.blit(self.commands_screen, (0, 0))
        self.screen.blit(self.back_button, (925, 25))
        pygame.display.update()

    def credits(self):
        self.refresh_screen(True)
        self.screen.blit(self.credits_screen, (0, 0))
        self.screen.blit(self.back_button, (925, 25))
        pygame.display.update()

    def pair_impair(self, x):
        if x % 2 == 0:
            return True

    def which_one_is_on_hover(self):
        if self.play_r.collidepoint(pygame.mouse.get_pos()) or self.settings_r.collidepoint(
                pygame.mouse.get_pos()) or self.commands_r.collidepoint(
            pygame.mouse.get_pos()) or self.credits_r.collidepoint(pygame.mouse.get_pos()):
            self.refresh_screen()

        if self.play_r.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.play_2, (0, 240))
            self.screen.blit(self.settings_1, (0, 320))
            self.screen.blit(self.commands_1, (0, 405))
            self.screen.blit(self.credits_1, (0, 490))

        elif self.settings_r.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.play_1, (0, 240))
            self.screen.blit(self.settings_2, (0, 320))
            self.screen.blit(self.commands_1, (0, 405))
            self.screen.blit(self.credits_1, (0, 490))

        elif self.commands_r.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.play_1, (0, 240))
            self.screen.blit(self.settings_1, (0, 320))
            self.screen.blit(self.commands_2, (0, 405))
            self.screen.blit(self.credits_1, (0, 490))

        elif self.credits_r.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.play_1, (0, 240))
            self.screen.blit(self.settings_1, (0, 320))
            self.screen.blit(self.commands_1, (0, 405))
            self.screen.blit(self.credits_2, (0, 490))

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            if self.back_r.collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN and self.in_menu:
                self.loading_menu()
                self.in_menu = False
                if self.sound_menu:
                    self.sound_menu = False

            elif self.play_r.collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN and not \
                    self.in_menu:
                self.running = False
                self.fade(1000, 600)
                return

            elif self.settings_r.collidepoint(
                    pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN and not self.in_menu:
                if self.pair_impair(self.counter):
                    self.sound(False)
                if not self.pair_impair(self.counter):
                    self.sound()
                self.in_menu = True
                self.sound_menu = True

            elif self.son_r.collidepoint(pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN and self.sound_menu:
                if self.pair_impair(self.counter):
                    self.sound()
                if not self.pair_impair(self.counter):
                    self.sound(False)
                self.counter += 1

            elif self.commands_r.collidepoint(
                    pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN and not self.in_menu:
                self.commands()
                self.in_menu = True

            elif self.credits_r.collidepoint(
                    pygame.mouse.get_pos()) and event.type == MOUSEBUTTONDOWN and not self.in_menu:
                self.credits()
                self.in_menu = True

        if not self.in_menu:
            self.which_one_is_on_hover()
        pygame.display.update()

    def mainloop(self):
        # Load the menu once so you don't need to hover a button to get the screen refreshed, you'll get a black screen
        self.screen.blit(self.wallpaper, (0, -45))
        self.screen.blit(self.game_title, (0, 0))
        self.screen.blit(self.play_1, (0, 240))
        self.screen.blit(self.settings_1, (0, 320))
        self.screen.blit(self.commands_1, (0, 405))
        self.screen.blit(self.credits_1, (0, 490))
        # Game loop
        # load_sound('sound/music.wav').play()
        while self.running:
            # Event loop
            self.on_event()

            # Draw everything
            pygame.display.update()

            # Limit FPS to 60
            self.clock.tick(self.fps)


class Game:
    def __init__(self, x, y, fps):
        # initialize
        self.screen = pygame.display.set_mode((x, y))
        self.running = True

        self.x = x
        self.y = y

        self.clock = pygame.time.Clock()
        self.fps = fps
        self.fpsFont = pygame.font.SysFont('mono', 22)

        self.player = Player(40, 53, 824, 340, 4.5)
        self.wall = Wall(1000, 120, 0, 0)
        self.wall2 = Wall(255, 240, 0, 0)
        self.wall3 = Wall(55, 600, 0, 0)
        self.wall4 = Wall(1000, 80, 0, 520)
        self.wall5 = Wall(130, 600, 870, 0)
        self.wall6 = Wall(200, 200, 800, 400)
        self.wall7 = Wall(190, 200, 0, 400)
        self.wall8 = Wall(250, 260, 630, 0)
        self.wall9 = Wall(190, 195, 308, 0)
        self.wall10 = Wall(20, 195, 546, 0)
        self.wall_in_first_house = Wall(1000, 185, 0, 0)
        self.wall_in_first_house2 = Wall(1000, 130, 0, 470)
        self.wall_in_first_house3 = Wall(290, 600, 0, 0)
        self.wall_in_first_house4 = Wall(250, 600, 750, 0)
        self.wall_in_up_house = Wall(1000, 230, 0, 0)
        self.wall_in_up_house2 = Wall(250, 600, 0, 0)
        self.wall_in_up_house3 = Wall(1000, 100, 0, 500)
        self.wall_in_up_house4 = Wall(250, 600, 750, 0)
        self.wall_in_second_house = Wall(250, 600, 750, 0)
        self.wall_in_second_house2 = Wall(250, 600, 0, 0)
        self.wall_in_second_house3 = Wall(1000, 130, 0, 470)
        self.wall_in_second_house4 = Wall(1000, 185, 0, 0)

        self.boss_image = load_image("pictures/boss.png")
        self.boss = False
        self.map = load_image("maps/game_intro.png")
        self.map_name = 'outside'
        self.object = load_image("items/sword.png")
        self.object_coordonates = (254, 128)
        self.amount_of_key_pressed = 0
        self.sword = False
        self.mc_do = False
        self.potion = False
        self.shield = False
        self.just_joined_the_game = False

    def play_intro(self):
        self.screen.blit(self.map, (0, 0))
        self.screen.blit(self.object, (254, 128))
        pygame.mouse.set_visible(False)
        pygame.key.set_repeat(True)
        pygame.display.update()

    def change_map(self, map, x, y):
        # map to load the right map in the images, x and y to put the character on the right side of the map
        if map is 'outside':
            self.map = load_image("maps/game_intro.png")
            self.map_name = map
            if not self.sword:
                self.object = load_image("items/sword.png")
                self.object_coordonates = (254, 128)
            self.player.rect.x = x
            self.player.rect.y = y
        if map is 'first_house':
            self.map = load_image("maps/first_house.png")
            self.map_name = map
            if not self.potion:
                self.object = load_image("items/potion.png")
                self.object_coordonates = (542, 163)
            self.player.rect.x = x
            self.player.rect.y = y
        if map is 'up_house':
            self.map = load_image("maps/up_house.png")
            self.map_name = map
            if not self.shield:
                self.object = load_image("items/shield.png")
                self.object_coordonates = (400, 207)
            self.player.rect.x = x
            self.player.rect.y = y
        if map is 'second_house':
            self.map = load_image("maps/second_house.png")
            self.map_name = map
            if not self.mc_do:
                self.object = load_image("items/mcdo.png")
                self.object_coordonates = (371, 140)
            self.player.rect.x = x
            self.player.rect.y = y

    def take_object(self):
        if 255 <= self.player.rect.x <= 268 and self.player.rect.y == 120 and not self.sword:
            self.object = load_image("pictures/nothing.png")
            self.sword = True
        elif 532 <= self.player.rect.x <= 552 and self.player.rect.y == 185 and not self.potion:
            self.object = load_image("pictures/nothing.png")
            self.potion = True
        elif 390 <= self.player.rect.x <= 410 and self.player.rect.y == 230 and not self.shield:
            self.object = load_image("pictures/nothing.png")
            self.shield = True
        elif 359 <= self.player.rect.x <= 382 and self.player.rect.y == 185 and not self.mc_do:
            self.object = load_image("pictures/nothing.png")
            self.mc_do = True

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            # Get keydown and adjust player speed, also check for collisions with houses
            keys = pygame.key.get_pressed()
            if keys[K_RIGHT]:
                if 210 <= self.player.rect.y <= 231 and 607 <= self.player.rect.x <= 614:
                    self.change_map('outside', 500, 180)
                self.player.move_character(self.screen, 'RIGHT')
            elif keys[K_LEFT]:
                self.player.move_character(self.screen, 'LEFT')
            elif keys[K_UP]:
                if 357 <= self.player.rect.x <= 377 and self.player.rect.y == 195 and self.map_name is not 'first_house':
                    self.change_map('first_house', 545, 405)
                if 498 <= self.player.rect.x <= 506 and self.player.rect.y == 120 and self.map_name is not 'up_house':
                    self.change_map('up_house', 614, 222)
                if 684 <= self.player.rect.x <= 711 and self.player.rect.y == 260 and self.map_name is not 'second_house':
                    self.change_map('second_house', 425, 413)
                self.player.move_character(self.screen, 'UPPER')
            elif keys[K_DOWN]:
                if 520 <= self.player.rect.x <= 566 and self.player.rect.y == 414:
                    self.change_map('outside', 367, 195)
                if 405 <= self.player.rect.x <= 456 and self.player.rect.y == 413:
                    self.change_map('outside', 700, 260)
                self.player.move_character(self.screen, 'LOWER')
            if not keys[K_RIGHT] and not keys[K_LEFT] and not keys[K_DOWN] and not keys[K_UP]:
                self.player.move_character(self.screen, 'REMAKE')
            pygame.display.update()

    def mainloop(self):
        self.play_intro()
        while self.running:
            # Event loop
            self.on_event()

            # Game Logic
            self.take_object()
            if self.map_name is 'outside':
                self.wall.collision(self.player)
                self.wall2.collision(self.player)
                self.wall3.collision(self.player)
                self.wall4.collision(self.player)
                self.wall5.collision(self.player)
                self.wall6.collision(self.player)
                self.wall7.collision(self.player)
                self.wall8.collision(self.player)
                self.wall9.collision(self.player)
                self.wall10.collision(self.player)
            if self.map_name is 'first_house':
                self.wall_in_first_house.collision(self.player)
                self.wall_in_first_house2.collision(self.player)
                self.wall_in_first_house3.collision(self.player)
                self.wall_in_first_house4.collision(self.player)
            if self.map_name is 'up_house':
                self.wall_in_up_house.collision(self.player)
                self.wall_in_up_house2.collision(self.player)
                self.wall_in_up_house3.collision(self.player)
                self.wall_in_up_house4.collision(self.player)
            if self.map_name is 'second_house':
                self.wall_in_second_house.collision(self.player)
                self.wall_in_second_house2.collision(self.player)
                self.wall_in_second_house3.collision(self.player)
                self.wall_in_second_house4.collision(self.player)

            # Draw everything
            pygame.display.flip()

            # Limit FPS to 60
            self.clock.tick(self.fps)


if __name__ == "__main__":
    menu = MainMenu(1000, 600, 60)
    menu.mainloop()
    game = Game(1000, 600, 60)
    game.mainloop()