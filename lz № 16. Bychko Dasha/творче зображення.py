from tkinter import *

root = Tk()
canvas = Canvas(root, width=600, height=500, bg="lightblue")
canvas.pack()

# Тіло корови (еліпс)
canvas.create_oval(150, 180, 450, 300, fill="white", outline="black", width=2)

# Голова (еліпс)
canvas.create_oval(80, 190, 180, 270, fill="white", outline="black", width=2)

# Роги(трикутники)
canvas.create_polygon(90, 190, 85, 165, 95, 180, fill="gray", outline="black")
canvas.create_polygon(170, 190, 175, 165, 165, 180, fill="gray", outline="black")

# Вуха(еліпс)
canvas.create_oval(75, 210, 90, 240, fill="white", outline="black", width=2)
canvas.create_oval(170, 210, 185, 240, fill="white", outline="black", width=2)

# Очі(коло)
canvas.create_oval(105, 215, 115, 225, fill="black")
canvas.create_oval(145, 215, 155, 225, fill="black")

# Ніс
canvas.create_oval(110, 245, 150, 265, fill="pink", outline="black", width=2)
canvas.create_oval(120, 250, 125, 255, fill="black")
canvas.create_oval(135, 250, 140, 255, fill="black")

# Ноги (знизу тіла)
canvas.create_rectangle(180, 300, 200, 370, fill="white", outline="black", width=2)
canvas.create_rectangle(240, 300, 260, 370, fill="white", outline="black", width=2)
canvas.create_rectangle(310, 300, 330, 370, fill="white", outline="black", width=2)
canvas.create_rectangle(380, 300, 400, 370, fill="white", outline="black", width=2)

# Копита
canvas.create_rectangle(180, 365, 200, 375, fill="black")
canvas.create_rectangle(240, 365, 260, 375, fill="black")
canvas.create_rectangle(310, 365, 330, 375, fill="black")
canvas.create_rectangle(380, 365, 400, 375, fill="black")

# Хвіст
canvas.create_line(440, 240, 480, 280, fill="black", width=4)
canvas.create_oval(475, 275, 485, 285, fill="black")

# Плями на тілі
canvas.create_oval(220, 200, 250, 230, fill="black")
canvas.create_oval(320, 230, 360, 260, fill="black")
canvas.create_oval(270, 190, 295, 215, fill="black")

root.mainloop()

