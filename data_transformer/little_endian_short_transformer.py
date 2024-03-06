from data_transformer.data_transformer import DataTransformer
import struct

class LittleEndianShortTransformer (DataTransformer):
  def transform (self, bytes):
    ret,  = struct.unpack('<h', bytes)
    return ret
