import pygame
import window
import player
from Levels import Level1
from Levels import menu
from Levels import shop
from Levels import options
import GUI
import PlayerSprites
import json

running = True
need_enemies = True
esc_let_go = True
mouse_let_go = True

# Load data
with open ("save_data.json", "r") as game_file:
    game_data = json.load(game_file)

window.start()


while running:
    
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            if esc_let_go == False:
                esc_let_go = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_let_go = True

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_ESCAPE]:
            if window.game_state == window.GAME:
                if esc_let_go:
                    window.game_state = window.PAUSE
                    esc_let_go = False
            else:
                if esc_let_go:
                    window.game_state = window.GAME
                    esc_let_go = False

    # pygame.mixer.music.load('musicfile.mp3')
    # pygame.mixer.music.play(-1)
    
    if window.game_state == window.TITLE:
        try:
            menu.draw_menu()
        except:
            # Error occurs whenever close game so when that happens save all the data then close
            game_data = [{"currency": player.currency_count}]

            with open("save_data.json", "w") as game_file:
                json.dump(game_data, game_file)

            running = False
    
    elif window.game_state == window.GAME:
        
        if need_enemies:
            Level1.spawn_enemies()
            need_enemies = False
        
        # Background
        window.screen.fill((100, 0, 255))
        
        # Level
        Level1.draw_level(window.screen)
        
        # Player
        player.collisions()
        player.player_movement()
        player.spawn_player(window.screen)
        player.dash()
        player.knockback()
        player.death()
        player.sword_attack(window.screen)
        # Enemies
        for enemy in Level1.enemies:
            if enemy.health > 0:
                enemy.update(Level1.camera_offset_x, Level1.blocks)
            else:
                Level1.enemies.remove(enemy)
                player.currency_count += 5
         # currency 
        player.display_currency()
        # GUI
        GUI.dash.create_box()
        if player.dash_cooldown > 0:
            GUI.dash.cooldown()
            player.dash_cooldown -= 1
        GUI.dash.draw_icon()
        
        player.display_health()
        player.Potion()
        player.animations()
        
        # Code to handle dashing in loop
        if player.right_dash == True:
            if player.dash_counter < 5:
                player.player_x += 40
                player.dash_counter += 1
            else:
                player.dash_counter = 0
                player.right_dash = False

        if player.left_dash == True:
            if player.dash_counter < 5:
                player.player_x -= 40
                player.dash_counter += 1
            else:
                player.dash_counter = 0
                player.left_dash = False


        # Cooldowns
        # Abilities
        for ability in GUI.abilities:
            if ability.cd == 0:
                ability.cd = ability.cd_max
        # Attack
        if player.sword_cool_down > 0:
            player.sword_cool_down -= 1 
        # brightness
        options.game_brightness()
     
    elif window.game_state == window.OPTION:
        window.screen.fill((00,00,00))
        options.draw_option()      
        
    if window.game_state == window.SHOP:
        window.screen.fill((00,00,00))
        shop.draw_shop() 

    if window.game_state == window.PAUSE:

        window.screen.fill((100, 0, 255))
        # Draw everything but with no movement or updates
        Level1.draw_level(window.screen)
        player.spawn_player(window.screen)
        window.screen.blit(PlayerSprites.current_player_anim,(player.player_x - Level1.camera_offset_x  -11 ,player.player_y-10)) 
        for enemy in Level1.enemies:
            enemy.draw()

        # Draw rect on background
        pause_surface = pygame.Surface(window.screen.get_size())
        pause_surface.fill((0, 0, 0))
        pause_surface.set_alpha(50)
        window.screen.blit(pause_surface, (0, 0))
        
        window.screen.blit(player.Menu_Background,(127,5))
        
        # Draw Title Text
        menu.get_font("PAUSED",70,(255,255,255),242,57)

        # Draw buttons and other text
        
        resume_button = pygame.Rect(272, 150, 187, 55)
        # pygame.draw.rect(window.screen, (0, 0, 0), resume_button)
        menu.get_font("Resume",50,(255,255,255),279,156)

        options_button = pygame.Rect(272, 225, 187, 55)
        # pygame.draw.rect(window.screen, (0, 0, 0), options_button)
        menu.get_font("Options",50,(255,255,255),282,228)

        shop_button = pygame.Rect(272, 300, 187, 55)
        # pygame.draw.rect(window.screen, (0, 0, 0), shop_button)
        menu.get_font("Armory",50,(255,255,255),282,303)

        menu_button = pygame.Rect(294, 380, 137, 55)
        # pygame.draw.rect(window.screen, (0, 0, 0), menu_button)
        menu.get_font("Quit",60,(255,255,255),304,380)

        # Act on buttons
        mouse_pos = pygame.mouse.get_pos()

        if resume_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and mouse_let_go:
                window.game_state = window.GAME
                mouse_let_go = False

        if options_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and mouse_let_go:
                window.game_state = window.OPTION
                options.prev_game_state = window.PAUSE
                mouse_let_go = False
                
        if shop_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and mouse_let_go:
                window.game_state = window.SHOP
                shop.prev_game_state = window.PAUSE
                mouse_let_go = False

        if menu_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and mouse_let_go:
                window.game_state = window.TITLE
                mouse_let_go = False
    
    pygame.display.flip()

    window.clock.tick(60)
