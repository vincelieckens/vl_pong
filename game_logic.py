#!/usr/bin/python
#https://www.pygame.org/docs/tut/tom/games6.html#AEN225

import math
import pygame
from pygame.locals import *

GREEN = (0, 51, 0)

    
class Ball():
    def __init__(self, screen):
        self.rect = pygame.Rect((320, 240), (15, 15))
        self.speed = 6
        self.angle = 0.47
        self.area = screen.get_rect()
        self.hit = 0
        
    def update(self, left_bat, right_bat):
        """
        Method that updates the position of the ball.
        It checks if the ball hit the top or bottom of the screen,
        went out of bounds or hit one of the bats
        """
        position = self.calcnewpos(self.rect, self.angle, self.speed)
        self.rect = position
        
        if not self.area.contains(position):
            top_left = not self.area.collidepoint(position.topleft)
            top_right = not self.area.collidepoint(position.topright)
            bottom_left = not self.area.collidepoint(position.bottomleft)
            bottom_right = not self.area.collidepoint(position.bottomright)
            if top_right and top_left or (bottom_right and bottom_left):
                self.angle = -self.angle
            if top_left and bottom_left:
                right_bat.score += 1
                self.rect = self.reset(left_bat)
            if top_right and bottom_right:
                left_bat.score += 1
                self.rect = self.reset(right_bat)
                
        else:
            if self.rect.colliderect(left_bat) == 1 and not self.hit:
                self.angle = math.pi - self.angle
                self.hit = not self.hit
            elif self.rect.colliderect(right_bat) == 1 and not self.hit:
                self.angle = math.pi - self.angle
                self.hit = not self.hit
            elif self.hit:
                self.hit = not self.hit
    
    def calcnewpos(self, rect, angle, speed):
        """
        Realistic physics
        """
        (dx, dy) = (speed * math.cos(angle), speed * math.sin(angle))
        return rect.move(dx, dy)
        
    def reset(self, bat):
        """
        Function that resets the position of the ball
        The ball will move to the position of the bat
        because otherwise it will be impossible
        to return it
        """
        if bat.side == 'right':
            if bat.rect.top > 240 and self.angle < 0:
                self.angle = -self.angle   
            elif bat.rect.top < 240 and self.angle > 0:
                self.angle = -self.angle
        elif bat.side == 'left':
            if bat.rect.top < 240 and self.angle < 0:
                self.angle = -self.angle
            elif bat.rect.top > 240 and self.angle > 0:
                self.angle = -self.angle
        return pygame.Rect((320, 240), (15, 15))   
        
        #Wanneer moet de angle van teken verwisseld worden: indien de richting van de bat en angle omgekeerd is
        
class Bat():
    def __init__(self, screen, side):
        self.rect = pygame.Rect((5, 190), (10, 75))
        self.speed = 6
        self.side = side
        self.state = 'still'
        self.area = screen.get_rect()
        self.score = 0
        self.reinit()
        
    def reinit(self):
        self.state = 'still'
        self.movepos = [0, 0]
        if self.side == 'left':
            self.rect.midleft = self.area.midleft
        elif self.side == 'right':
            self.rect.midright = self.area.midright
    
    def update(self):
        position = self.rect.move(self.movepos)
        if self.area.contains(position):
            self.rect = position
        pygame.event.pump()
        
    def moveup(self):
        self.movepos[1] = self.movepos[1] - (self.speed)
        self.state = 'moveup'
    
    def movedown(self):
        self.movepos[1] = self.movepos[1] + (self.speed)
        self.state = 'movedown'
        
         
 
def main(screen, background, clock, ball, left_bat, right_bat, title_font):
    while True:
        clock.tick(60) #Framerate 60fps
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                if event.key == K_z:
                    left_bat.moveup()
                if event.key == K_s:
                    left_bat.movedown()
                if event.key == K_UP:
                    right_bat.moveup()
                if event.key == K_DOWN:
                    right_bat.movedown()
            elif event.type == KEYUP:
                if event.key == K_z or event.key == K_s:
                    left_bat.movepos = [0, 0]
                    left_bat.state = "still"
                if event.key == K_UP or event.key == K_DOWN:
                    right_bat.movepos = [0, 0]
                    right_bat.state = "still"
        
        screen.blit(background, ball, ball)
        screen.blit(background, left_bat, left_bat)
        screen.blit(background, right_bat, right_bat)
        screen.blit(background, (160, 20))   #Left score position
        screen.blit(background, (421, 20))   #Right score position
        ball.update(left_bat, right_bat)
        left_bat.update()
        right_bat.update()
        
        left_score = title_font.render(str(right_bat.score), False, (0, 51, 0))
        right_score = title_font.render(str(left_bat.score), False, (0, 51, 0)) 
        
        pygame.draw.ellipse(screen, GREEN, ball)
        pygame.draw.rect(screen, GREEN, left_bat)
        pygame.draw.rect(screen, GREEN, right_bat)  
        screen.blit(left_score, (160, 20))
        screen.blit(right_score, (421, 20)) 
        pygame.display.update()
        
         

if __name__ == "__main__":
    main()
        
        
        

        
        
