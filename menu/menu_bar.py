from PySide6.QtWidgets import QMenuBar
from menu.settings_menu import SettingsMenu

class MenuBar (QMenuBar):
  def __init__ (self, settings_container):
    super().__init__()
    self.settings_container = settings_container
    self.addMenu(SettingsMenu(settings_container))
