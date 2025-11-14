#!/usr/bin/env python3
"""
Kaooa - Traditional Indian Board Game (Vulture and Crows)
A two-player abstract strategy game where 7 crows battle against 1 vulture.
"""

import turtle
import math


class KaooaGame:
    """Main game class for Kaooa board game."""

    def __init__(self):
        """Initialize the game board and state."""
        self.setup_window()
        self.setup_board()
        self.reset_game()

    def setup_window(self):
        """Setup the turtle graphics window."""
        self.screen = turtle.Screen()
        self.screen.setup(width=800, height=900)
        self.screen.bgcolor("white")
        self.screen.title("Kaooa - Vulture and Crows")
        self.screen.tracer(0)  # Turn off animation for faster drawing

    def setup_board(self):
        """Calculate board positions and setup drawing turtle."""
        # Center of the board
        self.center_x = 0
        self.center_y = 50
        self.radius = 200

        # Calculate the 10 intersection points of the pentagram
        self.points = []

        # 5 outer points of the pentagon (star tips)
        for i in range(5):
            angle = math.radians(90 + i * 72)  # Start from top
            x = self.center_x + self.radius * math.cos(angle)
            y = self.center_y + self.radius * math.sin(angle)
            self.points.append((x, y))

        # 5 inner points (star intersections)
        inner_radius = self.radius * 0.382  # Golden ratio approximation
        for i in range(5):
            angle = math.radians(90 + 36 + i * 72)  # Offset by 36 degrees
            x = self.center_x + inner_radius * math.cos(angle)
            y = self.center_y + inner_radius * math.sin(angle)
            self.points.append((x, y))

        # Define valid connections (edges) between points
        # NOTE: The star lines (0-2, 2-4, etc.) are VISUAL but pass through inner points
        # You must move through the inner intersections, not jump over them!
        self.connections = [
            # Inner pentagon edges
            (5, 6), (6, 7), (7, 8), (8, 9), (9, 5),
            # Radial connections from outer to inner
            (0, 5), (0, 9), (1, 5), (1, 6), (2, 6),
            (2, 7), (3, 7), (3, 8), (4, 8), (4, 9)
        ]

        # Create drawing turtle
        self.drawer = turtle.Turtle()
        self.drawer.hideturtle()
        self.drawer.speed(0)

    def reset_game(self):
        """Reset game state to initial conditions."""
        # Game state
        self.board = [None] * 10  # None, 'crow', or 'vulture'
        self.current_player = 'crow'  # Crow starts
        self.crows_placed = 0
        self.crows_captured = 0
        self.vulture_placed = False
        self.selected_point = None
        self.game_over = False
        self.winner = None

        # Piece turtles for animation
        self.piece_turtles = {}

    def draw_board(self):
        """Draw the pentagram board."""
        self.drawer.clear()

        # Draw title
        self.drawer.penup()
        self.drawer.goto(0, 320)
        self.drawer.color("black")
        style = ('Arial', 24, 'bold')
        self.drawer.write("KAOOA", align="center", font=style)

        # Draw connections (edges)
        self.drawer.color("brown")
        self.drawer.width(3)
        for p1, p2 in self.connections:
            self.drawer.penup()
            self.drawer.goto(self.points[p1])
            self.drawer.pendown()
            self.drawer.goto(self.points[p2])

        # Draw intersection points
        for i, point in enumerate(self.points):
            self.drawer.penup()
            self.drawer.goto(point)
            self.drawer.dot(15, "brown")

        # Draw status bar
        self.draw_status()

    def draw_status(self):
        """Draw game status information."""
        self.drawer.penup()
        self.drawer.goto(-350, -300)
        self.drawer.color("black")
        style = ('Arial', 12, 'normal')

        # Don't show turn if game is over
        if not self.game_over:
            status_text = f"Turn: {self.current_player.upper()}\n"
        else:
            status_text = ""
            
        status_text += f"Crows Placed: {self.crows_placed}/7\n"
        status_text += f"Crows Captured: {self.crows_captured}/4\n"

        if self.crows_placed < 7:
            if not self.vulture_placed:
                status_text += "\nPhase: Placement (placing pieces)"
            else:
                status_text += "\nPhase: Crow Placement + Vulture Hunting"
                if self.current_player == 'crow':
                    status_text += "\n(Click to place crow)"
                else:
                    status_text += "\n(Vulture: click vulture, then destination)"
        else:
            status_text += "\nPhase: Full Movement (both players move)"
            status_text += "\n(Click piece, then destination)"

        if self.game_over:
            status_text += f"\n\n*** GAME OVER ***\n{self.winner.upper()} WINS!"

        self.drawer.write(status_text, font=style)

    def draw_pieces(self):
        """Draw all pieces on the board."""
        # Clear existing piece turtles
        for t in self.piece_turtles.values():
            t.clear()
            t.hideturtle()
        self.piece_turtles.clear()

        # Draw current pieces
        for i, piece in enumerate(self.board):
            if piece:
                self.draw_piece(i, piece)

    def draw_piece(self, point_index, piece_type):
        """Draw a single piece at a point."""
        if point_index in self.piece_turtles:
            self.piece_turtles[point_index].clear()
        else:
            t = turtle.Turtle()
            t.hideturtle()
            t.speed(0)
            self.piece_turtles[point_index] = t

        t = self.piece_turtles[point_index]
        x, y = self.points[point_index]

        if piece_type == 'crow':
            # Draw crow (black circle)
            t.penup()
            t.goto(x, y - 20)
            t.pendown()
            t.fillcolor("black")
            t.begin_fill()
            t.circle(20)
            t.end_fill()
        elif piece_type == 'vulture':
            # Draw vulture (red circle with V)
            t.penup()
            t.goto(x, y - 20)
            t.pendown()
            t.fillcolor("red")
            t.begin_fill()
            t.circle(20)
            t.end_fill()
            t.penup()
            t.goto(x, y - 8)
            t.color("white")
            t.write("V", align="center", font=('Arial', 16, 'bold'))

    def get_point_from_click(self, x, y):
        """Find the nearest point to a click location."""
        min_dist = float('inf')
        nearest_point = None

        for i, (px, py) in enumerate(self.points):
            dist = math.sqrt((x - px)**2 + (y - py)**2)
            if dist < min_dist and dist < 30:  # Within 30 pixels
                min_dist = dist
                nearest_point = i

        return nearest_point

    def is_valid_move(self, from_point, to_point):
        """Check if a move is valid."""
        # Destination must be empty
        if self.board[to_point] is not None:
            return False

        # Check if points are connected
        if (from_point, to_point) not in self.connections and \
           (to_point, from_point) not in self.connections:
            return False

        return True

    def is_valid_capture(self, from_point, to_point):
        """Check if a capture move is valid for vulture."""
        # Must be vulture
        if self.board[from_point] != 'vulture':
            return False
        
        # Destination must be empty
        if self.board[to_point] is not None:
            return False
        
        # Capture means jumping, so destination must NOT be adjacent
        # (adjacent moves are handled by is_valid_move)
        if (from_point, to_point) in self.connections or (to_point, from_point) in self.connections:
            return False

        # Find if there's EXACTLY ONE crow between the two points
        crow_count = 0
        crow_found = None
        
        for mid_point in range(10):
            if self.board[mid_point] == 'crow':
                # Check if from -> mid -> to is a valid straight line
                if self.is_capture_path(from_point, mid_point, to_point):
                    crow_count += 1
                    crow_found = mid_point
        
        # Must have EXACTLY one crow in the path (can't jump over 2 crows)
        return crow_count == 1

    def is_capture_path(self, from_p, mid_p, to_p):
        """Check if three points form a valid capture path."""
        # Get the actual point coordinates
        p1 = self.points[from_p]
        p2 = self.points[mid_p]
        p3 = self.points[to_p]

        # Check if they are collinear (on the same straight line)
        cross = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])
        
        # Must be on same line (cross product near 0)
        # Increase tolerance to 3.0 to catch all valid straight paths (some are ~2.09)
        if abs(cross) > 3.0:
            return False
        
        # Check if mid_p is actually BETWEEN from_p and to_p using distance
        dist_1_2 = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2) ** 0.5
        dist_2_3 = ((p3[0] - p2[0])**2 + (p3[1] - p2[1])**2) ** 0.5
        dist_1_3 = ((p3[0] - p1[0])**2 + (p3[1] - p1[1])**2) ** 0.5
        
        # mid_p is between if dist(1,2) + dist(2,3) ≈ dist(1,3)
        # This ensures we count ALL crows between start and dest
        return abs((dist_1_2 + dist_2_3) - dist_1_3) < 2.0

    def get_captured_crow(self, from_point, to_point):
        """Get the index of crow captured in a move."""
        for mid_point in range(10):
            if self.board[mid_point] == 'crow':
                if self.is_capture_path(from_point, mid_point, to_point):
                    return mid_point
        return None

    def get_valid_moves(self, point):
        """Get all valid moves from a point."""
        valid_moves = []
        piece = self.board[point]

        if piece == 'crow':
            # Crows can only move to adjacent empty points
            for i in range(10):
                if self.board[i] is None and self.is_valid_move(point, i):
                    valid_moves.append(i)

        elif piece == 'vulture':
            # Vulture can move or capture
            for i in range(10):
                if self.board[i] is None:
                    if self.is_valid_move(point, i):
                        valid_moves.append(i)
                    elif self.is_valid_capture(point, i):
                        valid_moves.append(i)

        return valid_moves

    def is_vulture_trapped(self):
        """Check if vulture has no valid moves."""
        for i in range(10):
            if self.board[i] == 'vulture':
                if len(self.get_valid_moves(i)) == 0:
                    return True
        return False

    def check_win_condition(self):
        """Check if game is won."""
        # Vulture wins if 4 crows captured
        if self.crows_captured >= 4:
            self.game_over = True
            self.winner = 'vulture'  # VULTURE wins when capturing 4 crows
            return True

        # Crows win if vulture is trapped (only after all crows are placed)
        if self.crows_placed == 7 and self.is_vulture_trapped():
            self.game_over = True
            self.winner = 'crow'  # CROWS win when vulture is trapped
            return True

        return False

    def handle_click(self, x, y):
        """Handle mouse click events."""
        if self.game_over:
            return

        point = self.get_point_from_click(x, y)
        if point is None:
            return

        # PHASE 1: Crow placement (crows still being placed)
        if self.crows_placed < 7:
            # If it's crow's turn, place a crow
            if self.current_player == 'crow' and self.board[point] is None:
                self.board[point] = 'crow'
                self.crows_placed += 1
                self.current_player = 'vulture'
                self.selected_point = None
                self.update_display()
            
            # If it's vulture's turn and vulture not placed yet, place vulture
            elif self.current_player == 'vulture' and not self.vulture_placed and self.board[point] is None:
                self.board[point] = 'vulture'
                self.vulture_placed = True
                self.current_player = 'crow'
                self.selected_point = None
                self.update_display()
            
            # If vulture already placed and it's vulture's turn, vulture can MOVE/CAPTURE
            elif self.current_player == 'vulture' and self.vulture_placed:
                if self.selected_point is None:
                    # Select the vulture piece
                    if self.board[point] == 'vulture':
                        self.selected_point = point
                        self.highlight_selected(point)
                else:
                    # Try to move/capture with the vulture
                    from_point = self.selected_point
                    to_point = point

                    if from_point == to_point:
                        # Deselect
                        self.selected_point = None
                        self.update_display()
                    elif self.is_valid_move(from_point, to_point):
                        # Simple move
                        self.board[to_point] = 'vulture'
                        self.board[from_point] = None
                        self.current_player = 'crow'
                        self.selected_point = None
                        self.update_display()
                        self.check_win_condition()  # Check if vulture is now trapped
                    elif self.is_valid_capture(from_point, to_point):
                        # Capture move
                        crow_point = self.get_captured_crow(from_point, to_point)
                        if crow_point is not None:
                            self.board[to_point] = 'vulture'
                            self.board[from_point] = None
                            self.board[crow_point] = None
                            self.crows_captured += 1
                            self.current_player = 'crow'
                            self.selected_point = None
                            self.update_display()
                            self.check_win_condition()  # Check win after capture

        # PHASE 2: Full movement phase (all 7 crows placed, both players can move)
        else:
            if self.selected_point is None:
                # Select a piece to move
                if self.board[point] == self.current_player:
                    self.selected_point = point
                    self.highlight_selected(point)
            else:
                # Try to move selected piece
                from_point = self.selected_point
                to_point = point

                if from_point == to_point:
                    # Deselect
                    self.selected_point = None
                    self.update_display()
                elif self.board[from_point] == self.current_player:
                    # Try to make the move
                    if self.is_valid_move(from_point, to_point):
                        # Simple move
                        self.board[to_point] = self.board[from_point]
                        self.board[from_point] = None
                        self.current_player = 'vulture' if self.current_player == 'crow' else 'crow'
                        self.selected_point = None
                        self.update_display()
                        self.check_win_condition()
                    elif self.current_player == 'vulture' and self.is_valid_capture(from_point, to_point):
                        # Capture move
                        crow_point = self.get_captured_crow(from_point, to_point)
                        if crow_point is not None:
                            self.board[to_point] = 'vulture'
                            self.board[from_point] = None
                            self.board[crow_point] = None
                            self.crows_captured += 1
                            self.current_player = 'crow'
                            self.selected_point = None
                            self.update_display()
                            self.check_win_condition()

    def highlight_selected(self, point):
        """Highlight the selected piece."""
        x, y = self.points[point]
        self.drawer.penup()
        self.drawer.goto(x, y - 30)
        self.drawer.color("yellow")
        self.drawer.pendown()
        self.drawer.width(3)
        self.drawer.circle(30)
        self.screen.update()

    def update_display(self):
        """Update the entire display."""
        self.draw_board()
        self.draw_pieces()
        self.screen.update()

    def play(self):
        """Start the game."""
        self.update_display()
        self.screen.onclick(self.handle_click)

        # Instructions
        instructions = turtle.Turtle()
        instructions.hideturtle()
        instructions.penup()
        instructions.goto(0, -350)
        instructions.color("blue")
        style = ('Arial', 10, 'italic')
        inst_text = "Rules: Crows go first. Place all 7 crows and 1 vulture, then move pieces.\n"
        inst_text += "Vulture captures by jumping over crows. Vulture wins by capturing 4 crows.\n"
        inst_text += "Crows win by trapping the vulture (no valid moves)."
        instructions.write(inst_text, align="center", font=style)

        self.screen.mainloop()


def main():
    """Main entry point for the game."""
    print("Starting Kaooa - Vulture and Crows Game")
    print("=" * 50)
    print("\nGame Rules:")
    print("- 2 players: Crows (7 pieces) vs Vulture (1 piece)")
    print("- Crows move first and place pieces on the board")
    print("- After all pieces are placed, players take turns moving")
    print("- Vulture can capture crows by jumping over them")
    print("- Vulture wins by capturing 4 crows")
    print("- Crows win by trapping the vulture")
    print("\nStarting game window...")
    print("=" * 50)

    game = KaooaGame()
    game.play()


if __name__ == "__main__":
    main()