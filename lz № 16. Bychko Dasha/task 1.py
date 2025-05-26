from tkinter import *
import winsound

def play():
    if var.get() == 0:
        winsound.PlaySound('шрудень.wav', winsound.SND_FILENAME)
    elif var.get() == 1:
        winsound.PlaySound('січень.wav', winsound.SND_FILENAME)
    elif var.get() == 2:
        winsound.PlaySound('дютий.wav', winsound.SND_FILENAME)
    elif var.get() == 3:
        winsound.PlaySound('берез.wav', winsound.SND_FILENAME)
    elif var.get() == 4:
        winsound.PlaySound('Квітень.wav', winsound.SND_FILENAME)
    elif var.get() == 5:
        winsound.PlaySound('травень.wav', winsound.SND_FILENAME)
    elif var.get() == 6:
        winsound.PlaySound('червень.wav', winsound.SND_FILENAME)
    elif var.get() == 7:
        winsound.PlaySound('липень.wav', winsound.SND_FILENAME)
    elif var.get() == 8:
        winsound.PlaySound('серпень.wav', winsound.SND_FILENAME)
    elif var.get() == 9:
        winsound.PlaySound('вересень.wav', winsound.SND_FILENAME)
    elif var.get() == 10:
        winsound.PlaySound('жовтень.wav', winsound.SND_FILENAME)
    elif var.get() == 11:
        winsound.PlaySound('листопад.wav', winsound.SND_FILENAME)

root = Tk()
root.minsize(width=800, height=800)
root.title("Словник")
root['bg'] = 'yellow'

frame = LabelFrame(root, text='Виберіть слово', padx=50, bg="white", bd=3)
frame.pack()

var = IntVar()
var.set(0)

Radiobutton1 = Radiobutton(frame, bg="white", text="Грудень", variable=var, value=0).pack(anchor=W)
Radiobutton2 = Radiobutton(frame, bg="white", text="Січень", variable=var, value=1).pack(anchor=W)
Radiobutton3 = Radiobutton(frame, bg="white", text="Лютий", variable=var, value=2).pack(anchor=W)
Radiobutton4 = Radiobutton(frame, bg="white", text="Березень", variable=var, value=3).pack(anchor=W)
Radiobutton5 = Radiobutton(frame, bg="white", text="Квітень", variable=var, value=4).pack(anchor=W)
Radiobutton6 = Radiobutton(frame, bg="white", text="Травень", variable=var, value=5).pack(anchor=W)
Radiobutton7 = Radiobutton(frame, bg="white", text="Червень", variable=var, value=6).pack(anchor=W)
Radiobutton8 = Radiobutton(frame, bg="white", text="Липень", variable=var, value=7).pack(anchor=W)
Radiobutton9 = Radiobutton(frame, bg="white", text="Серпень", variable=var, value=8).pack(anchor=W)
Radiobutton10 = Radiobutton(frame, bg="white", text="Вересень", variable=var, value=9).pack(anchor=W)
Radiobutton11 = Radiobutton(frame, bg="white", text="Жовтень", variable=var, value=10).pack(anchor=W)
Radiobutton12 = Radiobutton(frame, bg="white", text="Листопад", variable=var, value=11).pack(anchor=W)

button = Button(text="Відтворити", width=15, height=2, bg="pink", command=play)
button.pack()

canvas = Canvas(root, width=500, height=400, bg='white')
canvas.pack()

img = PhotoImage(file='місяці 3.png')
canvas.create_image(20, 20, image=img, anchor=NW)
canvas.image = img

root.mainloop()
