import tkinter
import tkinter.messagebox
from .body_frame import BodyFrame

from ..client import Client

def askyesno(message, yes_command=None, no_command=None):
  res = tkinter.messagebox.askyesno(message=message)
  if res and yes_command:
    return yes_command()
  if not res and no_command:
    return no_command()


class GUI(tkinter.Tk):
  def __init__(self, client:Client):
    super().__init__()
    
    self.client = client
    
    self.title('CMS')
    self.geometry('800x400')

    body = BodyFrame(self, client)

    body.pack(expand=1)

    menubar = tkinter.Menu(self)
    menubar.add_command(label='quit', command=lambda: askyesno('Do you really want to quit?', self.quit))
    self.config(menu=menubar)

