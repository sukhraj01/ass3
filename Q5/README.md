# Kaooa - Vulture and Crows Board Game

A Python implementation of the traditional Indian abstract strategy game Kaooa (also known as Vulture and Crows), built using the Turtle graphics library.

## About the Game

Kaooa is a two-player asymmetric board game from India where seven crows battle against one vulture. The game is played on a pentagram (five-pointed star) board with 10 intersection points.

## Game Rules

### Setup
- The game board is a pentagram with 10 intersection points
- Player 1 controls 7 crow pieces (black circles)
- Player 2 controls 1 vulture piece (red circle with 'V')

### Placement Phase
1. **Crows move first**: Click on any empty point to place a crow
2. **Vulture places next**: After the first crow is placed, the vulture player places their piece on any empty point
3. Players alternate placing pieces until all 7 crows and 1 vulture are on the board

### Movement Phase
Once all pieces are placed, players alternate turns:

**Crow Movement:**
- Crows can move one space along the board lines to an adjacent empty point
- Crows cannot jump or capture

**Vulture Movement:**
- The vulture can either:
  - Move one space along the board lines to an adjacent empty point, OR
  - Capture a crow by jumping over it (like checkers/draughts)
- Captures are made by jumping over an adjacent crow to land on an empty point on the opposite side
- Multiple captures in one turn are not allowed

### Winning Conditions

**Vulture Wins:** Capture 4 or more crows

**Crows Win:** Trap the vulture so it has no legal moves (cannot move or capture)

## Installation

### Requirements
- Python 3.6 or higher
- Turtle graphics library (included with Python standard library)

### Running the Game

```bash
python3 kaooa.py
```

Or make it executable:

```bash
chmod +x kaooa.py
./kaooa.py
```

## How to Play

1. **Starting the Game:**
   - Run `kaooa.py`
   - A window will open showing the pentagram board

2. **Placement Phase (Turns 1-8):**
   - Click on any empty intersection point to place your piece
   - Crows (black) and Vulture (red) alternate placing pieces
   - Status display shows how many crows have been placed

3. **Movement Phase:**
   - Click on your piece to select it (it will be highlighted in yellow)
   - Click on a valid destination point to move your piece
   - Click on the same piece again to deselect

4. **Making Captures (Vulture only):**
   - Select your vulture piece
   - Click on an empty point that is two spaces away with a crow in between
   - The vulture will jump over and capture the crow

5. **Game Status:**
   - The left side of the screen shows:
     - Current player's turn
     - Number of crows placed (during placement phase)
     - Number of crows captured by vulture
     - Current game phase
     - Winner announcement when game ends

## Game Features

- **Interactive GUI:** Click-based interface using Turtle graphics
- **Visual Board:** Pentagram board with clearly marked intersection points
- **Piece Representation:**
  - Crows: Black filled circles
  - Vulture: Red filled circle with white 'V' label
- **Move Validation:** Only legal moves are allowed
- **Capture Detection:** Automatic detection of vulture captures
- **Win Condition Checking:** Automatic detection of game end conditions
- **Status Display:** Real-time game state information

## Strategy Tips

### For Crow Players:
- Work together to surround the vulture
- Block potential escape routes
- Stay connected as a group
- Move crows toward the center to limit vulture movement

### For Vulture Players:
- Try to capture isolated crows
- Keep moving to avoid being trapped
- Target crows on the outer edges
- Create capture opportunities by forcing crow movements

## Code Structure

The game is implemented as a single Python file with the following main components:

### `KaooaGame` Class
Main game controller containing:

- **Initialization:**
  - `__init__()`: Initialize game state
  - `setup_window()`: Create the game window
  - `setup_board()`: Calculate board geometry and connections
  - `reset_game()`: Reset game state

- **Drawing Methods:**
  - `draw_board()`: Draw the pentagram board
  - `draw_pieces()`: Render all game pieces
  - `draw_piece()`: Draw individual piece
  - `draw_status()`: Display game information
  - `highlight_selected()`: Highlight selected piece

- **Game Logic:**
  - `is_valid_move()`: Validate regular moves
  - `is_valid_capture()`: Validate capture moves
  - `get_valid_moves()`: Get all legal moves for a piece
  - `is_vulture_trapped()`: Check if vulture is trapped
  - `check_win_condition()`: Determine if game is won

- **User Interaction:**
  - `handle_click()`: Process mouse clicks
  - `get_point_from_click()`: Map screen coordinates to board points

### Game Board Structure

The board consists of:
- 5 outer points (star tips)
- 5 inner points (star intersections)
- 30 connections (edges) between points

All moves and captures must follow these connections.

## Technical Details

- **Graphics Library:** Python Turtle
- **Board Geometry:** Mathematical calculation of pentagram vertices
- **Click Detection:** Distance-based point selection (30-pixel radius)
- **Move Validation:** Graph-based connectivity checking
- **Capture Detection:** Collinearity checking for three-point alignment

## References

1. [Kaooa: Traditional Abstract Strategy Hunt Game from India](https://www.whatdowedoallday.com/kaooa/)
2. [Kaooa Game Video Tutorial](https://www.youtube.com/watch?v=Jzeug1XTRQM)
3. [Kaooa - Wikipedia](https://en.wikipedia.org/wiki/Kaooa)

## Troubleshooting

**Issue:** Window doesn't open
- **Solution:** Ensure Python's Turtle graphics is properly installed. Try running `python3 -m turtle` to test.

**Issue:** Clicks not registering
- **Solution:** Click directly on the brown dots (intersection points). Make sure you're clicking within about 30 pixels of a point.

**Issue:** Can't make a move
- **Solution:** Ensure:
  - It's your turn (check status display)
  - All pieces are placed before trying to move
  - You're moving to a valid adjacent point
  - The destination point is empty

## License

This is an educational implementation of a traditional game. Feel free to use and modify for learning purposes.
