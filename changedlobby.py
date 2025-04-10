import pygame
import threading
import sys

class Lobby:
    def __init__(self, screen_width, screen_height,network):
        self.ready = 0
        self.running = True
        self.hostgame = "HOST"
        self.joingame = "JOIN"
        self.width = screen_width
        self.height = screen_height
        self.network = network
        
        

    def hostlobby(self, screen, code,sock,server_address):
        self.running = True
        while self.running:
            screen.fill((200, 200, 200))
            fontTitle = pygame.font.SysFont("Arial", 70)
            text = fontTitle.render("Hosting game", True, (0, 0, 0))
            screen.blit(text, (self.width/2 - 250, self.height/2 - 200))

            fontTitle = pygame.font.SysFont("Arial", 30)
            text = fontTitle.render(code, True, (0, 0, 0))
            screen.blit(text, (self.width/2, self.height/2 - 200))

            # Draw buttons
            fontButton = pygame.font.SysFont("Arial", 40)

            self.ready_button = pygame.Rect(self.width/2 - 200, 460, 400, 50)
            pygame.draw.rect(screen, (0, 0, 255), self.ready_button)
            ready_text = fontButton.render("READY", True, (255, 255, 255))
            screen.blit(ready_text, (self.width/2 - 30, 460))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ready_button.collidepoint(event.pos):
                        # print("ready")
                        ready_up = "READYUP"
                        sock.sendto(ready_up.encode("utf-8"), self.network.server_address)
                        sock.sendto(ready_up.encode("utf-8"), self.network.server_address)
                        # print("Ready button clicked")
                        self.running = False
                        break
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def joinlobby(self, screen, sock, server_address):
        screen.fill((200, 200, 200))
        fontTitle = pygame.font.SysFont("Arial", 70)
        Titletext = fontTitle.render("Joining game", True, (0, 0, 0))
        screen.blit(Titletext, (self.width/2 - 250, self.height/2 - 200))

        input_box = pygame.Rect(self.width/2 - 100, self.height/2 + 100, 200, 32)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ""
        self.running = True

        font = pygame.font.SysFont(None, 32)

        while self.running:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Handle mouse events
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False

                if active:
                    color = color_active
                else:
                    color = color_inactive

                # Handle keyboard events
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            # print(text)
                            codeattempt = "CODE:" + text
                            self.network.tcp(codeattempt,server_address)
                            text = ""
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            

            screen.fill((200, 200, 200))
            fontTitle = pygame.font.SysFont("Arial", 70)
            Titletext = fontTitle.render("Joining game", True, (0, 0, 0))
            screen.blit(Titletext, (self.width/2 - 250, self.height/2 - 200))

            # Render the current text
            txt_surface = font.render(text, True, (0, 0, 0))
            # Resize the box if the text is too long
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            # Blit the text
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            # Blit the input box rect
            pygame.draw.rect(screen, color, input_box, 2)

            # Update the display outside the event loop
            pygame.display.flip()

            if self.network.readyup != None:
                self.running = False

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.ready_button.collidepoint(mouse_pos):
                    return self.ready
