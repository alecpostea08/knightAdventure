import pygame
import os

Enemy_Skin_1 = [
    pygame.image.load(os.path.join('graphics', 'enemy_Walk.png')),
    pygame.image.load(os.path.join('graphics', 'enemy_Idle.png')),
    pygame.image.load(os.path.join('graphics', 'enemy_Attack_3.png')),
    pygame.image.load(os.path.join('graphics', 'enemy_Run.png')),
]

current_skin = Enemy_Skin_1

def get_sprites(sheet, x, y, width, height):
    image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet, (0, 0), (x, y, width, height))
    return image

enemy_walk = get_sprites(Enemy_Skin_1[0], 0, 0, 128, 128)
enemy_walk = pygame.transform.scale(enemy_walk, (179, 208))

enemy_walk2 = get_sprites(Enemy_Skin_1[0], 128, 0, 128, 128)
enemy_walk2 = pygame.transform.scale(enemy_walk2, (179, 208))

enemy_walk3 = get_sprites(Enemy_Skin_1[0], 256, 0, 128, 128)
enemy_walk3 = pygame.transform.scale(enemy_walk3, (179, 208))

enemy_walk4 = get_sprites(Enemy_Skin_1[0], 384, 0, 128, 128)
enemy_walk4 = pygame.transform.scale(enemy_walk4, (179, 208))

enemy_walk5 = get_sprites(Enemy_Skin_1[0], 512, 0, 128, 128)
enemy_walk5 = pygame.transform.scale(enemy_walk5, (179, 208))

enemy_walk6 = get_sprites(Enemy_Skin_1[0], 640, 0, 128, 128)
enemy_walk6 = pygame.transform.scale(enemy_walk6, (179, 208))

enemy_walk7 = get_sprites(Enemy_Skin_1[0], 768, 0, 128, 128)
enemy_walk7 = pygame.transform.scale(enemy_walk7, (179, 208))







enemy_idle = get_sprites(current_skin[1], 0, 0, 128, 128)
enemy_idle = pygame.transform.scale(enemy_idle, (179, 208))
enemy_idle_left = pygame.transform.flip(enemy_idle, True, False)




enemy_attack = get_sprites(current_skin[2], 170, 34, 70, 50)
enemy_attack = pygame.transform.scale(enemy_attack, (150, 135))
enemy_attack_left = pygame.transform.flip(enemy_attack, True, False)

enemy_run_frames = [
    get_sprites(current_skin[3], 42, 40, 29, 42),
    get_sprites(current_skin[3], 72, 40, 29, 42),
    get_sprites(current_skin[3], 102, 40, 29, 42),
    get_sprites(current_skin[3], 132, 40, 29, 42)
]

enemy_run_frames = [pygame.transform.scale(frame, (63, 110)) for frame in enemy_run_frames]


current_enemy_anim = None

def update():
    global enemy_attack, enemy_attack_left, enemy_death, enemy_fall, enemy_fall_left, enemy_idle, enemy_idle_left, enemy_mantle, enemy_mantle_left
    global enemy_run, enemy_slide

    enemy_idle = get_sprites(current_skin[1], 40, 40, 27, 50)
    enemy_idle = pygame.transform.scale(enemy_idle, (70, 130))
    enemy_idle_left = pygame.transform.flip(enemy_idle, True, False)

    enemy_attack = get_sprites(current_skin[2], 170, 34, 70, 50)
    enemy_attack = pygame.transform.scale(enemy_attack, (150, 135))
    enemy_attack_left = pygame.transform.flip(enemy_attack, True, False)

    enemy_run = get_sprites(current_skin[4], 42, 40, 29, 42)
    enemy_run = pygame.transform.scale(enemy_run, (63, 110))
