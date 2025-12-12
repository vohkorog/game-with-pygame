import pygame 

class Style_scene:

    def __init__(self):
        
        self.mode = 0
        self.space_debounce = False
        self.x = []
        self.y = []

    def render(self, window):

        width = window.get_width()
        height = window.get_height()
        
        # Рисуем сразу без сохранения в списки
        cell_width = width / 10
        cell_height = height / 10
        
        # Вертикальные линии
        for i in range(11):  # 10 ячеек = 11 линий
            x = i * cell_width
            pygame.draw.line(window, (200, 200, 200), 
                           (x, 0), (x, height), 1)
        
        # Горизонтальные линии
        for i in range(11):
            y = i * cell_height
            pygame.draw.line(window, (200, 200, 200),
                           (0, y), (width, y), 1)
        

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