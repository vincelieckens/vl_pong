#!/usr/bin/env python3


import os
import pygame
from pygame.locals import *
         

class Menu():
    def __init__(self, screen, title, text, options):
        self.screen = screen
        self.title = title
        self.text = text
        self.options = options   
        self.choice_dot = pygame.Rect((210, 177), (10, 10))
                
    def draw(self):
        position = 150
        self.screen.blit(self.title, (220, 15))
        for text in self.text:
            self.screen.blit(text, (240, position))
            position += 75
        pygame.draw.rect(self.screen, (0, 51, 0), self.choice_dot) 
        
    def move_dot_up(self):
        if self.options == 3:
            if self.choice_dot.top == 177:
                return self.choice_dot.move_ip(0, 150)
            else:
                return self.choice_dot.move_ip(0, -75)
        elif self.options == 2:
            if self.choice_dot.top == 177:
                return self.choice_dot.move_ip(0, 75)
            else:
                return self.choice_dot.move_ip(0, -75)
    
    def move_dot_down(self):
        if self.options == 3:
            if self.choice_dot.top == 327:
                return self.choice_dot.move_ip(0, -150)
            else:
                return self.choice_dot.move_ip(0, 75)
        elif self.options == 2:
            if self.choice_dot.top == 252:
                return self.choice_dot.move_ip(0, -75)
            else:
                return self.choice_dot.move_ip(0, 75)



def main(screen, background, menu):
    
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return 'quit'
                elif event.key == K_DOWN:
                    menu.move_dot_down()
                elif event.key == K_UP:
                    menu.move_dot_up()
                elif event.key == K_RETURN:
                    if menu.choice_dot.top == 177:
                        return 1
                    elif menu.choice_dot.top == 252:
                        return 2
                    elif menu.choice_dot.top == 327:
                        return 3
                    
        screen.blit(background, (0, 0))
        menu.draw()
        pygame.display.update()
             


if __name__ == "__main__":
    choice = main(player_menu)


        




