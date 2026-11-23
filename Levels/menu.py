import pygame
import os
import window
from Levels import options
# from Levels import Level1

image_path = os.path.join('graphics', 'backgroundtest.png')
background = pygame.image.load(image_path)
font_path = os.path.join('graphics', 'alagard.ttf')

menu_end = pygame.key.get_pressed()

play_rect = pygame.Rect(254, 180, 180, 55)
option_rect = pygame.Rect(242, 255, 242, 55)
shop_rect = pygame.Rect(242, 330, 248, 55)
exit_rect = pygame.Rect(298, 400, 150, 55)

def get_font(text, size, color, x, y):
    font = pygame.font.Font(font_path, size)  
    
    img = font.render(text, True, color)
    # pygame.draw.rect(window.screen, (00, 00, 00), play_rect)
    # pygame.draw.rect(window.screen, (00, 00, 00), option_rect)
    # pygame.draw.rect(window.screen, (00, 00, 00), exit_rect)
    # pygame.draw.rect(window.screen, (00, 00, 00), shop_rect)

    img = window.screen.blit(img, (x, y))
    
    # while hit:
        # pygame.font.Font(None, size + 50)
        # font.render
        # break



def draw_menu():
    pygame.display.set_caption("Menu")
    window.game_state = window.TITLE
    running = True
    while running:
        
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rect.collidepoint(mouse_pos):
                    running = False

                if play_rect.collidepoint(mouse_pos):
                    window.game_state = window.GAME
                    return
                    
                if option_rect.collidepoint(mouse_pos):
                    window.game_state = window.OPTION
                    return
                
                if shop_rect.collidepoint(mouse_pos):
                    window.game_state = window.SHOP
                    return
                    
                if event.type == pygame.K_m:
                    pygame.mixer.music.stop()
            
        
        
        window.screen.blit(background, (0, 0))
        get_font("MAIN MENU", 86, (00, 00, 00), 140, 50) 
        get_font("Play", 68, (00, 00, 00), 309, 180) 
        get_font("Options", 68, (00, 00, 00), 257, 255) 
        get_font("Armory", 68, (00,00,00), 260, 330)
        get_font("Exit", 68, (00, 00, 00), 305, 400)    
        get_font('Click M to mute', 30, (00, 00, 00), 50, 450)   

        # Adding brightness
        brightness_surface = pygame.Surface(window.screen.get_size())
        brightness_surface.fill((255 * options.adjusted_brightness[0], 255 * options.adjusted_brightness[0], 255 * options.adjusted_brightness[0]))
        brightness_surface.set_alpha(options.opacity)  # Adjust transparency as needed
        window.screen.blit(brightness_surface, (0, 0))
       
        pygame.display.update()


    pygame.quit()
    draw_menu()
