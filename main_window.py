from PySide6.QtWidgets import QMainWindow
import matplotlib.pyplot as plt
from PySide6.QtCore import QSize
from menu.menu_bar import MenuBar

class MainWindow (QMainWindow):
  def __init__ (self, fig, ani, settings_container):
    super().__init__()

    self.fig = fig
    self.ani = ani

    self.setWindowTitle('fourier-plotter')
    self.setBaseSize(QSize(1000, 600))
    self.resize(QSize(1000, 600))
    self.setMenuBar(MenuBar(settings_container))
    self.closeEvent = self.handle_close

  def handle_close (self, event):
    self.ani.event_source.stop()
    self.fig.clf()
    plt.close(self.fig)
    event.accept()
