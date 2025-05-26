import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=300, bg="pink")  # Збільшене полотно
canvas.pack()

canvas.create_polygon(
    100, 200,
    200, 100,
    400, 100,
    300, 200,

    fill='yellow',
    outline='black'
)

root.mainloop()