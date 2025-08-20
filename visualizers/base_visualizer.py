
import pygame
from utils.colors import BACKGROUND

class BaseVisualizer:
    def __init__(self, screen):
        self.screen = screen

    def clear(self):
        self.screen.fill(BACKGROUND)
