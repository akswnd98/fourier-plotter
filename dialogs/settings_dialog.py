from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QWidget, QPushButton
from PySide6.QtGui import QIntValidator

class SettingsDialog (QDialog):
  def __init__ (self, settings_container):
    super().__init__()
    self.resize(QSize(1000, 600))
    self.setWindowTitle('settings')
    self.closeEvent = self.handle_close
    self.setLayout(MainLayout(settings_container))
    self.settings_container = settings_container
  
  def handle_close (self):
    pass

class MainLayout (QVBoxLayout):
  def __init__ (self, settings_container):
    super().__init__()
    self.port_input = PortInput()
    self.addWidget(self.port_input)
    self.sample_num_input = SampleNumInput()
    self.addWidget(self.sample_num_input)
    self.sampling_freq_input = SamplingFreqInput()
    self.addWidget(self.sampling_freq_input)
    self.compressness_input = CompressnessInput()
    self.addWidget(self.compressness_input)
    self.interval_input = IntervalInput()
    self.addWidget(self.interval_input)
    self.run_button = RunButton(
      settings_container, self.port_input, self.sample_num_input, self.sampling_freq_input,
      self.compressness_input, self.interval_input
    )
    self.addWidget(self.run_button)

class ValueInput (QWidget):
  def __init__ (self, label, validator):
    super().__init__()
    layout = QHBoxLayout()
    self.setLayout(layout)
    layout.addWidget(QLabel(label))
    self.line_edit = QLineEdit(validator=validator)
    layout.addWidget(self.line_edit)
  
  def get_value (self):
    return self.line_edit.text

class TextInput(ValueInput):
  def __init__ (self, label):
    super().__init__(label, None)

class NumberInput (ValueInput):
  def __init__ (self, label, range):
    super().__init__(label, validator=QIntValidator(*range))

class PortInput (TextInput):
  def __init__ (self):
    super().__init__('port')

class SampleNumInput (NumberInput):
  def __init__ (self):
    super().__init__('sample num', ())

class SamplingFreqInput (NumberInput):
  def __init__ (self):
    super().__init__('sampling freq', ())

class CompressnessInput (NumberInput):
  def __init__ (self):
    super().__init__('compressness', ())

class IntervalInput (NumberInput):
  def __init__ (self):
    super().__init__('interval', ())

class RunButton (QPushButton):
  def __init__ (self, settings_container, port_input, sample_num_input,
      sampling_freq_input, compressness_input, interval_input):
    super().__init__('run')
    self.settings_container = settings_container
    self.port_input = port_input
    self.sample_num_input = sample_num_input
    self.sampling_freq_input = sampling_freq_input
    self.compressness_input = compressness_input
    self.interval_input = interval_input
    self.clicked.connect(self.handle_click)
  
  def handle_click (self):
    self.settings_container.port = self.port_input.text
    self.settings_container.sample_num = self.sample_num_input.text
    self.settings_container.sampling_freq = self.sampling_freq_input.text
    self.settings_container.compressness = self.compressness_input.text
    self.settings_container.interval = self.interval_input.text
