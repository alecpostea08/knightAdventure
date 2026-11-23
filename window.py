import pygame

screen = pygame.display.set_mode((750, 500)) 
clock = pygame.time.Clock()

SHOP = "Shop"
OPTION = "Options"
TITLE = "Title"
GAME = "Game"
GAME_OVER = "Game Over"
PAUSE = "Pause"

game_state = TITLE


running = True

def start():

    pygame.init()

    background_colour = (100, 0, 255)
    
    # Define the dimensions of 
    # screen object(width,height
    
    # Set the caption of the screen 
    pygame.display.set_caption("Untitled Platformer") 
    
    # Fill the background colour to the screen 
    screen.fill(background_colour)
