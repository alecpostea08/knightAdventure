import pygame
import window
import enemy_data
import PlayerSprites
from Levels import menu

ground_level = 300

level_spawn_x = 350
level_spawn_y = 300

camera_offset_x = 0

random_block_x_pos = 1601
random_block_y_pos = 100

platform_1_x = 3401
platform_1_y = 180

platform_2_x = 3800
platform_2_y = 180

platform_3_x = 5550
platform_3_y = 180

tower_block_1_x = 2901
tower_block_1_y =-300

tower_block_2_x = 3050
tower_block_2_y =80

tower_block_3_x = 4501
tower_block_3_y =-300

tower_block_4_x = 4650
tower_block_4_y = 120

tower_block_5_x = 5000
tower_block_5_y = -1300

tower_block_6_x = 5250
tower_block_6_y = 120

roof_block_x = 4700
roof_block_y = 120

roof_block_x_2 = 5050
roof_block_y_2 = 120

ground = pygame.Rect(0, 400, 6400, 100)
enemies = []


fountain_sprites = pygame.image.load(('graphics/fountain_sprites.png'))

fountain_on = PlayerSprites.get_sprites(fountain_sprites,0,2,37,70)
fountain_on = pygame.transform.scale(fountain_on, (60,135))

fountain_off = PlayerSprites.get_sprites(fountain_sprites,38,2,75,70)
fountain_off = pygame.transform.scale(fountain_on, (60,135))

stone_texture = pygame.image.load("graphics/stone_texture.png")

def draw_level(window):
    global ground_level, level_spawn_x, level_spawn_y, random_block_x_pos, random_block_y_pos, another_random_block_y_pos, another_random_block_x_pos
    global blocks, ground, fountain_block, fountains, fountain_off
    blocks = []
    fountains = []
    blocks.append(ground)

    random_block = pygame.Rect(random_block_x_pos, random_block_y_pos, 200, 300)
    blocks.append(random_block)
    
    fountain_block = pygame.Rect(850, 280, 57,120)
    fountains.append(fountain_block)

    fountain_block_2 = pygame.Rect(4290, 280, 57,120)
    fountains.append(fountain_block_2)

    fountain_block_3 = pygame.Rect(6100, 280, 57,120)
    fountains.append(fountain_block_3)

    platform_1 = pygame.Rect(platform_1_x,platform_1_y, 300, 70)
    blocks.append(platform_1)

    platform_2 = pygame.Rect(platform_2_x,platform_2_y, 300, 70)
    blocks.append(platform_2)

    platform_3 = pygame.Rect(platform_3_x,platform_3_y, 300, 70)
    blocks.append(platform_3)

    tower_block = pygame.Rect(tower_block_1_x,tower_block_1_y, 50, 600)
    blocks.append(tower_block)

    tower_block_2 = pygame.Rect(tower_block_2_x,tower_block_2_y, 50, 320)
    blocks.append(tower_block_2)

    tower_block_3 = pygame.Rect(tower_block_3_x,tower_block_3_y, 50, 600)
    blocks.append(tower_block_3)

    tower_block_4 = pygame.Rect(tower_block_4_x,tower_block_4_y, 50, 280)
    blocks.append(tower_block_4)

    tower_block_5 = pygame.Rect(tower_block_5_x,tower_block_5_y, 50, 1470)
    blocks.append(tower_block_5)

    tower_block_5 = pygame.Rect(tower_block_5_x,tower_block_5_y, 50, 280)
    blocks.append(tower_block_5)

    tower_block_6 = pygame.Rect(tower_block_6_x,tower_block_6_y, 50, 170)
    blocks.append(tower_block_6)

    roof_block = pygame.Rect(roof_block_x,roof_block_y, 200, 50)
    blocks.append(roof_block)

    roof_block_2 = pygame.Rect(roof_block_x_2,roof_block_y_2, 250, 50)
    blocks.append(roof_block_2)

    non_existent_block = pygame.Rect(100000, 10000000, 50, 50)
    blocks.append(non_existent_block)

    
    
    menu.get_font("Press 'a' and 'd' to move left and right",20,(255,255,255),220-camera_offset_x,170)
    menu.get_font("Press space to jump",20,(255,255,255),220-camera_offset_x,190)
    menu.get_font("Press 's' to dash",20,(255,255,255),220-camera_offset_x,210)
    menu.get_font("Press 'z' at a fountain to recover ONLY 1 potion",20,(255,255,255),790-camera_offset_x,170)
    menu.get_font("Press 'h' to heal",20,(255,255,255),790-camera_offset_x,190)
    menu.get_font("this will consume one potion",20,(255,255,255),790-camera_offset_x,210)
    menu.get_font("Press space when touching a",20,(255,255,255),1310-camera_offset_x,170)
    menu.get_font("block mid air to wall jump",20,(255,255,255),1310-camera_offset_x,190)
    menu.get_font("Press F to attack",20,(255,255,255),2001-camera_offset_x,190)
    menu.get_font("SLAY",20,(220,0,0),2001-camera_offset_x,210)
    menu.get_font("your enemies",20,(255,255,255),2051-camera_offset_x,210)
    menu.get_font("The End",50,(255,255,255),6325-camera_offset_x,170)

    for block in blocks:
        adjusted_block = block.move(-camera_offset_x, 0)
        # pygame.draw.rect(window, (0, 200, 0), adjusted_block)
        
        scaled_texture = pygame.transform.scale(stone_texture, (adjusted_block.width, adjusted_block.height))
        window.blit(scaled_texture, adjusted_block)
        
    for fountain in fountains:
        adjusted_fountain = fountain.move(-camera_offset_x, 0)
        # pygame.draw.rect(window, (0, 0, 255), adjusted_fountain)
        window.blit(fountain_on,adjusted_fountain)
        
def spawn_enemies():
    enemies.append(enemy_data.Swordsman(2500, ground_level, (255, 0, 0), "left", camera_offset_x, ground))
    enemies.append(enemy_data.Swordsman(4050, ground_level, (255, 0, 0), "left", camera_offset_x, ground))
    enemies.append(enemy_data.Swordsman(4450, ground_level, (255, 0, 0), "left", camera_offset_x, ground))
    enemies.append(enemy_data.Swordsman(5300, ground_level, (255, 0, 0), "left", camera_offset_x, ground))
    enemies.append(enemy_data.Swordsman(5350, ground_level, (255, 0, 0), "left", camera_offset_x, ground))
    
def enemy_collisions():
    for enemy in enemies:
        for block in blocks:
            if enemy.rect.colliderect(block):

                if enemy.rect.colliderect(block):
                    
                    print("collision")
                    

                        # if enemy.rect.bottom <= block.top + 15 and enemy.rect.top < block.top:
                        #     enemy.rect.y = block.top - enemy.top
                            

                        # elif enemy.rect.right >= block.left and enemy.rect.left < block.left:
                        #     enemy.rect.x = block.left - enemy.rect.width + 1
                        
                        # elif enemy.rect.left <= block.right and enemy.rect.right > block.right:
                        #     enemy.rect.x = block.right - 1

                        # elif enemy.rect.top <= block.bottom and enemy.rect.bottom > block.bottom:
                        #     enemy.rect.y = block.bottom

