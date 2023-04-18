import pygame
from sys import exit 
import math
from settings import *

pygame.init()

#creating window
screen = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption("TDS")
clock = pygame.time.Clock()

#load image
background = pygame.transform.scale(pygame.image.load("Assesment-3-Research-Repo/Side Projects/TDS/background/background.png").convert(),  (WIDTH,HIGHT))

class Player(pygame.sprite.Sprite):
    #player icon
    def __init__(self):
        super().__init__()
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        self.image = pygame.transform.rotozoom(pygame.image.load("Assesment-3-Research-Repo/Side Projects/TDS/player/0.png").convert_alpha(), 0, PLAYER_SIZE)
        self.base_player_image = self.image
        #checking for collision 
        self.hitbox_rect = self.base_player_image.get_rect(center = self.pos)
        #drawing the player
        self.rect = self.hitbox_rect.copy()
        self.speed = PLAYER_SPEED
        self.shoot = False
        #this allows the user to only shoot when cooldown is at 0
        self.shoot_cooldown = 0
        self.gun_barrel_offset = pygame.math.Vector2(GUN_OFFSET_X, GUN_OFFSET_Y)

    #player rotation
    def player_rotation(self):
        self.mouse_coords = pygame.mouse.get_pos()
        self.x_change_mouse_player = (self.mouse_coords[0] - self.hitbox_rect.centerx) 
        self.y_change_mouse_player = (self.mouse_coords[1] - self.hitbox_rect.centery)
        self.angle = math.degrees(math.atan2(self.y_change_mouse_player,self.x_change_mouse_player))
        self.image = pygame.transform.rotate(self.base_player_image, -self.angle)
        self.rect = self.image.get_rect(center = self.hitbox_rect.center)


    #player movement inputs
    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.velocity_y = -self.speed
        if keys[pygame.K_s]:
            self.velocity_y = self.speed
        if keys[pygame.K_d]:
            self.velocity_x = self.speed
        if keys[pygame.K_a]:
            self.velocity_x = -self.speed

        #moving diagonaily
        if self.velocity_x != 0 and self.velocity_y != 0:
            self.velocity_x /= math.sqrt(2)
            self.velocity_y /= math.sqrt(2)

        #shooting keys
        if pygame.mouse.get_pressed() == (1,0,0) or keys[pygame.K_SPACE]:
            self.shoot = True
            self.is_shooting()
        else:
            self.shoot = False

    def is_shooting(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = SHOOT_COOLDOWN
            # Rotate the gun barrel offset vector by the player's angle
            rotated_gun_barrel_offset = self.gun_barrel_offset.rotate(self.angle)
            # Add the rotated gun barrel offset vector to the player's position vector to get the final position of the gun barrel
            spawn_bullet_pos = self.pos + rotated_gun_barrel_offset
            # Create the bullet at the final position of the gun barrel
            self.bullet = Bullet(spawn_bullet_pos[0], spawn_bullet_pos[1], self.angle)
            
            all_sprites_group.add(self.bullet)
            bullet_group.add(self.bullet)


    def move(self):
        self.pos += pygame.math.Vector2(self.velocity_x,self.velocity_y)
        self.hitbox_rect.center = self.pos
        self.rect.center = self.hitbox_rect.center

    def update(self):
        self.user_input()
        self.move()
        self.player_rotation()

        #if cooldown is not yet 0 it will -1 from the cooldown time
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

class Bullet(pygame.sprite.Sprite):
    #x and y is the possision of the bullet that we want to spawn it at. Angle is for the direction the player is shooting
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.image.load("Assesment-3-Research-Repo/Side Projects/TDS/bullet/1.png").convert_alpha()
        #this is for the bullet size for how big it will be in game
        self.image = pygame.transform.rotozoom(self.image, 0, BULLET_SCALE)
        #creates rectangle around our image(bullet)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = BULLET_SPEED
        self.x_vel = math.cos(self.angle * (2*math.pi/360)) * self.speed
        self.y_vel = math.sin(self.angle * (2*math.pi/360)) * self.speed
        self.bullet_lifetime = BULLET_LIFETIME
        #gets the secific time the bullet was created 
        self.spawn_time = pygame.time.get_ticks()

    #updates the x and y coordinates and places a rectangle 
    def bullet_movement(self):
        self.x += self.x_vel
        self.y += self.y_vel

        self.rect.x = self.x
        self.rect.y = self.y

        if pygame.time.get_ticks() - self.spawn_time > self.bullet_lifetime:
            self.kill()

    def update(self):
        self.bullet_movement()


player = Player()

#creating groups for our sprites in game
all_sprites_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

all_sprites_group.add(player)


while True:
    #launching winodws
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #displaying 
    screen.blit(background, (0,0))
    all_sprites_group.draw(screen)
    all_sprites_group.update()
    # pygame.draw.rect(screen, "red",player.hitbox_rect,width=2)
    # pygame.draw.rect(screen, "green",player.rect,width=2)

    pygame.display.update()
    clock.tick(FPS)
    
