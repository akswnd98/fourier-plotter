import numpy as np
from PySide6.QtCore import QSize, Qt, QTimer
from PySide6.QtWidgets import (
  QApplication, QMainWindow, QWidget,
  QVBoxLayout, QHBoxLayout, QMenuBar, QMenu
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.figure import Figure

class MainWindow (QMainWindow):
  def __init__ (self, fig, ani):
    super().__init__()

    self.fig = fig
    self.ani = ani

    self.setWindowTitle('fourier-plotter')
    self.setBaseSize(QSize(800, 400))
    self.resize(QSize(1000, 600))
    self.setMenuBar(MenuBar())
    self.closeEvent = self.handle_close
  
  def handle_close (self, event):
    self.ani.event_source.stop()
    self.fig.clf()
    plt.close(self.fig)
    event.accept()

class MenuBar (QMenuBar):
  def __init__ (self):
    super().__init__()
