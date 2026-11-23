import pygame 
import os 

Skin_1 = [
          pygame.image.load(os.path.join('graphics','_Fall.png')), 
          pygame.image.load(os.path.join('graphics','_Idle.png')),
          pygame.image.load(os.path.join('graphics','_Attack.png')),
          pygame.image.load(os.path.join('graphics','_Death.png')),
          pygame.image.load(os.path.join('graphics','_Run.png')),
          pygame.image.load(os.path.join('graphics','_SlideAll.png')),
          pygame.image.load(os.path.join('graphics','_WallHang.png')),
          ]

Skin_2 = [
          pygame.image.load(os.path.join('graphics','Skin2_Fall.png')), 
          pygame.image.load(os.path.join('graphics','Skin2_Idle.png')),
          pygame.image.load(os.path.join('graphics','Skin2_Attack.png')),
          pygame.image.load(os.path.join('graphics','Skin2_Death.png')),
          pygame.image.load(os.path.join('graphics','Skin2_Run.png')),
          pygame.image.load(os.path.join('graphics','Skin2_SlideAll.png')),
          pygame.image.load(os.path.join('graphics','Skin2_WallHang.png')),
          ]

Skin_3 = [
          pygame.image.load(os.path.join('graphics','Skin3_Fall.png')), 
          pygame.image.load(os.path.join('graphics','Skin3_Idle.png')),
          pygame.image.load(os.path.join('graphics','Skin3_Attack.png')),
          pygame.image.load(os.path.join('graphics','Skin3_Death.png')),
          pygame.image.load(os.path.join('graphics','Skin3_Run.png')),
          pygame.image.load(os.path.join('graphics','Skin3_SlideAll.png')),
          pygame.image.load(os.path.join('graphics','Skin3_WallHang.png')),
          ]

current_skin = Skin_1

def get_sprites(sheet, x, y, width, height):
    image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet, (0, 0), (x, y, width, height))

    return image
Skin_Display_1 = get_sprites(Skin_1[1],40,40,27,50)
Skin_Display_1 = pygame.transform.scale(Skin_Display_1, (70,130))

Skin_Display_2 = get_sprites(Skin_2[1],40,40,27,50)
Skin_Display_2 = pygame.transform.scale(Skin_Display_2, (70,130))

Skin_Display_3 = get_sprites(Skin_3[1],40,40,27,50)
Skin_Display_3 = pygame.transform.scale(Skin_Display_3, (70,130))

player_fall = get_sprites(current_skin[0],40,40,29,42)
player_fall = pygame.transform.scale(player_fall, (70,115))
player_fall_left = pygame.transform.flip(player_fall,True,False)

player_idle = get_sprites(current_skin[1],40,40,27,50)
player_idle = pygame.transform.scale(player_idle, (70,130))
player_idle_left = pygame.transform.flip(player_idle,True,False)

player_attack = get_sprites(current_skin[2],170,34,70,50)
player_attack = pygame.transform.scale(player_attack, (150,135))
player_attack_left = pygame.transform.flip(player_attack,True,False)

player_death = get_sprites(current_skin[3],1087,30,60,80)
player_death = pygame.transform.scale(player_death, (120,195))

player_run = get_sprites(current_skin[4],42,40,29,42)
player_run = pygame.transform.scale(player_run, (63,110))

player_run1 = get_sprites(current_skin[4], 162, 40, 29, 42) 
player_run1 = pygame.transform.scale(player_run1, (60,110))

player_run2 = get_sprites(current_skin[4], 282, 40, 29, 42)  
player_run2 = pygame.transform.scale(player_run2, (67,107))

player_run3 = get_sprites(current_skin[4], 402, 40, 29, 42)  
player_run3 = pygame.transform.scale(player_run3, (65,112))

player_run4 = get_sprites(current_skin[4], 522, 40, 29, 42)  
player_run4 = pygame.transform.scale(player_run4, (58,110))

player_run5 = get_sprites(current_skin[4], 640, 40, 29, 42)  
player_run5 = pygame.transform.scale(player_run5, (60,110))

player_run6 = get_sprites(current_skin[4], 761, 40, 29, 42) 
player_run6 = pygame.transform.scale(player_run6, (61,110))

player_run7 = get_sprites(current_skin[4], 882, 40, 24, 42)  
player_run7 = pygame.transform.scale(player_run7, (63,107))

player_run8 = get_sprites(current_skin[4], 1003, 40, 24, 42)  
player_run8 = pygame.transform.scale(player_run8, (58,112))

player_run9 = get_sprites(current_skin[4], 1120, 40, 29, 42) 
player_run9 = pygame.transform.scale(player_run9, (59,110))

player_slide = get_sprites(current_skin[5],45,30,40,70)
player_slide = pygame.transform.scale(player_slide, (120,135))

player_slide2 = get_sprites(current_skin[5],164,30,40,80)
player_slide2 = pygame.transform.scale(player_slide2, (120,195))
player_slide2_left = pygame.transform.flip(player_slide2,True,False)

player_slide3 = get_sprites(current_skin[5],406,30,28,60)
player_slide3 = pygame.transform.scale(player_slide3, (60,145))

player_mantle = get_sprites(current_skin[6],45,40,26,40)
player_mantle = pygame.transform.scale(player_mantle, (70,115))
player_mantle_left = pygame.transform.flip(player_mantle,True,False)

current_player_anim = None

def update():
    global player_attack, player_attack_left, player_death, player_fall, player_fall_left, player_idle, player_idle_left, player_mantle, player_mantle_left
    global player_run, player_run1,player_run2,player_run3,player_run4,player_run5,player_run6,player_run7,player_run8,player_run9, player_slide2,player_slide2_left

    player_fall = get_sprites(current_skin[0],40,40,29,42)
    player_fall = pygame.transform.scale(player_fall, (70,115))
    player_fall_left = pygame.transform.flip(player_fall,True,False)

    player_idle = get_sprites(current_skin[1],40,40,27,50)
    player_idle = pygame.transform.scale(player_idle, (70,130))

    player_idle_left = pygame.transform.flip(player_idle,True,False)

    player_attack = get_sprites(current_skin[2],170,34,70,50)
    player_attack = pygame.transform.scale(player_attack, (150,135))

    player_attack_left = pygame.transform.flip(player_attack,True,False)

    player_death = get_sprites(current_skin[3],1087,30,60,80)
    player_death = pygame.transform.scale(player_death, (120,195))

    player_run = get_sprites(current_skin[4],42,40,29,42)
    player_run = pygame.transform.scale(player_run, (63,110))

    player_run1 = get_sprites(current_skin[4], 162, 40, 29, 42) 
    player_run1 = pygame.transform.scale(player_run1, (60,110))

    player_run2 = get_sprites(current_skin[4], 282, 40, 29, 42)  
    player_run2 = pygame.transform.scale(player_run2, (67,107))

    player_run3 = get_sprites(current_skin[4], 402, 40, 29, 42)  
    player_run3 = pygame.transform.scale(player_run3, (65,112))

    player_run4 = get_sprites(current_skin[4], 522, 40, 29, 42)  
    player_run4 = pygame.transform.scale(player_run4, (58,110))

    player_run5 = get_sprites(current_skin[4], 640, 40, 29, 42)  
    player_run5 = pygame.transform.scale(player_run5, (60,110))

    player_run6 = get_sprites(current_skin[4], 761, 40, 29, 42) 
    player_run6 = pygame.transform.scale(player_run6, (61,110))

    player_run7 = get_sprites(current_skin[4], 882, 40, 24, 42)  
    player_run7 = pygame.transform.scale(player_run7, (63,107))

    player_run8 = get_sprites(current_skin[4], 1003, 40, 24, 42)  
    player_run8 = pygame.transform.scale(player_run8, (58,112))

    player_run9 = get_sprites(current_skin[4], 1120, 40, 29, 42) 
    player_run9 = pygame.transform.scale(player_run9, (59,110))

    player_slide2 = get_sprites(current_skin[5],164,30,40,80)
    player_slide2 = pygame.transform.scale(player_slide2, (120,195))
    player_slide2_left = pygame.transform.flip(player_slide2,True,False)

    player_mantle = get_sprites(current_skin[6],45,40,26,40)
    player_mantle = pygame.transform.scale(player_mantle, (70,115))
    player_mantle_left = pygame.transform.flip(player_mantle,True,False)



