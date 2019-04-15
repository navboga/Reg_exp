from tkinter import * #colorchooser, Tk, Canvas, Button
def calc(event):
    print(3+2,"могло быть и хуже")

window=Tk()
#colorchooser.askcolor()
canvas=Canvas(window, width=400, height=400, bg='green')
start_pik=[50,0]
end_pik=[50,400]
canvas.pack()
for i in range(7):
  canvas.create_line(start_pik[0],start_pik[1],end_pik[0],end_pik[1],width=2,fill="yellow")
  start_pik[0]+=50
  end_pik[0] += 50
#canvas.create_line(150,0,150,400,width=2,fill="yellow")
#canvas.create_line(200,0,200,400,width=2,fill="yellow")
enty=Entry(window, width=20, bd=3, bg="blue",font="Arial")
but=Button(window)
but['text']="Печать"
but.bind("<Button-1>",calc)


but.pack(side="bottom")
enty.pack(side="top")
window.mainloop()