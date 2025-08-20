
import pygame
import random
from utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT, INITIAL_FPS, MIN_FPS, MAX_FPS, FONT_NAME
from utils.colors import WHITE, GREY, YELLOW, BACKGROUND
from visualizers.array_visualizer import ArrayVisualizer
from menu import Menu

# Import algorithms
from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.sorting.insertion_sort import insertion_sort
from algorithms.sorting.selection_sort import selection_sort

ALGORITHMS = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
}

def build_steps(sort_func, arr):
    steps = []
    for state, highlight in sort_func(arr):
        # store a safe copy of state
        steps.append((state.copy(), tuple(highlight)))
    if not steps:
        steps.append((arr.copy(), ()))
    return steps

def draw_hud(screen, font_small, algorithm_name, fps, idx, total, playing):
    help_lines = [
        f"Algorithm: {algorithm_name}",
        f"Step: {idx+1}/{total}",
        f"Speed (FPS): {fps}",
        "[Space] Play/Pause  |  [←]/[→] Step  |  [R] Reshuffle  |  [↑]/[↓] Speed  |  [Esc] Exit",
    ]
    y = 8
    for line in help_lines:
        surf = font_small.render(line, True, YELLOW)
        screen.blit(surf, (10, y))
        y += 20
    # play/pause state
    state_text = "Playing" if playing else "Paused"
    surf = font_small.render(state_text, True, WHITE)
    screen.blit(surf, (SCREEN_WIDTH - 100, 8))

def visualize_sort(screen, arr, algorithm_name, sort_func):
    clock = pygame.time.Clock()
    visualizer = ArrayVisualizer(screen)
    font_small = pygame.font.SysFont(FONT_NAME, 18)

    steps = build_steps(sort_func, arr)
    idx = 0
    fps = INITIAL_FPS
    playing = True

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    playing = not playing
                elif event.key == pygame.K_RIGHT:
                    idx = min(idx + 1, len(steps) - 1)
                    playing = False
                elif event.key == pygame.K_LEFT:
                    idx = max(idx - 1, 0)
                    playing = False
                elif event.key == pygame.K_UP:
                    fps = min(MAX_FPS, fps + 1)
                elif event.key == pygame.K_DOWN:
                    fps = max(MIN_FPS, fps - 1)
                elif event.key == pygame.K_r:
                    # reshuffle and rebuild steps
                    random.shuffle(arr)
                    steps = build_steps(sort_func, arr)
                    idx = 0
                    playing = True

        # advance automatically if playing
        if playing and idx < len(steps) - 1:
            idx += 1

        # draw current step
        state, highlight = steps[idx]
        visualizer.draw(state, highlight, info_text=None)

        # HUD overlay
        draw_hud(screen, font_small, algorithm_name, fps, idx, len(steps), playing)

        pygame.display.flip()
        clock.tick(fps)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("DSA Visualizer")

    # Algorithm selection menu
    algo_menu = Menu(screen, "Choose Sorting Algorithm", list(ALGORITHMS.keys()) + ["Exit"])
    choice = algo_menu.run()
    if choice is None or choice == "Exit":
        pygame.quit()
        return

    # Array size menu
    size_menu = Menu(screen, "Choose Array Size", ["10", "30", "60", "Back"])
    size_choice = size_menu.run()
    if size_choice is None or size_choice == "Back":
        pygame.quit()
        return

    size = int(size_choice)
    arr = list(range(1, size + 1))
    random.shuffle(arr)

    # Run visualization with controls
    visualize_sort(screen, arr, choice, ALGORITHMS[choice])

    pygame.quit()

if __name__ == "__main__":
    main()
