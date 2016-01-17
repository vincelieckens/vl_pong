#!/usr/bin/env python3


import os 
import pygame
from pygame.locals import *
from game_logic import *
from menus import *
 

#Constants
SCREEN_SIZE = (640, 480)
SCREEN_TITLE = 'Pong'
MENU_FONT = os.path.join('font.ttf')
GREEN = (0, 51, 0)
TOP_TEXT_SIZE = 100
MENU_OPTIONS_SIZE = 50
TOP_TEXT = 'MENU'
MENU_OPTIONS = ('Play', 'Difficulty', 'Players')
DIFF_MENU_OPTIONS = ('Easy', 'Medium', 'Hard')            
DOT_SIZE = (10, 10)
BAT_SIZE = (10, 75)
BALL_SIZE = (15, 15)
LINE_SIZE = (640, 1)
                                           
#Initialize pygame modules, initialize the screen, title 
#and make mouse invisible
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(SCREEN_TITLE)
pygame.mouse.set_visible(0)

#Background resources
background = pygame.Surface(screen.get_size())
background.convert()
background.fill((0, 0, 0))

#Font objects for the text surfaces
top_font = create_font(MENU_FONT, TOP_TEXT_SIZE,)
menu_font = create_font(MENU_FONT, MENU_OPTIONS_SIZE)

#Game variables
running = True
difficulty = ''
angle = 0.47
speed = 5
clock = pygame.time.Clock()
menu_choice = ''
player1_score = 0
player2_score = 0

    
#Menu resources
top_text = create_surface_text(TOP_TEXT, top_font, GREEN)
menu_text = [create_surface_text(word, menu_font, GREEN) for word in MENU_OPTIONS]
diff_menu_text = [create_surface_text(word, menu_font, GREEN) for word in DIFF_MENU_OPTIONS]
choice_dot = create_choice_dot((210, 177), DOT_SIZE)


#Game resources
pong_ball = pygame.Rect(background.get_width() / 2, background.get_height() / 2, 15, 15)
bottom_line = pygame.Rect(0, 0, background.get_width(), 1)
top_line = pygame.Rect(0, 470, background.get_width(), 1)
pong_bat_left = pygame.Rect((5, background.get_height() / 2 - 50), (BAT_SIZE))
pong_bat_right = pygame.Rect((625, background.get_height() / 2 - 50), (BAT_SIZE))


def main(menu_choice, speed, player1_score, player2_score):
    
    while True:
        menu_choice = display_menu(screen, background, choice_dot, top_text, menu_text)
        if menu_choice == 1:
            print(speed)
            screen.blit(background, (0, 0))
            main_loop(screen, background, pong_ball, pong_bat_left, pong_bat_right, top_line, bottom_line, angle, speed, color=GREEN)
        elif menu_choice == 2:
            difficulty = display_menu(screen, background, choice_dot, top_text, diff_menu_text)
            if difficulty == 1:
                speed = 5
            elif difficulty == 2:
                speed = 6
            elif difficulty == 3:
                speed = 7
        elif menu_choice == 3:
            pass
    
        

if __name__ == '__main__':
    main(menu_choice, speed, player1_score, player2_score)
    

    












