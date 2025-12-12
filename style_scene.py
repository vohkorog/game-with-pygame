import pygame 

class Style_scene:

    def __init__(self):
        
        self.mode = 0
        self.space_debounce = False
        self.x = []
        self.y = []

    def render(self, window):

        self.get_coordinate(window)
        for i in range(len(self.x)):  # или len(y_lines)
            # Вертикальная линия
            pygame.draw.line(window, (200, 200, 200), 
                            (self.x[i], 0), (self.x[i], 600), 1)
            # Горизонтальная линия
            pygame.draw.line(window, (200, 200, 200),
                            (0, self.y[i]), (800, self.y[i]), 1)
        

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if not self.space_debounce:
                
                self.mode = 1 - self.mode 
                #print(f"Режим изменен: {self.mode}")
                self.space_debounce = True
        else:
            self.space_debounce = False          
        

    def update(self):
        self.input()

    def get_coordinate(self, window):

        win_w = window.get_width() 
        win_h = window.get_height()

        for i in range(0, win_w, int(win_w/10)):
            self.x.append(i)

        for i in range(0, win_h, int(win_h/10)):
            self.y.append(i)