from tkinter import ttk, PhotoImage, Tk, Label, Frame, Checkbutton
import sv_ttk
from winsound import SND_FILENAME, PlaySound

class App(Tk):
  def __init__(self):
      super().__init__()

      self.grid_columnconfigure(1, weight=1)    
      self.grid_columnconfigure(2, weight=1)
      self.grid_columnconfigure(3, weight=1)

    # configure the root window
      self.title('Tally Counter')
      self.geometry('300x300')
    
      sv_ttk.use_light_theme()
    
      self.num = 0

      self.label = Label(self, text= self.num, font = ("Segoe UI Variable Text", 50),  width= 3)
      self.label.grid(row = 1, column= 2, pady = 70)

    # button
      self.ibtn = ttk.Button(self, text= "")
      self.ibtn['command'] = self.incr
      self.ibtn.grid(row = 1, column= 3, sticky= "ew", padx = 20)

      self.dbtn = ttk.Button(self, text='')
      self.dbtn['command'] = self.decr
      self.dbtn['state'] = "disabled"
      self.dbtn.grid(row = 1, column= 1, sticky= "ew", padx = 20)

      self.frame1 = Frame(self)
      self.frame1.grid(row = 2, column= 1, columnspan= 3)

      self.sbtn = ttk.Checkbutton(self.frame1, text = "Sound", style="Toggle.TButton", width= "10")
      self.sbtn.grid(row = 2, column= 1, sticky = "e", padx = 10)
      self.sbtn['command'] = self.enablesound

      self.rbtn = ttk.Button(self.frame1, text = "Reset", width= "10")
      self.rbtn.grid(row = 2, column= 3, columnspan= 2, sticky= "w", padx= 10)
      self.rbtn['command'] = self.reset

      self.sound = 0

  def incr(self):
    if(self.num >= 0):
        self.dbtn["state"] = "enabled"
    self.num += 1
    self.label['text'] = self.num
    if(self.sound == 1):
      self.play = PlaySound('sound.wav', SND_FILENAME)

  def decr(self):
    self.num -= 1
    self.label['text'] = self.num
    if(self.num == 0): 
        self.dbtn["state"] = "disabled"
    if(self.sound == 1):
        self.play = PlaySound('sound.wav', SND_FILENAME)

  def reset(self):
    self.num = 0
    self.label['text'] = self.num

  def enablesound(self):
    if(self.sound == 1): 
      self.sound = 0
    else:
      self.sound = 1

if __name__ == "__main__":
  app = App()
  app.mainloop() 