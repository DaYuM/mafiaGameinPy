import Tkinter

hi = Tkinter.Tk()
hi.title("1+2")

#functions
def hide_all():
  pass

#gui

output1 = Tkinter.Label(hi, text = "help")
output1.pack()

input1 = Tkinter.Entry(hi)
input1.pack()


btn_show_all = Tkinter.Button(hi, text="Hide All", command = hide_all)
btn_show_all.pack()

hi.mainloop()
