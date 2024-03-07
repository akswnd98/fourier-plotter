import matplotlib.animation as animation
import numpy as np
from settings_container import SettingsContainer
from data_container import DataContainer

class PlotAnimation (animation.FuncAnimation):
  def __init__ (self, fig, time_domain_ax, freq_domain_ax):
    self.time_domain_ax = time_domain_ax
    self.freq_domain_ax = freq_domain_ax
    super().__init__(fig, self.update, frames=None, interval=SettingsContainer.interval, blit=False, cache_frame_data=False)

  def update (self, frame):    
    self.time_domain_ax.cla()
    self.freq_domain_ax.cla()

    self.time_domain_ax.autoscale(False)
    self.time_domain_ax.set_axis_on()
    self.time_domain_ax.axis([0, SettingsContainer.sample_num / SettingsContainer.sampling_freq, -5000, 5000])
    self.time_domain_ax.set_xlabel('time (s)')
    self.time_domain_ax.set_ylabel('signal')

    self.freq_domain_ax.autoscale(False)
    self.freq_domain_ax.set_axis_on()
    self.freq_domain_ax.axis([-SettingsContainer.sampling_freq / 2, SettingsContainer.sampling_freq / 2, -1, 10000])
    self.freq_domain_ax.set_xlabel('frequency (Hz)')
    self.freq_domain_ax.set_ylabel('fft')

    ret = []
    if len(DataContainer.data) >= SettingsContainer.sample_num:
      time_domain_xs = np.arange(0, len(DataContainer.data), 1, dtype=np.float32) / SettingsContainer.sampling_freq
      self.time_domain_ax.plot(time_domain_xs, DataContainer.data)

      fft_data = np.fft.fft(DataContainer.data)
      freq_domain_xs = np.fft.fftfreq(SettingsContainer.sample_num)[0: SettingsContainer.sample_num // SettingsContainer.compressness * SettingsContainer.compressness][0: : SettingsContainer.compressness] * SettingsContainer.sampling_freq
      fft_data_compressed = np.zeros_like(freq_domain_xs)
      for i in range(SettingsContainer.compressness):
        fft_data_compressed += np.abs(fft_data)[0: SettingsContainer.sample_num // SettingsContainer.compressness * SettingsContainer.compressness][i: : SettingsContainer.compressness]
      fft_data_compressed /= SettingsContainer.compressness

      self.freq_domain_ax.bar(freq_domain_xs, fft_data_compressed)
      return []

    return ret
