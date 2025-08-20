
# DSA Visualizer (Python + Pygame)

A modular, extensible DSA visualizer starting with arrays and sorting.
Includes **pause/resume**, **step forward/backward**, **speed control**, and **reshuffle**.

## Features
- Sorting algorithms: Bubble, Insertion, Selection
- Interactive controls:
  - Space: Play/Pause
  - Left/Right: Step backward/forward
  - Up/Down: Increase/Decrease speed (FPS)
  - R: Reshuffle current array and restart visualization
  - Esc: Exit
- Menu to pick algorithm and array size

## Project Structure
```
dsa_visualizer/
├── main.py
├── menu.py
├── algorithms/
│   └── sorting/
│       ├── bubble_sort.py
│       ├── insertion_sort.py
│       └── selection_sort.py
├── visualizers/
│   ├── base_visualizer.py
│   └── array_visualizer.py
└── utils/
    ├── colors.py
    └── settings.py
```

## Setup
```bash
pip install pygame
```

## Run
```bash
python main.py
```

## Extend
- Add new algorithms in `algorithms/sorting/` returning a generator that yields `(state_list, highlight_indices)`.
- For new data structures (Stacks, Trees, Graphs), add a new visualizer in `visualizers/` and a menu entry.
