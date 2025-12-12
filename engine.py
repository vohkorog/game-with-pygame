import pygame
from entity import *
from texture_add import *
from style_scene import *

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
        
        self.texture = TextureAdd("src\\image\\texture.jpg")
        self.entity = Entity(38, 30, 60, 60, "src\\image\\ball.png")
        self.style_scene = Style_scene()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
    
    
    def run(self):
        self.running = True
        clock = pygame.time.Clock()
        
        while self.running:
            
            self.running = self.handle_events()
            self.update()
            self.screen.fill((255, 255, 255))
            self.render()
            clock.tick(60)  
            fps = clock.get_fps()
            print(int(fps))
            
            pygame.display.flip()
            
        pygame.quit()

    def render(self):
        self.entity.render(self.screen)
        self.texture.render(self.screen)
        self.style_scene.render(self.screen)



    def update(self):
        self.entity.update()
        self.texture.update()
        self.style_scene.update()
        self.input()

    def input(self):
        pass
