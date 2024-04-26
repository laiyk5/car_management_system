from app.gui import GUI
from .pseudo_client import PseudoClient

client = PseudoClient()
gui = GUI(client)
gui.mainloop()