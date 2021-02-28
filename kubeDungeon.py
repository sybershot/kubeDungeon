import random
from datetime import datetime, timedelta

import os
import time
import pygame
from pygame.rect import Rect

import config as c
from button import Button
from game import Game
from player import Player
from text_object import TextObject
import colors

class kubeDungeon(Game):
    def __init__(self):
        Game.__init__(self, 'kubeDungeon', c.screen_width, c.screen_height, c.background_image, c.frame_rate)
        #self.sound_effects = {name: pygame.mixer.Sound(sound) for name, sound in c.sounds_effects.items()}
        self.reset_effect = None
        self.score = 0
        self.lives = c.initial_lives
        self.start_level = False
        self.player = None
        self.menu_buttons = []
        self.is_game_running = False
        self.tick = 0
        self.create_objects()

    def create_menu(self):
        def on_play(button):
            for b in self.menu_buttons:
                self.objects.remove(b)

            self.is_game_running = True
            self.start_level = True

        def on_quit(button):
            self.game_over = True
            self.is_game_running = False

        for i, (text, click_handler) in enumerate((('PLAY', on_play), ('QUIT', on_quit))):
            b = Button(c.menu_offset_x,
                       c.menu_offset_y + (c.menu_button_h + 5) * i,
                       c.menu_button_w,
                       c.menu_button_h,
                       text,
                       click_handler,
                       padding=5)
            self.objects.append(b)
            self.menu_buttons.append(b)
            self.mouse_handlers.append(b.handle_mouse_event)

    def create_objects(self):
        self.create_player()
        self.create_labels()
        self.create_menu()

    def create_labels(self):
        self.score_label = TextObject(c.score_offset,
                                      c.status_offset_y,
                                      lambda: f'SCORE: {self.score}',
                                      c.text_color,
                                      c.font_name,
                                      c.font_size)
        self.objects.append(self.score_label)
        self.lives_label = TextObject(c.lives_offset,
                                      c.status_offset_y,
                                      lambda: f'LIVES: {self.lives}',
                                      c.text_color,
                                      c.font_name,
                                      c.font_size)
        self.objects.append(self.lives_label)

    def create_player(self):
        player = Player((c.screen_width - c.paddle_width) // 2,
                        c.screen_height - c.paddle_height * 2,
                        10,
                        10,
                        c.paddle_color,
                        c.paddle_speed)
        #add controls
        self.keydown_handlers[pygame.K_LEFT].append(player.handle)
        self.keydown_handlers[pygame.K_RIGHT].append(player.handle)
        self.keydown_handlers[pygame.K_UP].append(player.handle)
        self.keydown_handlers[pygame.K_DOWN].append(player.handle)
        self.keyup_handlers[pygame.K_LEFT].append(player.handle)
        self.keyup_handlers[pygame.K_RIGHT].append(player.handle)
        self.keyup_handlers[pygame.K_UP].append(player.handle)
        self.keyup_handlers[pygame.K_DOWN].append(player.handle)
        self.player = player
        self.objects.append(self.player)


    def update(self):
        if not self.is_game_running:
            return

        if self.start_level:
            self.start_level = False
            self.show_message('GET READY!', centralized=True)

        # if not self.bricks:
        #     self.show_message('YOU WIN!!!', centralized=True)
        #     self.is_game_running = False
        #     self.game_over = True
        #     return
        super().update()
            
        if self.game_over:
            self.show_message('GAME OVER!', centralized=True)

    def show_message(self, text, color=colors.WHITE, font_name='Arial', font_size=20, centralized=False):
        message = TextObject(c.screen_width // 2, c.screen_height // 2, lambda: text, color, font_name, font_size)
        self.draw()
        message.draw(self.surface, centralized)
        pygame.display.update()
        time.sleep(c.message_duration)


def main():
    kubeDungeon().run()


if __name__ == '__main__':
    main()
