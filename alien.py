import pygame
import random
import os

#class to represent aliens
class Alien(pygame.sprite.Sprite):
    def __init__(self, coordinates, speed_multiplier):
        super().__init__()

        self.image= pygame.image.load(os.path.join('images','UFO.png'))
        self.image= pygame.transform.scale(self.image,(60,60))
        self.rect= self.image.get_rect()
        self.rect.x= coordinates[0]
        self.rect.y= coordinates[1]

        self.health= 30
        self.speed= random.choice([-1*speed_multiplier, 1*speed_multiplier])

    #method to move the alien
    def move(self, jump_chance_multiplier):
        #randomizes when the alien will jump fowards to the player
        action= random.randint(0, 900*jump_chance_multiplier)
        if action != 0:
            self.rect.x += self.speed
        else:
            self.rect.y+= 30

        if self.rect.x <= 0:
            self.speed= self.speed*-1
            self.rect.x=0

        elif self.rect.x >=1240:
            self.speed= self.speed*-1
            self.rect.x=1235
        
        #returns False when the alien has reached the end of the map
        if self.rect.y >= 800:
            return False
        
    #method to display healthbar
    def healthbar(self, screen, red, green):
        pygame.draw.rect(screen, red, [self.rect.x, self.rect.y, 60, 7])
        pygame.draw.rect(screen, green, [self.rect.x, self.rect.y, self.health*0.0333333333333*60, 7])

    #method to remove health from the alien and return when it has 0 health
    def dead(self):
        self.health+=-10
        if self.health<=0:
            return True

    #method to randomize when the alien fires bullets
    def fire(self):
        fire_option= random.randint(0, 1000)
        if fire_option ==0:
            return True