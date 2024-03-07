from PySide6.QtWidgets import QMenuBar
from menu.settings_menu import SettingsMenu

class MenuBar (QMenuBar):
  def __init__ (self):
    super().__init__()
    self.addMenu(SettingsMenu())
