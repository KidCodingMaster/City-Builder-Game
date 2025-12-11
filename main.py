import pygame
from settings import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
if __name__ == '__main__':
    game = Game()
    game.run()
