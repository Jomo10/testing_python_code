import tkinter as tk

# Function to handle left and right clicks
def click(event):
    if event.num == 1:  # Left click
        color = "white"
    elif event.num == 3:  # Right click
        color = "black"
    canvas.create_rectangle(event.x, event.y, event.x + 1, event.y + 1, outline=color, fill=color)

# Initialize the main window
root = tk.Tk()
root.title("Road Map Designer")

# Create a canvas with a grey background
canvas = tk.Canvas(root, width=800, height=600, bg="grey")
canvas.pack()

# Bind left click (Button-1) and right click (Button-3) to the click function
canvas.bind("<Button-1>", click)
canvas.bind("<Button-3>", click)

# Start the Tkinter event loop
root.mainloop()

