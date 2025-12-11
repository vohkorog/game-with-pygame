
import pygame
from entity import *

class TextureAdd:

    def __init__(self, path: str):

        self.path = path
        self.position = [0, 0] 
        self.mouse_click = 0
        self.list_entity = []
        self.last_mouse_state = False
        self.paint_style_state = 0

    def update(self):
        self.input()
        if self.mouse_click == 1:
            entity = Entity(50, 50, self.position[0], self.position[1], self.path)
            self.list_entity.append(entity)
        
    def input(self):
        event_mouse = pygame.mouse.get_pressed()
        event_keyboar = pygame.key.get_pressed()

        if event_keyboar[pygame.K_1]:
            self.paint_style_state = 0
        if event_keyboar[pygame.K_2]:
            self.paint_style_state = 1
        
        if self.paint_style_state == 0:
            if event_mouse[0] and not self.last_mouse_state:
                self.mouse_click = 1
                self.position = pygame.mouse.get_pos()
                #print(self.position)   # вывод координат клика мыши в консоли 
            else:
                self.mouse_click = 0
            if event_mouse[2]:
                self.list_entity.clear()
            
            self.last_mouse_state = event_mouse[0]

        if self.paint_style_state == 1:
            if event_mouse[0]:
                self.mouse_click = 1
                self.position = pygame.mouse.get_pos()
                #print(self.position)    # вывод координат клика мыши в консоли
            else:
                self.mouse_click = 0
            if event_mouse[2]:
                self.list_entity.clear()
            

    def render(self, window):
        for entit in self.list_entity:
            entit.render(window)
        
        
            


    
