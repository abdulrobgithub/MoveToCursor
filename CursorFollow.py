import tkinter as tk
import time

CANVAS_SIZE = 400
BALL_DIAMETER = 50
PAUSE_TIME = 1 / 50

def main():
    root = tk.Tk()
    root.title("Ball Follow Mouse")
    canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE, bg="white")
    canvas.pack()

    # Create a ball
    ball = canvas.create_oval(
        0, 0,
        BALL_DIAMETER, BALL_DIAMETER,
        fill='blue'
    )

    def update_position(event):
        """Move the ball to the mouse pointer location."""
        mouse_x, mouse_y = event.x, event.y
        canvas.moveto(ball, mouse_x - BALL_DIAMETER // 2, mouse_y - BALL_DIAMETER // 2)

    # Bind mouse motion to update_position
    canvas.bind('<Motion>', update_position)

    # Run the Tkinter main loop
    root.mainloop()

if __name__ == '__main__':
    main()
