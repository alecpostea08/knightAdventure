import pygame
import window
from Levels import menu
from Levels import options
import PlayerSprites
import os
import player


prev_game_state = window.TITLE

exit_rect2 = pygame.Rect(34, 375, 105, 50)

Skin_2_Unlock = False
Skin_3_Unlock = False


Shop_Background = pygame.transform.scale(
    pygame.image.load(os.path.join('graphics', 'Shop_Menu.png')).convert_alpha(),(575, 480))

def draw_shop():
    global Skin_1_Rect, Skin_2_Rect, Skin_3_Rect

    Skin_1_Rect = pygame.Rect(234, 136, 97, 104)
    Skin_2_Rect = pygame.Rect(406, 136, 97, 104)
    Skin_3_Rect = pygame.Rect(585, 136, 97, 104)
    
    pygame.display.set_caption("Armory")

    window.screen.blit(menu.background, (0, 0))
    window.screen.blit(Shop_Background,(170,5))
    # pygame.draw.rect(window.screen,(0,0,0),exit_rect2)
    pygame.draw.rect(window.screen,(0,0,0),Skin_1_Rect)
    pygame.draw.rect(window.screen,(0,0,0),Skin_2_Rect)
    pygame.draw.rect(window.screen,(0,0,0),Skin_3_Rect)
    
    menu.get_font("Armory", 90, (00, 00, 00), 307, 30) 
    menu.get_font("Exit",53,(0,0,0),34,378)
    window.screen.blit(PlayerSprites.Skin_Display_1,(240,133))
    window.screen.blit(PlayerSprites.Skin_Display_2,(415,133))
    window.screen.blit(PlayerSprites.Skin_Display_3,(596,133))

    if PlayerSprites.current_skin == PlayerSprites.Skin_1:
            menu.get_font("Selected", 30, (00, 00, 00), 226,254) 

    if PlayerSprites.current_skin == PlayerSprites.Skin_2:
            menu.get_font("Selected", 30, (00, 00, 00), 398,254) 

    if PlayerSprites.current_skin == PlayerSprites.Skin_3:
            menu.get_font("Selected", 30, (00, 00, 00), 578,254) 

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rect2.collidepoint(event.pos):
                    window.game_state = prev_game_state
                    return

                if Skin_1_Rect.collidepoint(event.pos):
                     PlayerSprites.current_skin = PlayerSprites.Skin_1
                     player.skin_1_active = True
                     PlayerSprites.update()
                
                if Skin_2_Rect.collidepoint(event.pos) and Skin_2_Unlock == False and player.currency_count >= 25:
                     player.currency_count -= 25
                     PlayerSprites.current_skin = PlayerSprites.Skin_2
                     player.skin_2_active = True
                     PlayerSprites.update()
                
                if Skin_2_Rect.collidepoint(event.pos) and Skin_2_Unlock == True:
                     PlayerSprites.current_skin = PlayerSprites.Skin_2
                     player.skin_2_active = True
                     PlayerSprites.update()

                if Skin_3_Rect.collidepoint(event.pos) and Skin_3_Unlock == False and player.currency_count >= 50:
                     player.currency_count -= 50
                     PlayerSprites.current_skin = PlayerSprites.Skin_3
                     player.skin_1_active = True
                     PlayerSprites.update()

                if Skin_3_Rect.collidepoint(event.pos) and Skin_3_Unlock == True:
                    PlayerSprites.current_skin = PlayerSprites.Skin_3
                    PlayerSprites.update()



    brightness_surface = pygame.Surface(window.screen.get_size())
    brightness_surface.fill((255 * options.adjusted_brightness[0], 255 * options.adjusted_brightness[0], 255 * options.adjusted_brightness[0]))
    brightness_surface.set_alpha(options.opacity)  # Adjust transparency as needed
    window.screen.blit(brightness_surface, (0, 0))
