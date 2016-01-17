#!/usr/bin/env python3

from copy import deepcopy
import pygame
from pygame.locals import *
import math
from pong import *



def erase_screen(screen, background, pong_ball, pong_bat_left, pong_bat_right):
    """ Erases the previous positions of the game objects """
    screen.blit(background, (pong_ball[0], pong_ball[1]))
    screen.blit(background, (pong_bat_left[0], pong_bat_left[1]))
    screen.blit(background, (pong_bat_right[0], pong_bat_right[1]))
    screen.blit(background, (160, 20))
    screen.blit(background, (480, 20))
    

def move_pong_ball(pong_ball, angle, speed):
    """ 
    Function that moves the ball according to
    realistic physics
    """
    
    (dx, dy) = (speed * math.cos(angle),speed * math.sin(angle))
    pong_ball = pong_ball.move(dx, dy) 
    return pong_ball
    

def draw_game(screen, background, pong_ball, pong_bat_left, pong_bat_right, top_line, bottom_line, player1_score, player2_score, color=GREEN):
    """ 
    Function that draws all the game objects onto the screen
    """
    left_score = create_surface_text(str(player1_score), top_font, pong.GREEN)
    right_score = create_surface_text(str(player2_score), top_font, pong.GREEN)
    pygame.draw.ellipse(screen, color, pong_ball)
    pygame.draw.rect(screen, color, pong_bat_left)
    pygame.draw.rect(screen, color, pong_bat_right)
    pygame.draw.rect(screen, color, top_line)
    pygame.draw.rect(screen, color, bottom_line)
    screen.blit(left_score, (160, 20))
    screen.blit(right_score, (460, 20))
    
    
def event_handler(pong_bat_left, pong_bat_right):
    """
    Handles user input. Returns three values: the exit
    status, the new value of the left pong bat and
    the new value of the right pong bat 
    """
    exit = ''
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit = True
            elif event.key == K_DOWN:
                if pong_bat_right[1] == 400:
                    pong_bat_right = pong_bat_right.move(0, 0)
                else:
                    pong_bat_right = pong_bat_right.move(0, 30)
            elif event.key == K_UP:
                if pong_bat_right[1] == 10:
                    pong_bat_right = pong_bat_right.move(0, 0)
                else:
                    pong_bat_right = pong_bat_right.move(0, -30)
            elif event.key == K_s:
                if pong_bat_left[1] == 400:
                    pong_bat_left = pong_bat_left.move(0, 0)
                else:
                    pong_bat_left = pong_bat_left.move(0, 30)
            elif event.key == K_z:
                if pong_bat_left[1] == 10:
                    pong_bat_left = pong_bat_left.move(0, 0)
                else:
                    pong_bat_left = pong_bat_left.move(0, -30)
    return exit, pong_bat_left, pong_bat_right 
            

def reset_pong_ball(background, pong_ball):
    """ Resets the ball to his starting position """
    return pygame.Rect(background.get_width() / 2, background.get_height() / 2, 15, 15)
    

def out_of_bounds(background, pong_ball):
    """ 
    Function that returns True is the ball
    is out of bounds
    """
   
    if pong_ball.left == 640 or pong_ball.left == 0:
        return True
    
        
def compute_angle(pong_ball, pong_bat_left, pong_bat_right, angle):
    """ Computes the angle for the ball movement """
    if pong_ball.colliderect(pong_bat_left):
        angle = math.pi - angle
    elif pong_ball.colliderect(pong_bat_right):
        angle = math.pi - angle
    elif pong_ball.colliderect(bottom_line):
        angle = -angle
    elif pong_ball.colliderect(top_line):
        angle = -angle
    return angle
 
            
def main_loop(screen, background, pong_ball, pong_bat_left, pong_bat_right, top_line, bottom_line, angle, speed, color=GREEN):

    clock = pygame.time.Clock()
    player1_score = 0
    player2_score = 0
    
    while True:
        
        clock.tick(60)
        
        erase_screen(screen, background, pong_ball, pong_bat_left, pong_bat_right)
    
        exit, pong_bat_left, pong_bat_right = event_handler(pong_bat_left, pong_bat_right)
        
        if exit == True:
            break
    
        angle = compute_angle(pong_ball, pong_bat_left, pong_bat_right, angle)
        
    
        if out_of_bounds(background, pong_ball):
            if pong_ball.left == 640:
                player1_score += 1
            elif pong_ball.left == 0:
                player2_score += 1
            pong_ball = reset_pong_ball(background, pong_ball)
        
        
        pong_ball = move_pong_ball(pong_ball, angle, speed)
        draw_game(screen, background, pong_ball, pong_bat_left, pong_bat_right, top_line, bottom_line, player1_score, player2_score, color=GREEN)
        pygame.display.update()
        
   
    

if __name__ == '__main__':
    main_loop(screen, background, pong_ball, pong_bat_left, pong_bat_right, top_line, bottom_line, angle, player1_score, player2_score, color=GREEN)   
        
        
    
