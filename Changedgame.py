import pygame
from changedwalls import *
from changedplayer import *
from Changedstartscreen import *
from changedlobby import *
from client2server import *
from Hostserver import *
import time
import sys


# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 1290
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BLOEN Poppers")

clock = pygame.time.Clock()
n = CLIENTNetwork()

frametime = 1.0 / 60.0

BG = pygame.image.load("../sprites/grey.png")

def draw(players):
    screen.blit(BG, (0, 0))
    for wall in allWalls:
        pygame.draw.rect(screen, (0, 0, 0), wall)
    for player in players:
        player.draw(screen)
        if player.swordb and player.is_alive:
            player.drawSword(screen)

def mainmenu():
    menu = Menu(SCREEN_WIDTH,SCREEN_HEIGHT)
    menu.display_menu(screen)
    while True:
        action = menu.handle_input()
        if action == "HOST":
            # Start the game
            print("Hosting game")
            return "HOST"
        elif action == "JOIN":
            print("Joining game")
            return "PEER"

def Hostlobby(join):
    test1 = "test1"
    n.sendmess(test1)
    s = HOSTServerNetwork()
    code = s.code
    sendcode = "CODE:" + str(code)
    # tcp
    n.sendmess(sendcode)
    lobby = Lobby(SCREEN_WIDTH, SCREEN_HEIGHT,n)
    lobby.hostlobby(screen,code,n.client,n.server_address)
    test2 = "test2"
    n.sendmess(test2)

def Joinlobby(join):
    test1 = "test1"
    n.sendmess(test1)
    lobby = Lobby(SCREEN_WIDTH, SCREEN_HEIGHT,n)
    lobby.joinlobby(screen,n.client,n.server_address)
    test2 = "test2"
    n.sendmess(test2)

def maingame():
    print("maingame reached")
    time.sleep(0.1)
    player1 = Player(300,250,30,30,2,2,(255,0,0))
    player2 = Player(300,200,30,30,2,2,(0,0,255))
    player3 = None
    player4 = None
    
    print(str(n.numplayers) + "what")
    

    if n.numplayers >= 3:
        player3 = Player(250,200,30,30,2,2,(0,255,0))
        print("made player 3")
    if n.numplayers == 4:
        player4 = Player(300,200,30,30,2,2,(255,255,0))


    player = None
    allPLAYERSlist = []
    playerotherlist = []
    playerIDs = []
    

    if n.playerID == "PLAYER1":
        player = player1
        player.id = "PLAYER1"
        allPLAYERSlist.append(player)
        if player2: 
            playerotherlist.append(player2) 
            allPLAYERSlist.append(player2)
            playerIDs.append("PLAYER2")
        if player3: 
            playerotherlist.append(player3)
            allPLAYERSlist.append(player3)
            playerIDs.append("PLAYER3")
        if player4: 
            playerotherlist.append(player4)
            allPLAYERSlist.append(player4)
            playerIDs.append("PLAYER4")
    elif n.playerID == "PLAYER2":
        player = player2
        player.id = "PLAYER2"
        if player1: 
            playerotherlist.append(player1)
            allPLAYERSlist.append(player1)
            allPLAYERSlist.append(player)
            playerIDs.append("PLAYER1")
        if player3: 
            playerotherlist.append(player3)
            allPLAYERSlist.append(player3)
            playerIDs.append("PLAYER3")
        if player4: 
            playerotherlist.append(player4)
            allPLAYERSlist.append(player4)
            playerIDs.append("PLAYER4")
    elif n.playerID == "PLAYER3" and player3:
        player = player3

        player.id = "PLAYER3"
        if player1: 
            playerotherlist.append(player1)
            allPLAYERSlist.append(player1)
            playerIDs.append("PLAYER1")
        if player2: 
            playerotherlist.append(player2)
            allPLAYERSlist.append(player2)
            allPLAYERSlist.append(player)
            playerIDs.append("PLAYER2")
        if player4: 
            playerotherlist.append(player4)
            allPLAYERSlist.append(player4)
            playerIDs.append("PLAYER4")
    elif n.playerID == "PLAYER4" and player4:
        player = player4

        player.id = "PLAYER4"
        if player1:
            playerotherlist.append(player1)
            allPLAYERSlist.append(player1)
            playerIDs.append("PLAYER1")
        if player2:
            playerotherlist.append(player2)
            allPLAYERSlist.append(player2)
            playerIDs.append("PLAYER2")
        if player3:
            playerotherlist.append(player3)
            allPLAYERSlist.append(player3)
            allPLAYERSlist.append(player4)
            playerIDs.append("PLAYER3")
    else:
        print("Error: Invalid playerID received")
        return  # Exit the game loop if playerID not found

    player_isalive = {
        "PLAYER1": True,
        "PLAYER2": True,
        "PLAYER3": True if player3 else False,
        "PLAYER4": True if player4 else False
    }

    



    print(f"Assigned player: {n.playerID}")

    for allplayers in allPLAYERSlist:
            allplayers.facing = "down"

    previous_time = time.time()
    accumulator = 0.0

    # print("hondacivic")

    gameloop = True
    while gameloop:
        # quiting event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cheatmess = "CHEATER:" + player.id
                n.sendmess(cheatmess)
                gameloop = False
                

        current_time = time.time()
        delta_time = current_time - previous_time
        previous_time = current_time
        accumulator += delta_time

        while accumulator >= frametime:
            for player_id in player_isalive:
                if player_id == "PLAYER1":
                    player_isalive[player_id] = player1.is_alive
                elif player_id == "PLAYER2":
                    player_isalive[player_id] = player2.is_alive
                elif player_id == "PLAYER3" and player3:
                    player_isalive[player_id] = player3.is_alive
                elif player_id == "PLAYER4" and player4:
                    player_isalive[player_id] = player4.is_alive

            alive_players = [player_id for player_id, alive in player_isalive.items() if alive]
            print(alive_players)
            print(len(alive_players))

            if len(alive_players) == 1:
                winner = alive_players[0]
                winnermess = "WINNER: " + winner
                n.tcpconn(winnermess,n.server_address)
                time.sleep(0.1)
                break

            # print("hello im under the water")
            # get key
            key = pygame.key.get_pressed()
            # move player depending on keys pressed
            if key[pygame.K_a]:
                player.move("left")
                player.facing = "left"
            elif key[pygame.K_d]:
                player.move("right")
                player.facing = "right"
            if key[pygame.K_w]:
                player.move("up")
                player.facing = "up"
            elif key[pygame.K_s]:
                player.move("down")
                player.facing = "down"
            
            for wall in allWalls:
                if player.rect.colliderect(wall):
                    # If player collides with a wall, move the player other direction and cancel out movement
                    if key[pygame.K_a]:
                        player.move("right")
                        player.facing = "left"
                    elif key[pygame.K_d]:
                        player.move("left")
                        player.facing = "right"
                    if key[pygame.K_w]:
                        player.move("down")
                        player.facing = "up"
                    elif key[pygame.K_s]:
                        player.move("up")
                        player.facing = "down"
            
            player.updatePos(player.rect.x,player.rect.y)
            player.updateDamage()
            player.updateFacing()
            n.getPos(player.posistion)
            
                
            if n.cheater == player.id:
                # print("you are cheating")
                
                gameloop = False
                break
            # print(n.cheater)
            if n.cheater != player.id and n.cheater != None:
                playerIDrecv = n.cheater
                otherplayerindex = playerIDs.index(playerIDrecv)
                playerother = playerotherlist[otherplayerindex]
                playerother.is_alive = False

                n.cheater = None


            n.directionfac(player.Nfacing)

            all_players_positions = [n.player1x, n.player2x, n.player3x, n.player4x]
            
            # Update positions
            for pos in all_players_positions:
                if "X:" in pos and pos[0:7] != n.playerID:
                    playerIDrecv = pos[0:7]
                    otherplayerindex = playerIDs.index(playerIDrecv)
                    playerother = playerotherlist[otherplayerindex]
                    x_pos = int(pos.split("X:")[1].split("Y:")[0].strip())
                    y_pos = int(pos.split("Y:")[1].split()[0].strip())
                    playerother.rect.x = x_pos
                    playerother.rect.y = y_pos

            all_players_facing = [n.player1fac, n.player2fac, n.player3fac, n.player4fac]
            # update sword and dir
            for fac in all_players_facing:
                if "F:" in fac and pos[0:7] != n.playerID:
                    playerIDrecv = fac[0:7]
                    otherplayerindex = playerIDs.index(playerIDrecv)
                    playerother = playerotherlist[otherplayerindex]
                    playerother.facing = fac.split("F:")[1].split()[0].strip()
                    sworddraw = fac.split("S:")[1].split()[0].strip()
                    if sworddraw == "T":
                        # print("the world")
                        playerother.swordb = True
                    elif sworddraw == "F":
                        # print("mothra x godzilla")
                        playerother.swordb = False

            # get cooldown
            for allplayers in allPLAYERSlist:
                allplayers.getcooldown()
            
            # sword collision and damage
            for attacker in allPLAYERSlist:
                if attacker.swordb == True and attacker.cant_damaged == False and attacker.is_alive == True:
                    for defender in allPLAYERSlist:
                        if attacker != defender and attacker.swordrect.colliderect(defender.rect):
                            if not defender.is_damaged:
                                defender.damaged()
                                defender.is_damaged = True
                        else:
                            defender.is_damaged = False

            # draw sword
            if key[pygame.K_SPACE]:
                player.swordb = True
            if not key[pygame.K_SPACE]:
                player.swordb = False
            
            player.sword()
            
            for playerother in playerotherlist:
                playerother.sword()

            draw(allPLAYERSlist)
            accumulator -= frametime

        pygame.display.update()
        clock.tick(60)


def winner():
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False  # Exit the loop when quit event is detected
        winnermess = n.winner
        winner = winnermess.split("WINNER: ")[1].split("ACK:")[0]
        screen.fill((200, 200, 200))
        fontTitle = pygame.font.SysFont("Arial",70)
        text = fontTitle.render(winner, True, (0, 0, 0))
        screen.blit(text, (SCREEN_WIDTH/2 - 250, SCREEN_HEIGHT/2 - 200))
        pygame.display.update()


def main():
    join = mainmenu()
    if join == "HOST":
        print("host")
        Hostlobby(join)
    elif join == "PEER":
        print("lobby")
        Joinlobby(join)
    print("passed")
    maingame()
    winner()

if __name__ == "__main__":
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    main()