import pygame
import window
from Levels import Level1
from Levels import menu
import os
from time import time
import PlayerSprites
import json


player_x = 500
player_y = 300
player_x_vel = 5
player_height = 100
player_width = 50
keys_pressed = pygame.key.get_pressed()
gravity = True

idle = True
moving_left = False
moving_right = False

singular_hit = False

direction = "right"

player_top = player_y
player_bottom = player_y + player_height
player_left = player_x
player_right = player_x + player_width

right_dash = False
left_dash = False
dash_counter = 0
dash_cooldown = 0

left_knockback = False
right_knockback = False
knockback_counter = 5

player_health = 6
death_timer = None
dying = None

running_anim_counter = 0

PlayerSprites.current_player_anim = PlayerSprites.player_idle

def animations():
    global running_anim_counter, player_health, dying, death_timer
    
    if moving_right:
        
        if running_anim_counter <= 5:
            PlayerSprites.current_player_anim = PlayerSprites.player_run
        elif running_anim_counter <= 10:
            PlayerSprites.current_player_anim = PlayerSprites.player_run1
        elif running_anim_counter <= 15:
            PlayerSprites.current_player_anim = PlayerSprites.player_run2
        elif running_anim_counter <= 20:
            PlayerSprites.current_player_anim = PlayerSprites.player_run3
        elif running_anim_counter <= 25:
            PlayerSprites.current_player_anim = PlayerSprites.player_run4
        else:
            running_anim_counter = 0

    if moving_left:
        if running_anim_counter <= 5:
            PlayerSprites.current_player_anim = pygame.transform.flip(PlayerSprites.player_run, True, False)
        elif running_anim_counter <= 10:
            PlayerSprites.current_player_anim = pygame.transform.flip(PlayerSprites.player_run1, True, False)
        elif running_anim_counter <= 15:
            PlayerSprites.current_player_anim = pygame.transform.flip(PlayerSprites.player_run2, True, False)
        elif running_anim_counter <= 20:
            PlayerSprites.current_player_anim = pygame.transform.flip(PlayerSprites.player_run3, True, False)
        elif running_anim_counter <= 25:
            PlayerSprites.current_player_anim = pygame.transform.flip(PlayerSprites.player_run4, True, False)
        else:
            running_anim_counter = 0
            
    if direction == "right" and not moving_right:
        PlayerSprites.current_player_anim = PlayerSprites.player_idle
        
    elif direction == "left" and not moving_left:
        PlayerSprites.current_player_anim = PlayerSprites.player_idle_left

    if direction == "right" and attack_active == True:
        PlayerSprites.current_player_anim = PlayerSprites.player_attack
        
    if direction == "left" and attack_active == True:
        PlayerSprites.current_player_anim = PlayerSprites.player_attack_left

    if direction == "right" and attack_active == True and not moving_right:
        PlayerSprites.current_player_anim = PlayerSprites.player_attack
        
    if direction == "left" and attack_active == True and not moving_right:
        PlayerSprites.current_player_anim = PlayerSprites.player_attack_left

    if Jumping == True and direction == "right":
        PlayerSprites.current_player_anim = PlayerSprites.player_fall
        
    if Jumping == True and direction == "left":
        PlayerSprites.current_player_anim = PlayerSprites.player_fall_left

    if r_collide == True and Jumping == True:
        PlayerSprites.current_player_anim = PlayerSprites.player_mantle

    if l_collide == True and player_y < 300:
        PlayerSprites.current_player_anim = PlayerSprites.player_mantle_left

    if right_dash == True and player_y < 300: 
        PlayerSprites.current_player_anim = PlayerSprites.player_slide2

    if left_dash == True:
        PlayerSprites.current_player_anim = PlayerSprites.player_slide2_left

    if player_health <= 0:
        # Initialize or decrement the death timer
        dying == True
        if death_timer is None:
            death_timer = 60  
        
        if death_timer > 0:
            PlayerSprites.current_player_anim = PlayerSprites.player_death
            death_timer -= 1

        else:
            # Reset state after death animation ends
            death_timer = None
            dying = False
            PlayerSprites.current_player_anim = PlayerSprites.player_idle
        
    running_anim_counter += 1

    if attack_active == False and death_timer == None:
        window.screen.blit(PlayerSprites.current_player_anim,(player_x - Level1.camera_offset_x  -11 ,player_y-10))    
    
    if PlayerSprites.current_player_anim == PlayerSprites.player_attack:
        window.screen.blit(PlayerSprites.current_player_anim,(player_x - Level1.camera_offset_x  -11 ,player_y-30)) 

    if PlayerSprites.current_player_anim == PlayerSprites.player_attack_left:
        window.screen.blit(PlayerSprites.current_player_anim,(player_x - Level1.camera_offset_x  -90 ,player_y-30))
    
    if PlayerSprites.current_player_anim == PlayerSprites.player_death:
        window.screen.blit(PlayerSprites.current_player_anim,(player_x - Level1.camera_offset_x - 30,player_y-30))

Menu_Background = pygame.transform.scale(
    pygame.image.load(os.path.join('graphics', 'Pause_Menu.png')).convert_alpha(),(480, 490))

six_heart_sprite_sheet = pygame.transform.scale(
    pygame.image.load(os.path.join('graphics', '6heartte.png')).convert_alpha(),(350, 90))

five_heart_sprite_sheet = pygame.transform.scale(
    pygame.image.load(os.path.join('graphics', '5heartte.png')).convert_alpha(),(350, 90))

four_heart_sprite_sheet = pygame.transform.scale(
    pygame.image.load(os.path.join('graphics', '4heartte.png')).convert_alpha(),(350, 90))

three_heart_sprite_sheet = pygame.transform.scale(
    pygame.image.load(os.path.join('graphics', '3heartte.png')).convert_alpha(),(350, 90))

two_heart_sprite_sheet = pygame.transform.scale(
    pygame.image.load(os.path.join('graphics', '2heartte.png')).convert_alpha(),(350, 90))

one_heart_sprite_sheet = pygame.transform.scale(
    pygame.image.load(os.path.join('graphics', '1heartte.png')).convert_alpha(),(350, 90))

#potions:

all_empty_bottles = pygame.transform.scale(
    pygame.image.load(os.path.join('graphics', '4EmptyBottle.png')).convert_alpha(),(220, 50))

three_empty_bottles = pygame.transform.scale(
    pygame.image.load(os.path.join('graphics', '3EmptyBottle.png')).convert_alpha(),(220, 50))

two_empty_bottles = pygame.transform.scale(
    pygame.image.load(os.path.join('graphics', '2EmptyBottle.png')).convert_alpha(),(220, 50))

one_empty_bottles = pygame.transform.scale(
    pygame.image.load(os.path.join('graphics', '1EmptyBottle.png')).convert_alpha(),(220, 50))

all_full_bottles = pygame.transform.scale(
    pygame.image.load(os.path.join('graphics', 'AllBottlesFull.png')).convert_alpha(),(220, 50))

#currency:

currency_sprite = pygame.transform.scale(
    pygame.image.load(os.path.join('graphics', 'skull with white bachground.png')).convert_alpha(),(60, 50))


Jumping = False
can_jump = False
Y_Gravity = 15
Jump_height = 50

player_color = (255, 0, 0)

attack_rect = None  
attack_active = False 
attack_start_time = 0  
attack_duration = 0.5
sword_cool_down = 0.2 * 60 
# currency
with open('save_data.json', 'r') as file:
    currency_dict = json.load(file)
    
currency_count = currency_dict[0]["currency"]

heal_count = 1
potion_count = 2
fountains_used = []

attack_direction =  pygame.Rect(player_x +player_width - Level1.camera_offset_x , player_y ,60,player_height)

pygame.init()

def display_health():
    if player_health == 6:
        window.screen.blit(six_heart_sprite_sheet, (0, -10))
        # pygame.display.update()
        six_heart_sprite_sheet.set_colorkey((166, 166, 166))

    if player_health == 5:
        window.screen.blit(five_heart_sprite_sheet, (0, -10))
        # pygame.display.update()
        five_heart_sprite_sheet.set_colorkey((166, 166, 166))
    
    if player_health == 4:
        window.screen.blit(four_heart_sprite_sheet, (0, -10))
        # pygame.display.update()
        four_heart_sprite_sheet.set_colorkey((166, 166, 166))

    if player_health == 3:
        window.screen.blit(three_heart_sprite_sheet, (0, -10))
        # pygame.display.update()
        three_heart_sprite_sheet.set_colorkey((166, 166, 166))

    if player_health == 2:
        window.screen.blit(two_heart_sprite_sheet, (0, -10))
        # pygame.display.update()
        two_heart_sprite_sheet.set_colorkey((166, 166, 166))

    if player_health == 1:
        window.screen.blit(one_heart_sprite_sheet, (0, -10))
        # pygame.display.update()
        one_heart_sprite_sheet.set_colorkey((166, 166, 166))

def Potion():
    global keys_pressed, potion_count, player_health, heal_count, fountains_used

    if potion_count == 0:
        window.screen.blit(all_empty_bottles, (-7, 65))
        # pygame.display.update()
        all_empty_bottles.set_colorkey((166, 166, 166))

    if potion_count == 1:
        window.screen.blit(three_empty_bottles, (-7, 65))
        # pygame.display.update()
        three_empty_bottles.set_colorkey((166, 166, 166))

    if potion_count == 2:
        window.screen.blit(two_empty_bottles, (-7, 65))
        # pygame.display.update()
        two_empty_bottles.set_colorkey((166, 166, 166))

    if potion_count == 3:
        window.screen.blit(one_empty_bottles, (-7, 65))
        # pygame.display.update()
        one_empty_bottles.set_colorkey((166, 166, 166))

    if potion_count == 4:
        window.screen.blit(all_full_bottles, (-7, 65))
        # pygame.display.update()
        all_full_bottles.set_colorkey((166, 166, 166))

    if keys_pressed[pygame.K_h] and potion_count > 0 and player_health < 6 and heal_count == 1:
        potion_count -=1
        player_health +=1
        heal_count +=1
    
    if not keys_pressed[pygame.K_h]:
        heal_count = 1





def spawn_player(window):
    global player_x, player_y, player_color, player
    player = pygame.Rect(player_x - Level1.camera_offset_x, player_y, player_width, player_height)
    # pygame.draw.rect(window, player_color, player)

def respawn_player():
    global player_x, player_y
    player_x = 500
    player_y = 300

def player_movement():
    global player_x, player_y, Jumping, Jump_height, Y_Gravity, running, can_jump, player_x_vel, left_collision, i_frame, move_lock, l_collide, keys_pressed, edge
    global right_dash, left_dash, last_d_press_time, dash_interval, player_top, player_bottom, player_left, player_right, moving_right, moving_left, r_collide, direction

    keys_pressed = pygame.key.get_pressed()
    keys_released = pygame.KEYUP
    edge = False
    
    if player_x < 100:
        edge = True
        player_x = 100  
    elif player_x > 6311:
        edge = True
        player_x = 6310  

    if keys_pressed[pygame.K_d] and not edge:
        player_x += player_x_vel
        direction = "right"
        moving_right = True
        moving_left = False
    else:
        moving_right = False

    if keys_pressed[pygame.K_a] and not edge:
        player_x -= player_x_vel
        direction = "left"
        moving_right = False
        moving_left = True
    else:
        moving_left = False

    if keys_pressed[pygame.K_LSHIFT]:
        player_x_vel = 9
    else:
        player_x_vel = 5
    
    if keys_pressed[pygame.K_SPACE] and can_jump == True:
        Jumping = True
        can_jump = False

    if Jumping == True:
        player_y -= Jump_height
        for i in range (Jump_height):
            Jump_height -= 3
            break

        if Jump_height < 0:
            Jumping = False
            Jump_height = 50
        
        if r_collide == True:
            can_jump = True

        if l_collide == True:
            can_jump = True
        
    Level1.camera_offset_x = player_x - 750 // 2
    
    if gravity:
        player_y += Y_Gravity

    player_top = player_y
    player_bottom = player_y + player_height
    player_left = player_x
    player_right = player_x + player_width

def dash():
    global right_dash, left_dash, dash_counter, player_x, player_x_vel, dash_cooldown, last_d_press_time, last_a_press_time, right_dash_interval, left_dash_interval, move_lock, direction, keys_pressed
    
    if dash_cooldown == 0:

        if keys_pressed[pygame.K_s] and direction == "right":
            direction = "right"
            right_dash = True
            dash_counter = 0
            dash_cooldown = 60

        if keys_pressed[pygame.K_s]:
            direction = "left"
            left_dash = True
            dash_counter = 0
            dash_cooldown = 60

def collisions():
    global player_x, player_y, player_color, jumping, can_jump, top_collision, left_wall_jump, left_collision, Y_Gravity, collision, r_collide, l_collide
    global potion_count, keys_pressed

    r_collide = False
    l_collide = False
    
    player = pygame.Rect(player_x, player_y, 50, 100)
    for block in Level1.blocks:

            if player.colliderect(block):
                
    
                    collision = True

                    if player_bottom <= block.top + 15 and player_top < block.top:
                        player_y = block.top - player_height
                        top_collision = True
                        Jumping = False
                        can_jump = True
                        Jump_height = 50
                        Y_Gravity = 0

                    elif player_right >= block.left and player_left < block.left:
                        player_x = block.left - player_width + 1
                        r_collide = True
                    
                    elif player_left <= block.right and player_right > block.right:
                        player_x = block.right - 1
                        l_collide = True

                    elif player_top <= block.bottom and player_bottom > block.bottom:
                        player_y = block.bottom
                        Y_Gravity = 15

            else:
                top_collision = False
                Y_Gravity = 15
                collision = False
                
    for fountain in Level1.fountains:
        if player.colliderect(fountain):
            if keys_pressed[pygame.K_z] and potion_count < 5 and fountain not in fountains_used:
                potion_count+=1
                fountains_used.append(fountain)
                
def death():
    global player_x, player_y, player_health, potion_count, dying
    
    if player_x + 100 < Level1.ground.left or player_x - 100 > Level1.ground.right:
        respawn_player()

    if player_health <= 0 and dying == False:
        player_health = 6
        potion_count = 0
        dying = None
        respawn_player()
        for enemy in Level1.enemies:
            enemy.x = 400
            enemy.y = 300
            enemy.speed = 4
            enemy.aware = False
            enemy.direction = "right"
            enemy.timer = 10 * 60
            enemy.walking_area = pygame.Rect(enemy.x - 300, enemy.y, 400, 100)
            enemy.rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)


def sword_attack(window):

    global attack_rect, attack_active, attack_start_time,direction,sword_cool_down, attack_duration,cool_down_over
    global attack_down_time, attack_count,attack_direction, singular_hit
    keys_pressed = pygame.key.get_pressed()
    cool_down_over = True

    if not keys_pressed[pygame.K_f]:
        attack_count = 1

    # Activate the attack when the "Q" key is pressed
    if keys_pressed[pygame.K_f] and not attack_active and attack_count == 1:
        # attack_rect = (player_x + player_width // 2, player_y + player_height // 2)  # Centered around the player
        attack_active = True
        attack_start_time = time()

    # Draw the sword attck if it is active
    if attack_active:
        if attack_active and sword_cool_down == 0 and cool_down_over == True:
            sword_cool_down = 0.2 * 60 
            if direction == "right":
                attack_direction =  pygame.Rect(player_x +player_width - Level1.camera_offset_x , player_y ,60,player_height)
            else: 
                attack_direction = pygame.Rect(player_x - 60 - Level1.camera_offset_x , player_y,60,player_height)
                
        attack_count +=1
        # pygame.draw.rect(window,(0,0,0) , attack_direction)

        # Deactivate after the duration
        if time() - attack_start_time >= attack_duration:
            cool_down_over = False
            attack_active = False
            attack_down_time = time()
            singular_hit = False
            if attack_down_time == 1*60:
                cool_down_over = True
                
def knockback():
    global player_x, player_y, player_x_vel, player_y_vel, player_height, player_width, player, direction, keys_pressed, knockback_counter, right_knockback, left_knockback, gravity
    
    if right_knockback or left_knockback:
        gravity = False

        if knockback_counter > 0:
            knockback_counter -= 1
            
            if right_knockback:
                player_x += 10
                player_y -= 10
            else:
                player_x -= 10
                player_y -= 10
        else:
            right_knockback = False
            left_knockback = False
            gravity = True
            knockback_counter = 5
        
#------------------------------

font = pygame.font.Font(None, 36)  # Default font, size 36

def display_currency():
    # pass
    """
    Displays the current currency count on the screen.
    """
    global currency_count
    menu.get_font(F"{currency_count}", 35,(255,255,255), 680,17)
    window.screen.blit(currency_sprite, (620, 8)) 

    currency_sprite.set_colorkey((255,255,255))
