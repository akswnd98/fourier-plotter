import serial
import threading
from settings_container import SettingsContainer
from data_container import DataContainer
from data_transformer.little_endian_short_transformer import LittleEndianShortTransformer
from serial_container import SerialContainer

class DataReceiveThread:
  def __init__ (self):
    self.data_transformer = LittleEndianShortTransformer()

  def receive_continuousely (self):
    while True:
      raw_data = SerialContainer.ser.read(2)
      new_data = self.data_transformer.transform(raw_data)
      if len(DataContainer.data) >= SettingsContainer.sample_num:
        DataContainer.data = DataContainer.data[1: ] + [new_data]
      else:
        DataContainer.data += [new_data]

  def start (self):
    if SerialContainer.ser != None:
      SerialContainer.ser.close()
    SerialContainer.ser = serial.Serial(SettingsContainer.port, SettingsContainer.baudrate, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
    DataContainer.data = [0.0] * SettingsContainer.sample_num
    thread = threading.Thread(target=self.receive_continuousely, daemon=True)
    thread.start()
