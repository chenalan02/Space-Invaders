import pygame
import os
import math

#class to represent bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, angle, coordinates, speed):
        super().__init__()

        self.image= pygame.image.load(os.path.join('images','Bullet.png'))
        self.image= pygame.transform.scale(self.image,(10, 30))
        self.image= pygame.transform.rotate(self.image, angle)
        self.rect= self.image.get_rect()

        self.speed= speed
        self.rect.x= coordinates[0]
        self.rect.y= coordinates[1]
        self.angle= angle

    #method to move each bullet with a return if the bullet has reached the maps end
    #determines direction of bullet travel based on self.angle
    def move(self):

        if self.angle == 0:
            if self.rect.y <= -100:
                return True
            self.rect.y+=-self.speed

        elif self.angle == 180:
            if self.rect.y >= 900:
                return True
            self.rect.y+=self.speed