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

if __name__ == '__main__':
  app = QApplication(sys.argv)

  fig = plt.figure()
  time_domain_ax = fig.add_subplot(2, 1, 1)
  freq_domain_ax = fig.add_subplot(2, 1, 2)

  ani = PlotAnimation(fig, time_domain_ax, freq_domain_ax)
  window = MainWindow(fig, ani)
  canvas = FigureCanvas(fig)
  window.setCentralWidget(canvas)

  window.show()
  app.exec()
