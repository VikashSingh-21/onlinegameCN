import pygame
import socket
import time

class Player:
    def __init__(self, x, y, width, height, vel_x, vel_y,color):
        self.rect = pygame.Rect(x, y, width, height)
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.color = color

        self.posistion = "X:" + str(self.rect.x) + "Y:" + str(self.rect.y) + "\n"
        self.facing = "down"

        # hp
        self.hp = 50
        self.is_damaged = False
        self.is_alive = True
        self.lastdamged = 0

        # sword
        self.swordx = 0
        self.swordy = 0
        self.swordb = False
        self.swordwidth = 15
        self.swordheight = 30
        self.swordrect = pygame.Rect(0,0,self.swordwidth,self.swordheight)

        # cooldown
        self.cooldown = 180
        self.cooldowncounter = 300
        self.can_get_damged = True

        self.id = None

    def move(self, direction):
        if direction == "left":
            self.rect.x -= self.vel_x
            self.facing = "left"
        elif direction == "right":
            self.rect.x += self.vel_x
            self.facing = "right"
        elif direction == "up":
            self.rect.y -= self.vel_y
            self.facing = "up"
        elif direction == "down":
            self.rect.y += self.vel_y
            self.facing = "down"

    def damaged(self):
        if self.hp > 100:
            self.hp = 100
        if self.can_get_damged == True:
            self.hp -= 25
            self.cooldowncounter = 0
            self.cant_damaged = True
        # if self.hp <= 0:
        #     self.hp = 0
            

        if self.hp <= 0:
            self.hp = 0 
            self.is_alive = False
        # print("damaged")
        # print(self.hp)

    def getcooldown(self):
        if self.cooldowncounter >= self.cooldown:
            self.can_get_damged = True
            self.vel_x = 2
            self.vel_y = 2
            self.cant_damaged = False
        else:
            self.cooldowncounter += 1
            self.vel_x = 3
            self.vel_y = 3
            self.can_get_damged = False


    def sword(self):
        if self.facing == "left":
            self.swordrect.x = self.rect.x - 30
            self.swordrect.y = self.rect.y + 7
            self.swordrect.width = 30
            self.swordrect.height = 15
        elif self.facing == "right":
            self.swordrect.x = self.rect.x + 30
            self.swordrect.y = self.rect.y + 7
            self.swordrect.width = 30
            self.swordrect.height = 15
        elif self.facing == "up":
            self.swordrect.x = self.rect.x + 7
            self.swordrect.y = self.rect.y - 30
            self.swordrect.width = 15
            self.swordrect.height = 30
        elif self.facing == "down":
            self.swordrect.x = self.rect.x + 7
            self.swordrect.y = self.rect.y + 30
            self.swordrect.width = 15
            self.swordrect.height = 30


    def draw(self, screen):
        if self.is_alive == True:
            if self.can_get_damged == True:
                pygame.draw.rect(screen, self.color, self.rect)
            elif self.can_get_damged == False and pygame.time.get_ticks() % 200 < 100:
                pygame.draw.rect(screen, self.color, self.rect)

    def drawSword(self,screen):
        if self.swordb == True:
            pygame.draw.rect(screen, (0, 255, 0), self.swordrect)

    def updatePos(self,x_pos,y_pos):
        self.posistion = self.id + "X: " + str(x_pos) + " Y:" + str(y_pos) + "\n"

    def updateDamage(self):
        self.Nisdamaged = self.id + "DMG:" + str(self.is_damaged) + "\n"

    def updateFacing(self):
        if self.swordb == True:
            self.Nfacing = self.id + " S: " + "T " + "F: " + str(self.facing) + "\n"
        elif self.swordb == False:
            self.Nfacing = self.id + " S: " + "F " + "F: " + str(self.facing) + "\n"