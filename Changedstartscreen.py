import pygame
import sys

class Menu:
    def __init__(self,screen_width,screen_height):
        self.Host_button = 0
        self.quit_button = 0
        self.hostgame = "HOST"
        self.joingame = "JOIN"
        self.width = screen_width
        self.height = screen_height

    def display_menu(self, screen):
        screen.fill((200, 200, 200))
        fontTitle = pygame.font.SysFont("Arial",70)
        text = fontTitle.render("BLOEN Poppers", True, (0, 0, 0))
        screen.blit(text, (self.width/2 - 250, self.height/2 - 200))

        # Draw buttons
        self.Host_button = pygame.Rect(self.width/2 - 200, 320, 400, 50)
        pygame.draw.rect(screen, (255, 0, 0), self.Host_button)
        fontButton = pygame.font.SysFont("Arial",40)
        play_text = fontButton.render("Host Game", True, (255, 255, 255))
        screen.blit(play_text, (self.width/2 - 100, 320))

        self.Join_button = pygame.Rect(self.width/2 - 200, 390, 400, 50)
        pygame.draw.rect(screen, (0, 255, 0), self.Join_button)
        fontButton = pygame.font.SysFont("Arial",40)
        play_text = fontButton.render("Join Game", True, (255, 255, 255))
        screen.blit(play_text, (self.width/2 - 100, 390))

        self.quit_button = pygame.Rect(self.width/2 - 200, 460, 400, 50)
        pygame.draw.rect(screen, (0, 0, 255), self.quit_button)
        quit_text = fontButton.render("Quit", True, (255, 255, 255))
        screen.blit(quit_text, (self.width/2 - 30, 460))

        pygame.display.update()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.Host_button.collidepoint(mouse_pos):
                    return self.hostgame
                elif self.Join_button.collidepoint(mouse_pos):
                    return self.joingame
                elif self.quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

