import tkinter
from tkinter import ttk
import tkinter.messagebox

from ..client import Client

class LoginFrame(tkinter.Frame):
  
  def __verify__(self):
    res = self.client.verify(self.username_entry.get(), self.password_entry.get())
    return res
  
  def __login_handler__(self, on_success, on_failure):
    res = self.__verify__()
    if res and on_success:
      on_success()
    if not res and on_failure:
      on_failure()
      
    
  def __init__(self, master, client:Client, on_success, on_failure):
    
    super().__init__(master=master)
    
    self.client = client
    
    self.username_label = ttk.Label(self, text='Username: ')
    self.username_entry = ttk.Entry(self)
    self.password_label = ttk.Label(self, text='Password: ')
    self.password_entry = ttk.Entry(self)
    
    login_button = ttk.Button(self, text='login', command= lambda : self.__login_handler__(on_success, on_failure))
    self.username_label.grid(row=0, column=0)
    self.username_entry.grid(row=0, column=1)
    self.password_label.grid(row=1, column=0)
    self.password_entry.grid(row=1, column=1)
    login_button.grid(row=2, columnspan=2)
    