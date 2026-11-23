import pygame
import player
import window

bottom = 425

abilities = []

class Ability():
    def __init__(self, slot, cooldown, icon):
        self.box_width = 50
        self.box_height = 50
        self.box_x = 750 - (75 * slot)
        self.box_y = bottom
        self.rect = pygame.Rect(self.box_x, self.box_y, self.box_width, self.box_height)
        self.cd = cooldown
        self.cd_max = cooldown
        self.icon = icon

    def create_box(self):
        pygame.draw.rect(player.window.screen, (78, 84, 80), self.rect)
        pygame.draw.line(player.window.screen, (68, 74, 70), (self.box_x + 1, self.box_y), (self.box_x + self.box_width - 2, self.box_y), 7) # Top Line
        pygame.draw.line(player.window.screen, (68, 74, 70), (self.box_x + 1, self.box_y), (self.box_x + 1, self.box_y + self.box_height - 2), 7) # Left Line
        pygame.draw.line(player.window.screen, (68, 74, 70), (self.box_x + self.box_width - 2, self.box_y), (self.box_x + self.box_width - 2, self.box_y + self.box_height - 2), 7) # Right Line
        pygame.draw.line(player.window.screen, (68, 74, 70), (self.box_x + 1, self.box_y + self.box_height - 2), (self.box_x + self.box_width - 2, self.box_y + self.box_height - 2), 7) # Bottom Line
        
    def draw_icon(self):
        player.window.screen.blit(self.icon, (self.box_x + 5, self.box_y + 5))
        
    def cooldown(self):
        if self.cd > 0:
            height = (self.box_height - 10) * (self.cd / self.cd_max)
            pygame.draw.rect(player.window.screen, (98, 104, 100), (self.box_x + 5, self.box_y + 4 + (self.box_height - 10 - height), self.box_width - 10, height))
            self.cd -= 1
        
dash_icon = pygame.image.load("graphics/icons/dash_icon.png")
dash_icon = pygame.transform.scale(dash_icon, (40, 40))
dash = Ability(1, 1 * 60, dash_icon)
abilities.append(dash)
