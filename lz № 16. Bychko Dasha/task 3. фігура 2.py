import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=500, bg="lightblue")  # Збільшене полотно
canvas.pack()

canvas.create_polygon(
    400, 40,    # вершина вгорі
    194, 262,    # нижня ліва
    632, 262,   # нижня права
    fill='pink',
    outline='black'
)

root.mainloop()


