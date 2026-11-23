import pygame
import window
from Levels import menu
# global variables
brightness = 1.0  # Initial brightness factor
opacity = 50 # inital value
dragging = False
prev_game_state = window.TITLE

# list
adjusted_brightness = [brightness]

def game_brightness():
    brightness_surface = pygame.Surface(window.screen.get_size())
    brightness_surface.fill((255 * adjusted_brightness[0], 255 * adjusted_brightness[0], 255 * adjusted_brightness[0]))
    brightness_surface.set_alpha(opacity)  # Adjust transparency as needed
    window.screen.blit(brightness_surface, (0, 0))

def draw_option():
    pygame.display.set_caption("Options")

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (200, 200, 200)

    # Screen and background
    window.screen.blit(menu.background, (0, 0))

    # Draw text
    menu.get_font("Options", 95, BLACK, 215, 15)
    menu.get_font("Exit", 75, BLACK, 285, 355)
    menu.get_font('Brightness', 55, BLACK, 185, 150)

    # Slider variables
    slider_x = 260  # Starting x-coordinate of the slider bar
    slider_y = 250  # y-coordinate of the slider
    slider_width = 200  # Width of the slider bar
    slider_height = 10  # Height of the slider bar
    handle_width = 20  # Width of the draggable handle
    handle_x = slider_x + slider_width // 2 - handle_width // 2  # Center the handle
    handle_y = slider_y - 5  # Align handle with the slider bar
    brightness = 1.0  # Initial brightness factor

    # Button variables
    exit_button_rect = pygame.Rect(320, 315, 150, 50)

    # Main loop for brightness adjustment
    running = True
    dragging = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Handle button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the "Exit" button was clicked
                if exit_button_rect.collidepoint(event.pos):
                    # Return to menu by calling the menu function
                    window.game_state = prev_game_state
                    return

                # Check if the slider handle was clicked
                if pygame.Rect(handle_x, handle_y, handle_width, slider_height + 10).collidepoint(event.pos):
                    dragging = True

            # Stop dragging
            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False

        # Handle dragging
        if dragging:
            mouse_x, _ = pygame.mouse.get_pos()
            handle_x = max(slider_x, min(mouse_x - handle_width // 2, slider_x + slider_width - handle_width))
            brightness = (handle_x - slider_x) / (slider_width - handle_width)

        # Clear screen and redraw elements
        window.screen.blit(menu.background, (0, 0))
        menu.get_font("Options", 95, BLACK, 215, 15)
        menu.get_font("Exit", 75, BLACK, 287, 315)
        menu.get_font('Brightness', 75, BLACK, 185, 150)

        # Draw slider
        pygame.draw.rect(window.screen, GRAY, (slider_x, slider_y, slider_width, slider_height))
        pygame.draw.rect(window.screen, WHITE, (handle_x, handle_y, handle_width, slider_height + 10))

        # Adjust brightness
        adjusted_surface = pygame.Surface(window.screen.get_size())
        adjusted_surface.fill((brightness * 255, brightness * 255, brightness * 255))
        adjusted_surface.set_alpha(50)  # Adjust this value for intensity
        window.screen.blit(adjusted_surface, (0, 0))

        adjusted_brightness[0] = brightness

        # Update the display
        pygame.display.flip()
