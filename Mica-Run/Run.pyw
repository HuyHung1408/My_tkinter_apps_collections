from tkinter import Tk, Label, PhotoImage, filedialog, ttk, messagebox
from ctypes import windll
import tkinter
import os
import sv_ttk

class App(Tk):
  def __init__(self):
      super().__init__()

      self.title("File runner")
      self.geometry('380x190')
      self.iconbitmap("Run.ico")
      sv_ttk.set_theme('light')

      self.input = ttk.Combobox()
      self.input.place(x=60, y=79, width=295)
      self.input.focus_set()

      
      self.Ok = ttk.Button(self, text='OK')
      self.Ok.place(x = 95, y = 143, width = 80)
      self.Ok['command'] = self.okbutton
      self.Ok.bind('<Return>', self.okbutton)

      self.Cancel = ttk.Button(self, text='Cancel', command=self.destroy).place(x = 185, y = 143, width = 80)
      self.Browse = ttk.Button(self, text='Browse...', command= self.browsefunc).place(x = 275, y = 143, width = 80)

      self.opentext = ttk.Label(text='Open:').place(x=13, y=85)

      self.img = PhotoImage(file='Run.png')
      self.Runicon = Label(self, image=self.img).place(x=10, y=18)
      self.text = ttk.Label(text='Type the name of a program, folder, document, or\nInternet resource, and Windows will open it for you.', font=('Segoe UI Variable Display','10')).place(x=60, y=20)

  def browsefunc(self):
    self.filename = filedialog.askopenfilename(filetypes=(("Programs","*.exe"),("All files","*.*")))
    input.set("")
    input.insert(tk.END, filename)
    
  def okbutton(self):
    try:
      self.os.startfile(input.get())
      self.destroy()
    except:
      self.messagebox.showerror(input.get(), 'Make sure you typed the name correctly, and then try again.')

if __name__ == "__main__":
  app = App()
  app.mainloop() 