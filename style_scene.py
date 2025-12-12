import pygame 

class Style_scene:
    def __init__(self):
        self.mode = 0
        self.space_debounce = False
    
    def render(self, window):
        # Рендерим сетку только если mode == 1
        if self.mode == 1:
            self.draw_grid(window)
    
    def draw_grid(self, window):
        """Рисует сетку линий"""
        width = window.get_width()
        height = window.get_height()
        color = (200, 200, 200)  # Серый цвет
        
        # Вертикальные линии (10 ячеек = 11 линий)
        for i in range(11):
            x = int(i * (width / 10))
            pygame.draw.line(window, color, (x, 0), (x, height), 1)
        
        # Горизонтальные линии
        for i in range(11):
            y = int(i * (height / 10))
            pygame.draw.line(window, color, (0, y), (width, y), 1)
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if not self.space_debounce:
                # Переключаем 0 ↔ 1
                self.mode = 1 - self.mode 
                print(f"Сетка: {'ВКЛ' if self.mode == 1 else 'ВЫКЛ'}")
                self.space_debounce = True
        else:
            self.space_debounce = False
    
    def update(self, window):
        self.input()  # Только обработка ввода
    
    def get_mode_scene(self):
        return self.mode