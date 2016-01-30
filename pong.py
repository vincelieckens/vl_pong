#!/usr/bin/env python3


import os 
import pygame
from pygame.locals import *
import game_logic
import menus
 
                                           
#Initialize pygame modules, initialize the screen, title 
#and make mouse invisible
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pong')
pygame.mouse.set_visible(0)

#Background resources
background = pygame.Surface(screen.get_size())
background.convert()
background.fill((0, 0, 0))

#Font objects
title_font = pygame.font.Font(os.path.join('font.ttf'), 100)
menu_font = pygame.font.Font(os.path.join('font.ttf'), 50)

#Surfaces
top_text = title_font.render('Menu', False, (0, 51, 0))
menu_text = [menu_font.render(text, False, (0, 51, 0)) for text in ('Play', 'Difficulty', 'Players')]
diff_menu_text = [menu_font.render(text, False, (0, 51, 0)) for text in ('Easy', 'Medium', 'Hard')]
player_menu_text = [menu_font.render(text, False, (0, 51, 0)) for text in ('One player', 'Two players')]


#Menu objects
main_menu = menus.Menu(screen, top_text, menu_text, 3)
difficulty_menu = menus.Menu(screen, top_text, diff_menu_text, 3)
player_menu = menus.Menu(screen, top_text, player_menu_text, 2)

#Game objects
global left_bat
global right_bat
left_bat = game_logic.Bat(screen, 'left')
right_bat = game_logic.Bat(screen, 'right')
ball = game_logic.Ball(screen)
clock = pygame.time.Clock()

#Draw background
screen.blit(background, (0, 0))
pygame.display.update()
    
    
def main():
    while True:
        menu_choice = menus.main(screen, background, main_menu)
        if menu_choice == 1:
            screen.blit(background, (0, 0))
            game_logic.main(screen, background, clock, ball, left_bat, right_bat, title_font)
        elif menu_choice == 2:
            difficulty = menus.main(screen, background, difficulty_menu)
            if difficulty == 1:
                ball.speed = 5
            elif difficulty == 2:
                ball.speed = 6
            elif difficulty == 3:
                ball.speed = 7
        elif menu_choice == 3:
            pass
        elif menu_choice == 'quit':
            break
            


if __name__ == '__main__':
    main()
    

    












