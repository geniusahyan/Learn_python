# create tkinter
# from tkinter import *
# #create a window
# window = Tk()
# #set the title of the window
# window.title("My First Window")
# #set the size of the window
# window.geometry('400x200')
# #create label widget in the window
# label1=Label(window,text="Hello World!",bg='red',fg='white')
# #pack the label to the center of the window
# label1.pack(pady=5)
# #start the main loop for the application
# window.mainloop()


from tkinter import *

def prank():
    win = Tk()
    win.title('My window')
    win.geometry('400x200')
    win.configure(bg='cyan')
    label1 = Button(win,text='button', bg='orange')
    label1.place(x=20,y=20)

    win.mainloop()
prank()