from tkinter import ttk

class MainPageFrame(ttk.Frame):
  
  def __logout_handler__(self, on_logout):
    self.destroy()
    on_logout()
  
  def __init__(self, master, on_logout):
    super().__init__(master=master)
    self.label = ttk.Label(self, text='Main Page')
    self.logout_button = ttk.Button(self, text='logout', command=lambda: self.__logout_handler__(on_logout))
    
    self.label.pack()
    self.logout_button.pack()