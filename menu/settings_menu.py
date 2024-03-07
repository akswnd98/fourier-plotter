from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QAction
from dialogs.settings_dialog import SettingsDialog
from settings_dialog_instance import SettingsDialogInstance

class SettingsMenu (QMenu):
  def __init__ (self):
    super().__init__('settings')
    action = QAction('settings', self)
    action.triggered.connect(self.handle_settings_triggered)
    self.addAction(action)
  
  def handle_settings_triggered (self):
    dialog = SettingsDialog()
    SettingsDialogInstance.instance = dialog
    dialog.exec()
