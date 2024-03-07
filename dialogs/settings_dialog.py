from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QWidget, QPushButton
from PySide6.QtGui import QIntValidator
from data_receive_thread import DataReceiveThread
from data_transformer.little_endian_short_transformer import LittleEndianShortTransformer
from settings_container import SettingsContainer
from settings_dialog_instance import SettingsDialogInstance

class SettingsDialog (QDialog):
  def __init__ (self):
    super().__init__()
    self.resize(QSize(1000, 600))
    self.setWindowTitle('settings')
    self.closeEvent = self.handle_close
    self.setLayout(MainLayout())
  
  def handle_close (self, event):
    pass

class MainLayout (QVBoxLayout):
  def __init__ (self):
    super().__init__()
    self.port_input = PortInput()
    self.addWidget(self.port_input)
    self.baudrate_input = BaudrateInput()
    self.addWidget(self.baudrate_input)
    self.sample_num_input = SampleNumInput()
    self.addWidget(self.sample_num_input)
    self.sampling_freq_input = SamplingFreqInput()
    self.addWidget(self.sampling_freq_input)
    self.compressness_input = CompressnessInput()
    self.addWidget(self.compressness_input)
    self.interval_input = IntervalInput()
    self.addWidget(self.interval_input)
    self.run_button = RunButton(
      self.port_input, self.baudrate_input, self.sample_num_input, self.sampling_freq_input,
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
    return self.line_edit.text()

class TextInput(ValueInput):
  def __init__ (self, label):
    super().__init__(label, None)

class NumberInput (ValueInput):
  def __init__ (self, label, range):
    super().__init__(label, validator=QIntValidator(*range))

class PortInput (TextInput):
  def __init__ (self):
    super().__init__('port')

class BaudrateInput (NumberInput):
  def __init__ (self):
    super().__init__('baudrate', ())

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
  def __init__ (self, port_input, baudrate_input, sample_num_input, sampling_freq_input, compressness_input, interval_input):
    super().__init__('run')
    self.port_input = port_input
    self.baudrate_input = baudrate_input
    self.sample_num_input = sample_num_input
    self.sampling_freq_input = sampling_freq_input
    self.compressness_input = compressness_input
    self.interval_input = interval_input
    self.clicked.connect(self.handle_click)
  
  def handle_click (self):
    SettingsContainer.port = self.port_input.get_value()
    SettingsContainer.baudrate = int(self.baudrate_input.get_value())
    SettingsContainer.sample_num = int(self.sample_num_input.get_value())
    SettingsContainer.sampling_freq = int(self.sampling_freq_input.get_value())
    SettingsContainer.compressness = int(self.compressness_input.get_value())
    SettingsContainer.interval = int(self.interval_input.get_value())
    SettingsDialogInstance.instance.close()
    thread = DataReceiveThread()
    thread.start()
