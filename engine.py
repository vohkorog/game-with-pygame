import pygame
import os
from entity import *

class Engine:

    def __init__(self, width: int = 800, height: int = 600, title: str = "my_game"):

        self.width = width
        self.height = height
        self.title = title

        self.screen = None 
        self.running = False
        
        self.init_window()
        self.init_object()

    def init_window(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def init_object(self):
        self.entity = Entity(300, 300, 60, 60, "src\\image\\ball.png")

        #enemy_image = self.get_image("src\\image\\ball.png")
        #self.enemy_scale_image = pygame.transform.scale(enemy_image, (150, 100))
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
    
    
    def run(self):
        
        self.running = True
        while self.running:
            self.running = self.handle_events()
            self.screen.fill((255, 255, 255))
            self.render()
            pygame.display.flip()
        pygame.quit()

    def render(self):
        self.entity.render(self.screen)
        #self.entity.render(self.screen)
        #self.screen.blit(self.enemy_scale_image, (100,100))

