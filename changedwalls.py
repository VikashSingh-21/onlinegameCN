import pygame

allWalls = []
class Walls:
    def __init__(self, wallx, wally, wallwidth, wallheight):
        self.x = wallx
        self.y = wally
        self.width = wallwidth
        self.height = wallheight
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

# Create wall1 object
topBorder = Walls(0, 0, 1290, 30)
topBorder_rect = topBorder.get_rect()

leftBorder = Walls(0, 30, 30, 720)
leftBorder_rect = leftBorder.get_rect()

rightBorder = Walls(1260, 0, 30, 720)
rightBorder_rect = rightBorder.get_rect()

bottomBorder = Walls(30,690,1260,30)
bottomBorder_rect = bottomBorder.get_rect()


wall_1 = Walls(90,90,30,270)
wall_1_rect = wall_1.get_rect()

wall_2 = Walls(90, 330, 390, 30)
wall_2_rect = wall_2.get_rect()

wall_3 = Walls(450, 120, 30, 210)
wall_3_rect = wall_3.get_rect()

wall_4 = Walls(180,30,30,90)
wall_4_rect = wall_4.get_rect()

wall_5 = Walls(180,120,210,30)
wall_5_rect = wall_5.get_rect()

wall_6 = Walls(360,150,30,120)
wall_6_rect = wall_6.get_rect()

# bottom right flipped

wall_7 = Walls(1080,570,30,120)
wall_7_rect = wall_7.get_rect()

wall_8 = Walls(900,570,180,30)
wall_8_rect = wall_8.get_rect()

wall_9 = Walls(900,450,30,120)
wall_9_rect = wall_9.get_rect()

wall_10 = Walls(1170,360,30,270)
wall_10_rect = wall_10.get_rect()

wall_11 = Walls(810,360,360,30)
wall_11_rect = wall_11.get_rect()

wall_12 = Walls(810,390,30,210)
wall_12_rect = wall_12.get_rect()


# bottom left
wall_13 = Walls(180,510,30,180)
wall_13_rect = wall_13.get_rect()

wall_14 = Walls(90,600,90,30)
wall_14_rect = wall_14.get_rect()

wall_15 = Walls(210,540,390,30)
wall_15_rect = wall_15.get_rect()

wall_16 = Walls(360,630,30,60)
wall_16_rect = wall_16.get_rect()

wall_17 = Walls(480,570,30,60)
wall_17_rect = wall_17.get_rect()

# top right
wall_18 = Walls(1080,30,30,180)
wall_18_rect = wall_18.get_rect()

wall_19 = Walls(1110,90,90,30)
wall_19_rect = wall_19.get_rect()

wall_20 = Walls(690,150,390,30)
wall_20_rect = wall_20.get_rect()

wall_21 = Walls(900,30,30,60)
wall_21_rect = wall_21.get_rect()

wall_22 = Walls(780,90,30,60)
wall_22_rect = wall_22.get_rect()

# power up test
wall_23 = Walls(630,345,30,30)
wall_23_rect = wall_23.get_rect()

#borders
allWalls.append(topBorder_rect)
allWalls.append(leftBorder_rect)
allWalls.append(rightBorder_rect)
allWalls.append(bottomBorder_rect)

# top left
allWalls.append(wall_1.get_rect())
allWalls.append(wall_2_rect)
allWalls.append(wall_3_rect)
allWalls.append(wall_4_rect)
allWalls.append(wall_5_rect)
allWalls.append(wall_6_rect)

# bottom right flipped
allWalls.append(wall_7_rect)
allWalls.append(wall_8_rect)
allWalls.append(wall_9_rect)
allWalls.append(wall_10_rect)
allWalls.append(wall_11_rect)
allWalls.append(wall_12_rect)

# bottom left
allWalls.append(wall_13_rect)
allWalls.append(wall_14_rect)
allWalls.append(wall_15_rect)
allWalls.append(wall_16_rect)
allWalls.append(wall_17_rect)

# top right
allWalls.append(wall_18_rect)
allWalls.append(wall_19_rect)
allWalls.append(wall_20_rect)
allWalls.append(wall_21_rect)
allWalls.append(wall_22_rect)

# power up test
allWalls.append(wall_23_rect)