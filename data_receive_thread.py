import serial
import threading
import struct

class DataReceiveThread:
  def __init__ (self, data_container, sample_num):
    self.data_container = data_container
    self.sample_num = sample_num
    self.ser = serial.Serial('COM4', 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
  
  def receive_continuousely (self):
    while True:
      raw_data = self.ser.read(2)
      new_data,  = struct.unpack('<h', raw_data)
      if len(self.data_container.data) >= self.sample_num:
        self.data_container.data = self.data_container.data[1: ] + [new_data]
      else:
        self.data_container.data += [new_data]

  def start (self):
    thread = threading.Thread(target=self.receive_continuousely, daemon=True)
    thread.start()
