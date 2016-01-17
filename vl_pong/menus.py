#!/usr/bin/env python3


import os
import pygame
from pygame.locals import *
import pong


def create_font(font, size):
    """
    Function that returns a pygame font object,
    with the font type and size as arguments
    """
    return pygame.font.Font(os.path.join(font), size)
    
def create_choice_dot(coordinates, size):
    """
    Creates a choice dot based on a (x, y) coordinates
    argument and a (x, x) size argument
    """
    return pygame.Rect(coordinates, size)
    

def create_surface_text(text, font_object, color):
    """
    Creates a text surface based on a given
    text, font_object and color, which is green
    by default
    """
    return font_object.render(text, False, color)
    

def menu_events(choice_dot):
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
            elif event.key == K_DOWN:
                if choice_dot.top == 327:
                    choice_dot.move_ip(0, -150)
                else:
                    choice_dot.move_ip(0, 75)
            elif event.key == K_UP:
                if choice_dot.top == 177:
                    choice_dot.move_ip(0, 150)
                else:
                    choice_dot.move_ip(0, -75)
            elif event.key == K_RETURN:
                if choice_dot.top == 177:
                    return 1
                elif choice_dot.top == 252:
                    return 2
                elif choice_dot.top == 327:
                    return 3
                
    
             

def draw_menu(screen, background, choice_dot, top_text, menu_text, color):
    """ 
    Draws all the menu resources to the screen
    """
    text_y_pos = 150
    computation = (background.get_width() / 2) - (top_text.get_width() / 2)
    screen.blit(top_text, (computation, 15))
    for text in menu_text:
        screen.blit(text, (240, text_y_pos))
        text_y_pos += 75
    pygame.draw.rect(screen, color, choice_dot) 
    
def display_menu(screen, background, choice_dot, top_text, menu_text):
    """ 
    Function that shows the menu on the screen.
    It returns the choice made by the user
    """
    while True:
        screen.blit(background, (0, 0))
        draw_menu(screen, background, choice_dot, top_text, menu_text, pong.GREEN)
        choice = menu_events(choice_dot)
        if choice:
            break
        pygame.display.update()
    return choice
    

        




