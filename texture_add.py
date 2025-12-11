
import pygame
from entity import *

class TextureAdd:

    def __init__(self, path: str):

        self.path = path
        self.position = [0, 0] 
        self.mouse_click = 0
        self.list_entity = []

    def update(self):
        self.input()
        if self.mouse_click == 1:
            entity = Entity(50, 50, self.position[0], self.position[1], self.path)
            self.list_entity.append(entity)
        
    def input(self):
        event = pygame.mouse.get_pressed()

        if event[0]:
            self.mouse_click = 1
            self.position = pygame.mouse.get_pos()
            print(self.position)    
        else:
            self.mouse_click = 0
        if event[2]:
            self.list_entity.clear()

    def render(self, window):
        for entit in self.list_entity:
            entit.render(window)
        
        
            


    
