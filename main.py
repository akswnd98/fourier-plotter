import sys
from PySide6.QtCore import QSize, QTimer
from PySide6.QtWidgets import QVBoxLayout, QDialog, QApplication
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.animation as animation
import numpy as np
from matplotlib.ticker import AutoLocator, ScalarFormatter
from main_window import MainWindow
from data_receive_thread import DataReceiveThread
from data_container import DataContainer
from plot_animation import PlotAnimation

sample_num = 1000
sampling_freq = 200
data_container = DataContainer()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  thread = DataReceiveThread(data_container, sample_num)
  thread.start()

  fig = plt.figure()
  time_domain_ax = fig.add_subplot(2, 1, 1)
  freq_domain_ax = fig.add_subplot(2, 1, 2)

  ani = PlotAnimation(fig, data_container, time_domain_ax, freq_domain_ax, sample_num, sampling_freq)
  window = MainWindow(fig, ani)
  canvas = FigureCanvas(fig)
  window.setCentralWidget(canvas)

  window.show()
  app.exec()
