
import pygame
from utils.colors import WHITE, GREEN, GREY, BACKGROUND
from utils.settings import FONT_NAME

class Menu:
    def __init__(self, screen, title, options):
        self.screen = screen
        self.title = title
        self.options = options
        self.selected = 0
        self.font = pygame.font.SysFont(FONT_NAME, 32)
        self.title_font = pygame.font.SysFont(FONT_NAME, 40, bold=True)

    def draw(self):
        self.screen.fill(BACKGROUND)
        title_surf = self.title_font.render(self.title, True, WHITE)
        title_rect = title_surf.get_rect(center=(self.screen.get_width()//2, 100))
        self.screen.blit(title_surf, title_rect)

        for i, option in enumerate(self.options):
            color = GREEN if i == self.selected else WHITE
            text_surface = self.font.render(option, True, color)
            rect = text_surface.get_rect(center=(self.screen.get_width() // 2, 200 + i * 50))
            self.screen.blit(text_surface, rect)
        hint = "↑/↓ to move • Enter to select • Esc to quit"
        hint_surf = self.font.render("", True, GREY)
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return None
                    if event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        return self.options[self.selected]
            self.draw()
            clock.tick(30)
