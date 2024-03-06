import sys
from PySide6.QtWidgets import QApplication
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from main_window import MainWindow
from data_receive_thread import DataReceiveThread
from data_container import DataContainer
from plot_animation import PlotAnimation
from data_transformer.little_endian_short_transformer import LittleEndianShortTransformer
from settings_container import SettingsContainer

sample_num = 1000
sampling_freq = 200
compressness = 10
interval = 150

settings_container = SettingsContainer(sample_num, sampling_freq, compressness, interval)
data_container = DataContainer(sample_num)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  thread = DataReceiveThread(data_container, sample_num, LittleEndianShortTransformer())
  thread.start()

  fig = plt.figure()
  time_domain_ax = fig.add_subplot(2, 1, 1)
  freq_domain_ax = fig.add_subplot(2, 1, 2)

  ani = PlotAnimation(fig, data_container, time_domain_ax, freq_domain_ax, sample_num, sampling_freq, compressness, interval)
  window = MainWindow(fig, ani, settings_container)
  canvas = FigureCanvas(fig)
  window.setCentralWidget(canvas)

  window.show()
  app.exec()
