import matplotlib.animation as animation
import numpy as np

class PlotAnimation (animation.FuncAnimation):
  def __init__ (self, fig, data_container, time_domain_ax, freq_domain_ax, sample_num, sampling_freq, compressness, interval):
    self.data_container = data_container
    self.time_domain_ax = time_domain_ax
    self.freq_domain_ax = freq_domain_ax
    self.sample_num = sample_num
    self.sampling_freq = sampling_freq
    self.compressness = compressness
    super().__init__(fig, self.update, frames=None, interval=interval, blit=False, cache_frame_data=False)

  def update (self, frame):    
    self.time_domain_ax.cla()
    self.freq_domain_ax.cla()

    self.time_domain_ax.autoscale(False)
    self.time_domain_ax.set_axis_on()
    self.time_domain_ax.axis([0, self.sample_num / self.sampling_freq, -5000, 5000])
    self.time_domain_ax.set_xlabel('time (s)')
    self.time_domain_ax.set_ylabel('signal')

    self.freq_domain_ax.autoscale(False)
    self.freq_domain_ax.set_axis_on()
    self.freq_domain_ax.axis([-self.sampling_freq / 2, self.sampling_freq / 2, -1, 10000])
    self.freq_domain_ax.set_xlabel('frequency (Hz)')
    self.freq_domain_ax.set_ylabel('fft')

    ret = []
    if len(self.data_container.data) >= self.sample_num:
      time_domain_xs = np.arange(0, len(self.data_container.data), 1, dtype=np.float32) / self.sampling_freq
      self.time_domain_ax.plot(time_domain_xs, self.data_container.data)

      fft_data = np.fft.fft(self.data_container.data)
      freq_domain_xs = np.fft.fftfreq(self.sample_num)[0: self.sample_num // self.compressness * self.compressness][0: : self.compressness] * self.sampling_freq
      fft_data_compressed = np.zeros_like(freq_domain_xs)
      for i in range(self.compressness):
        fft_data_compressed += np.abs(fft_data)[0: self.sample_num // self.compressness * self.compressness][i: : self.compressness]
      fft_data_compressed /= self.compressness

      self.freq_domain_ax.bar(freq_domain_xs, fft_data_compressed)
      return []

    return ret
