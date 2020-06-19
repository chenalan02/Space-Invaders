import pygame
import map
from bullet import Bullet
from alien import Alien
from spaceship import Spaceship
import os
import random

if __name__=="__main__":

    pygame.init()
    size= (1300, 800)
    pygame.display.set_caption('Inot Invaders')
    screen= pygame.display.set_mode(size)
    clock= pygame.time.Clock()

    #define colors
    white= (255, 255, 255)
    black= (0, 0, 0)
    red= (255, 0, 0)
    green= (0, 255, 0)

    #groups for sprites
    player= Spaceship()
    players_list= pygame.sprite.Group()
    players_list.add(player)
    aliens_list= pygame.sprite.Group()
    player_bullets_list= pygame.sprite.Group()
    alien_bullets_list= pygame.sprite.Group()

    #set variables that determine state of game
    done= False
    lost= False
    restart= False
    difficulty_chosen= False

    while not done:
        #screen to choose difficulty
        if not difficulty_chosen:

            screen.fill(black)
            map.draw_difficulty_options(screen, white, black)

            #detects if a difficulty has been chosen yet and esccapes the loop
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos= pygame.mouse.get_pos()
                    if pos[0] >= 120 and pos[0] <=370:
                        if pos[1] >=330 and pos[1] <= 475:
                            difficulty= "Normal"
                            difficulty_chosen= True

                    if pos[0] >= 525 and pos[0] <=775:
                        if pos[1] >=330 and pos[1] <= 475:
                            difficulty= "Hard"
                            difficulty_chosen= True

                    if pos[0] >= 930 and pos[0] <=1180:
                        if pos[1] >=330 and pos[1] <= 475:
                            difficulty= "Insane"
                            difficulty_chosen= True

            pygame.display.flip()
            clock.tick(300)

        #loop for main game
        elif not lost:

            screen.fill(black)

            for event in pygame.event.get():

                if event.type == pygame.QUIT: 
                    done = True
                #changes direction the player moves
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        player.speed=-2    
                    elif event.key==pygame.K_RIGHT:
                        player.speed=2

                    if event.key == pygame.K_SPACE:
                        bullet= Bullet(0, (player.rect.x, player.rect.y), 6)
                        player_bullets_list.add(bullet)
            
            #randomizes alien spawn with a 1 in 400 chance to spawn
            alien_spawn= random.randint(0, 400)
            #changes speed based on difficulty
            if alien_spawn == 0:
                if difficulty == "Hard":
                    speed_multiplier= 1.5
                if difficulty == "Insane":
                    speed_multiplier= 5
                else:
                    speed_multiplier= 1
                #creates an alien and puts it in a sprite group of aliens
                alien= Alien((random.randint(0, 1140), 0), speed_multiplier)
                aliens_list.add(alien)

            #moves the aliens with a different chance to jump fowards based on difficulty
            for alien in aliens_list:
                if difficulty == "Normal":
                    jump_chance_multiplier= 1
                elif difficulty == "Hard":
                    jump_chance_multiplier= 0.5
                else:
                    jump_chance_multiplier= 0.2

                #deletes the alien if it has reached the player
                if alien.move(jump_chance_multiplier) == False:
                    aliens_list.remove(alien)
                    #tests if the player has lost all health and ends the game
                    if player.dead() == True:
                        lost = True
                else:
                    #randomizes alien firing a bullet and creates a bullet
                    if alien.fire() == True:
                        bullet= Bullet(180, (alien.rect.x, alien.rect.y), 2)
                        alien_bullets_list.add(bullet)
            
            #moves the player
            player.move()

            #tests if each bullet has reached the end of the map and deletes it
            for bullet in player_bullets_list:
                terminal_bullet= bullet.move()
                if terminal_bullet== True:
                    player_bullets_list.remove(bullet)

                #creates a list of aliens that have collided with each bullet and removes the bullet
                aliens_hit_list= pygame.sprite.spritecollide(bullet, aliens_list, False)
                if aliens_hit_list != []:
                    player_bullets_list.remove(bullet)

                    #tests if alien has no health and removes it from group
                    #adds score to player
                    for alien_hit in aliens_hit_list:
                        if alien_hit.dead() == True:
                            aliens_list.remove(alien_hit)
                            player.score+=1

            #tests if each alien bullet has reached the end of the map and deletes it
            for bullet in alien_bullets_list:
                terminal_bullet= bullet.move()
                if terminal_bullet== True:
                    alien_bullets_list.remove(bullet)

                #tests if the player has been hit and removes the bullet 
                players_hit_list= pygame.sprite.spritecollide(bullet, players_list, False)
                if players_hit_list != []:
                    alien_bullets_list.remove(bullet)
                    #tests if the player has 0 health
                    if player.dead() == True:
                            lost= True
        
            #draw all sprites and healthbars
            player_bullets_list.draw(screen)
            players_list.draw(screen)
            alien_bullets_list.draw(screen)
            aliens_list.draw(screen)
            player.healthbar(screen, red, green)
            for alien in aliens_list:
                alien.healthbar(screen, red, green)
            map.draw_score(screen, player.score, white)
            
            pygame.display.flip()

            #sets frames per second
            clock.tick(300)

        else:
            #creates screen if the player has lost with options to restart or quit
            for event in pygame.event.get():

                #if player clicks reset, empty all sprite groups and reset game status variables to default
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos= pygame.mouse.get_pos()
                    if pos[0] >= 200 and pos[0] <=500:
                        if pos[1] >=330 and pos[1] <= 480:

                            lost= False
                            difficulty_chosen= False
                            players_list.empty()
                            aliens_list.empty()
                            player_bullets_list.empty()
                            alien_bullets_list.empty()
                            player= Spaceship()
                            players_list.add(player)
                        
                    #ends game if player clicks quit
                    if pos[0] >= 795 and pos[0] <=1195:
                        if pos[1] >=330 and pos[1] <= 480:
                             done= True

                map.draw_restart_options(screen, white, black)
                pygame.display.flip()
                clock.tick(300)
    #if done is true, quits program
    pygame.quit()