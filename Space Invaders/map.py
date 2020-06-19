import pygame
import os
from bullet import Bullet

def draw_difficulty_options(screen, white, black):

    pygame.draw.rect(screen, white, [525,330,250,145])
    pygame.draw.rect(screen, white, [120,330,250,145])
    pygame.draw.rect(screen, white, [930,330,250,145])

    font= pygame.font.SysFont('Calibri', 50, True, False)
    text= font.render("Hard", True, (black))
    screen.blit(text, [595,373])
    
    font= pygame.font.SysFont('Calibri', 50, True, False)
    text= font.render("Normal", True, (black))
    screen.blit(text, [163,373])

    font= pygame.font.SysFont('Calibri', 50, True, False)
    text= font.render("Insane", True, (black))
    screen.blit(text, [985,373])

    font= pygame.font.SysFont('Calibri', 50, True, False)
    text= font.render("Choose a Difficulty", True, (white))
    screen.blit(text, [460,160])

def draw_restart_options(screen, white, black):

    pygame.draw.rect(screen, white, [200,330,300,150])
    pygame.draw.rect(screen, white, [795,330,300,150])

    font= pygame.font.SysFont('Calibri', 50, True, False)
    text= font.render("Restart", True, (black))
    screen.blit(text, [273,380])

    font= pygame.font.SysFont('Calibri', 50, True, False)
    text= font.render("Exit", True, (black))
    screen.blit(text, [900,380])
    
def draw_score(screen, score, white):

    font= pygame.font.SysFont('Calibri', 70, True, False)
    text= font.render(str(score), True, (white))
    if score <= 100:
        screen.blit(text, [1220,0])
    else:
        screen.blit(text, [1190,0])
