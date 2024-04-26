import tkinter
from tkinter import ttk
import tkinter.messagebox

from ..client import Client
from .login_frame import LoginFrame
from .main_page_frame import MainPageFrame

class BodyFrame(ttk.Frame):
  def __on_login_success__(self):
    self.login_frame.destroy()
    self.main_page_frame = MainPageFrame(self, on_logout=self.__on_logout__)
    self.main_page_frame.pack()
    
  def __on_login_failure__(self):
    tkinter.messagebox.showerror(message='Userid does not exist or password missmatched.')
    return
  
  def __on_logout__(self):
    self.__enter_login_frame__()
  
  def __enter_login_frame__(self):
    self.login_frame = LoginFrame(self, self.client, self.__on_login_success__, self.__on_login_failure__)
    self.login_frame.pack()
  
  def __init__(self, master, client:Client):
    super().__init__(master=master)
    
    self.client = client
    
    self.__enter_login_frame__()