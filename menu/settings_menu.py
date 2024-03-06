from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QAction
from dialogs.settings_dialog import SettingsDialog

class SettingsMenu (QMenu):
  def __init__ (self, settings_container):
    super().__init__('settings')
    self.settings_container = settings_container
    action = QAction('settings', self)
    action.triggered.connect(self.handle_settings_triggered)
    self.addAction(action)
  
  def handle_settings_triggered (self):
    dialog = SettingsDialog(self.settings_container)
    dialog.exec()
