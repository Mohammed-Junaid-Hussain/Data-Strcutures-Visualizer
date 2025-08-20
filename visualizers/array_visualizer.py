
import pygame
from visualizers.base_visualizer import BaseVisualizer
from utils.colors import WHITE, GREEN, BLUE, YELLOW
from utils.settings import BAR_GAP, PADDING, FONT_NAME

class ArrayVisualizer(BaseVisualizer):
    def __init__(self, screen):
        super().__init__(screen)
        self.font_small = pygame.font.SysFont(FONT_NAME, 18)
        self.font = pygame.font.SysFont(FONT_NAME, 24)

    def draw(self, arr, highlight=None, info_text=None):
        self.clear()
        if not arr:
            return

        width = self.screen.get_width() // max(len(arr), 1)
        width = max(2, width - BAR_GAP)
        max_val = max(arr) if arr else 1
        h = self.screen.get_height()
        baseline = h - PADDING

        # draw bars
        for i, v in enumerate(arr):
            bar_h = int((v / max_val) * (h - 2 * PADDING))
            x = i * (width + BAR_GAP)
            y = baseline - bar_h
            color = WHITE
            if highlight and i in highlight:
                # different colors for first/second highlight if provided
                if highlight.index(i) == 0:
                    color = GREEN
                else:
                    color = BLUE
            pygame.draw.rect(self.screen, color, (x, y, width, bar_h))

        # overlay info text
        if info_text:
            text_surface = self.font_small.render(info_text, True, YELLOW)
            self.screen.blit(text_surface, (10, 10))

        pygame.display.flip()
