import pygame
from settings import *
from building import Building

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        
        self.buildings = pygame.sprite.Group()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    building = Building(*pygame.mouse.get_pos())
                    
                    for sprite in self.buildings:
                        if sprite.rect.colliderect(building.rect):
                            break
                    else:
                        self.buildings.add(building)
                    
            self.buildings.draw(self.screen)
            
            pygame.display.update()

                    
if __name__ == '__main__':
    game = Game()
    game.run()
