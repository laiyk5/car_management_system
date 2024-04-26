from typing import Protocol

class Client(Protocol):
  def verify(self, username:str, password:str)->bool:
    ...
  