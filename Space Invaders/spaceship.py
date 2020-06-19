import pygame
import os
from bullet import Bullet

#class to represent the player
class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.health= 100
        self.speed= 0
        self.score= 0
        self.image= pygame.image.load(os.path.join('images','Spaceship.png'))
        self.image= pygame.transform.scale(self.image,(60, 80))

        self.rect= self.image.get_rect()
        self.rect.x= 600
        self.rect.y= 720

    #method to display the healthbar based on self.health
    def healthbar(self, screen, red, green):
        pygame.draw.rect(screen, red, [self.rect.x, self.rect.y, 60, 7])
        pygame.draw.rect(screen, green, [self.rect.x, self.rect.y, self.health*0.01*60, 7])

    #method to move the player
    #changes x coordinate of player based on their speed
    #if the player reaches the border, change their speed to 0
    def move(self):
        self.rect.x+=self.speed
        if self.rect.x <= 0:
            self.speed=0
            self.rect.x=0
        elif self.rect.x >=1235:
            self.speed=0
            self.rect.x=1235

    #method to remove health and returns if the player had died
    def dead(self):
        self.health+=-10
        if self.health<=0:
            return True

