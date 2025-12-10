import pygame
import os

class Entity:

    def __init__(self, w: int, h: int, x: int, y: int, path: str):
        
        self._image_library = {}

        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.path = path

        enemy_image = self.get_image()
        self.enemy_scale_image = pygame.transform.scale(enemy_image, (self.w, self.h))

    def render(self, window):
        window.blit(self.enemy_scale_image, (self.x, self.y))

    def get_image(self):
        image = self._image_library.get(self.path)
        if image == None:
                canonicalized_path = self.path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                self._image_library[self.path] = image
        return image