import tkinter as tk
import math

def draw_heart(canvas, width, height):
    points = []

    # Parametric heart curve
    for t in range(0, 360):
        t_rad = math.radians(t)
        
        x = 16 * math.sin(t_rad)**3
        y = (13 * math.cos(t_rad) 
             - 5 * math.cos(2 * t_rad) 
             - 2 * math.cos(3 * t_rad) 
             - math.cos(4 * t_rad))
        
        # Scale and move to center
        x = x * 10 + width / 2
        y = -y * 10 + height / 2
        
        points.append((x, y))

    # Draw heart
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        canvas.create_line(x1, y1, x2, y2, fill="red", width=2)

# Create window
root = tk.Tk()
root.title("Heart GUI ❤️")

canvas_width = 400
canvas_height = 400

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

draw_heart(canvas, canvas_width, canvas_height)

root.mainloop()