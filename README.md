# Dynamic Console Tic-Tac-Toe (OOP Style)

### Requirements
Python 3.12+

### Run
```bash
python trainee_cross_zeros.py
```

### Usage
```python
# Default 3x3 board
game = HrestyNoliki()

# Custom size
game = HrestyNoliki(size=5)

# Custom matrix (must be n×n, at least 3×3)
game = HrestyNoliki(matrix=[['*','*','*'],['*','*','*'],['*','*','*']])

game.game()
```

### Structure
```text
HrestyNoliki
├── __init__     — board initialization
├── display       — print board to console
├── check_winner  — check for a winner
├── player_move   — player input with validation
└── game          — game loop
```
