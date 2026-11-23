import pygame
import window
import player
import EnemySprites

class Swordsman():
    def __init__(self, x, y, color, direction, camera_offset_x, block):
        self.x = x
        self.starting_x = x
        self.y = y
        self.width = 50
        self.height = 100
        self.prev_x = self.x

        self.moving = False
        
        self.player_seen_pos_x = 0
        
        self.block = block
        self.color = color
        self.health = 3
        self.speed = 2
        
        self.immunity = 0

        self.camera_offset_x = camera_offset_x
        

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        if direction == "left":
            self.vision = pygame.Rect(self.x - 450, self.y, 450, 100)
        else:
            self.vision = pygame.Rect(self.x, self.y, 450, 100)
        
        self.aware_area = pygame.Rect(self.x - 100, self.y, 250, 100)
        self.walking_area_start = self.block.x + self.starting_x
        

        self.direction = direction
        self.aware = False

        self.attacking = False
        self.damage = 1
        self.attack_cd = 1 * 30
        self.attack_timer = 0

        self.timer = 5 * 60
        
        self.walk_anim_counter = 0

        self.current_sprite = None

    def animations(self):
        if self.direction == "left" and not self.moving:
            self.current_sprite = EnemySprites.enemy_idle_left
        elif self.direction == "right" and not self.moving:
            self.current_sprite = EnemySprites.enemy_idle

        if self.direction == "right" and self.moving:
            if self.walk_anim_counter < 5:
                self.current_sprite = EnemySprites.enemy_walk
            elif self.walk_anim_counter < 10:
                self.current_sprite = EnemySprites.enemy_walk2
            elif self.walk_anim_counter < 15:
                self.current_sprite = EnemySprites.enemy_walk3
            elif self.walk_anim_counter < 20:
                self.current_sprite = EnemySprites.enemy_walk4
            elif self.walk_anim_counter < 25:
                self.current_sprite = EnemySprites.enemy_walk5
            elif self.walk_anim_counter < 30:
                self.current_sprite = EnemySprites.enemy_walk6
            elif self.walk_anim_counter < 35:
                self.current_sprite = EnemySprites.enemy_walk7
            else:
                self.walk_anim_counter = 0

        if self.direction == "left" and self.moving:
            self.current_sprite = EnemySprites.enemy_walk
            if self.walk_anim_counter < 5:
                self.current_sprite = pygame.transform.flip(EnemySprites.enemy_walk, True, False)
            elif self.walk_anim_counter < 10:
                self.current_sprite = pygame.transform.flip(EnemySprites.enemy_walk2, True, False)
            elif self.walk_anim_counter < 15:
                self.current_sprite = pygame.transform.flip(EnemySprites.enemy_walk3, True, False)
            elif self.walk_anim_counter < 20:
                self.current_sprite = pygame.transform.flip(EnemySprites.enemy_walk4, True, False)
            elif self.walk_anim_counter < 25:
                self.current_sprite = pygame.transform.flip(EnemySprites.enemy_walk5, True, False)
            elif self.walk_anim_counter < 30:
                self.current_sprite = pygame.transform.flip(EnemySprites.enemy_walk6, True, False)
            elif self.walk_anim_counter < 35:
                self.current_sprite = pygame.transform.flip(EnemySprites.enemy_walk7, True, False)
            else:
                self.walk_anim_counter = 0

        self.walk_anim_counter += 1


    def draw(self):
        # Use these to debug enemy
        
        # pygame.draw.rect(window.screen, (0, 0, 255), self.vision)
        # pygame.draw.rect(window.screen, (255, 255, 0), self.aware_area)
        # pygame.draw.rect(window.screen, (100, 100, 255), self.range)
        # pygame.draw.rect(window.screen, (155, 22, 63), self.walking_area)
        
        # This just draws enemy
        # pygame.draw.rect(window.screen, self.color, self.rect)
        window.screen.blit(self.current_sprite, (self.x - self.camera_offset_x - 64, self.y - 100))
        
    def vision_func(self):
        
        if self.direction == "left":
            self.vision = pygame.Rect(self.x - 450, self.y, 450, 100)
        else:
            self.vision = pygame.Rect(self.x, self.y, 450, 100)
            

        self.vision = self.vision.move(-self.camera_offset_x, 0)
            
        # Check if enemy sees player
        if self.vision.colliderect(player.player):
            if self.direction == "left":
                self.speed = -4
                self.aware = True
                self.player_seen_pos_x = player.player.x - self.camera_offset_x
            else:
                self.speed = 4
                self.aware = True
                self.player_seen_pos_x = player.player.x - self.camera_offset_x
                
        elif self.aware_area.colliderect(player.player):
            self.aware = True
            if self.direction == "left":
                self.direction = "right"
            else:
                self.direction = "left"
                
        else:
            self.timer -= 1
            
        if self.timer == 0:
            self.aware = False
            self.timer = 10 * 60
            self.walking_area_start = self.x - 200

        if self.direction == "right":
            self.range = self.rect.move(25, 0)
        else:
            self.range = self.rect.move(-25, 0)
        
    def move(self):
        
        # Checks if player is in range of enemy to be attacked
        
        if self.range.colliderect(player.player) and self.aware:
            self.speed = 0
            self.attacking = True
            
        else:
            
            # If enemy is aware of player, move towards
        
            if self.aware:
                
                if self.vision.colliderect(player.player):
                
                    if player.player.x > (self.x - self.camera_offset_x) + 75 or player.player.x < (self.x - self.camera_offset_x) - 75:

                        if player.player.x < self.x - self.camera_offset_x:
                            self.speed = -6
                        else:
                            self.speed = 6                    
                        
                else:
                    if self.direction == "left" and self.x - self.camera_offset_x > self.player_seen_pos_x:
                        self.speed = -6
                    elif self.direction == "right" and self.x - self.camera_offset_x < self.player_seen_pos_x:
                        self.speed = 6
                    else:
                        self.speed = 0
                
                        
                        
                self.x += self.speed


            else:
                
                if self.direction == "left":
                    self.speed = -2
                else:
                    self.speed = 2
                    
                # Make sure enemy stays in walking area
                                        
                if self.rect.colliderect(self.walking_area):
                    self.x += self.speed
                else:
                    self.speed *= -1
                    self.x += self.speed
                    
                # Make sure enemy doesn't go off block
                    
                if (self.x - self.camera_offset_x) + 50 >= (self.block.x + self.block.width) - self.camera_offset_x or (self.x - self.camera_offset_x) <= self.block.x - self.camera_offset_x:
                    self.speed *= -1

        # Confirm direction of enemy
        if -abs(self.speed) == self.speed and self.speed != 0:
            self.direction = "left"
        elif abs(self.speed) == self.speed and self.speed != 0:
            self.direction = "right"
                

    def attack(self):
        if self.attack_timer > 0:
            self.attack_timer -= 0.5

        if self.attacking:
            if self.attack_timer == 0:
                # Do attack code here
                # Double check if player is in range
                if self.range.colliderect(player.player):
                    player.player_health -= self.damage
                    if self.direction == "left":
                        player.left_knockback = True
                    else:
                        player.right_knockback = True

                self.attack_timer = self.attack_cd

    def death(self):
        if self.rect.colliderect(player.attack_direction) and player.singular_hit == False and self.immunity == 0:
            self.health -= 1
            player.singular_hit = True
            self.immunity = 1 * 60
            
    
            
                
    def update(self, camera_offset_x, blocks):

        self.camera_offset_x = camera_offset_x
        
        self.walking_area = pygame.Rect(self.walking_area_start, self.y, 400, 100)
        self.walking_area = self.walking_area.move(-self.camera_offset_x, 0)
        
        
        self.aware_area = pygame.Rect(self.x - 100, self.y, 250, 100)
        self.aware_area = self.aware_area.move(-self.camera_offset_x, 0)

        
        self.vision_func()
        self.move()
        self.attack()
        self.death()
        
        if self.prev_x != self.x:
            self.moving = True
        else:
            self.moving = False

        if self.immunity > 0:
            self.immunity -= 1
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect = self.rect.move(-self.camera_offset_x, 0)
        
        

                # else:
                #     top_collision = False
                #     Y_Gravity = 15
                #     collision = False

        self.animations()
        self.draw()
        self.prev_x = self.x
