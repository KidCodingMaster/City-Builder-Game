import pygame

class Building(pygame.sprite.Sprite):
    def __init__(self, x, y, groups=()):
        super().__init__(groups)
        
        self.x = x
        self.y = y
        
        self.image = pygame.Surface((10, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
    def update(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        