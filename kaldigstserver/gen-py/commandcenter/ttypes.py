#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class MachineData:
  """
  Attributes:
   - name
   - port
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.I32, 'port', None, None, ), # 2
  )

  def __init__(self, name=None, port=None,):
    self.name = name
    self.port = port

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.name = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.port = iprot.readI32()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('MachineData')
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 1)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.port is not None:
      oprot.writeFieldBegin('port', TType.I32, 2)
      oprot.writeI32(self.port)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.port)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class QueryData:
  """
  Attributes:
   - audioData
   - audioFormat
   - audioB64Encoding
   - imgData
   - imgFormat
   - imgB64Encoding
   - textData
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'audioData', None, "", ), # 1
    (2, TType.STRING, 'audioFormat', None, "", ), # 2
    (3, TType.BOOL, 'audioB64Encoding', None, False, ), # 3
    (4, TType.STRING, 'imgData', None, "", ), # 4
    (5, TType.STRING, 'imgFormat', None, "", ), # 5
    (6, TType.BOOL, 'imgB64Encoding', None, False, ), # 6
    (7, TType.STRING, 'textData', None, "", ), # 7
  )

  def __init__(self, audioData=thrift_spec[1][4], audioFormat=thrift_spec[2][4], audioB64Encoding=thrift_spec[3][4], imgData=thrift_spec[4][4], imgFormat=thrift_spec[5][4], imgB64Encoding=thrift_spec[6][4], textData=thrift_spec[7][4],):
    self.audioData = audioData
    self.audioFormat = audioFormat
    self.audioB64Encoding = audioB64Encoding
    self.imgData = imgData
    self.imgFormat = imgFormat
    self.imgB64Encoding = imgB64Encoding
    self.textData = textData

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.audioData = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.audioFormat = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.BOOL:
          self.audioB64Encoding = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.imgData = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.imgFormat = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.BOOL:
          self.imgB64Encoding = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.textData = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('QueryData')
    if self.audioData is not None:
      oprot.writeFieldBegin('audioData', TType.STRING, 1)
      oprot.writeString(self.audioData)
      oprot.writeFieldEnd()
    if self.audioFormat is not None:
      oprot.writeFieldBegin('audioFormat', TType.STRING, 2)
      oprot.writeString(self.audioFormat)
      oprot.writeFieldEnd()
    if self.audioB64Encoding is not None:
      oprot.writeFieldBegin('audioB64Encoding', TType.BOOL, 3)
      oprot.writeBool(self.audioB64Encoding)
      oprot.writeFieldEnd()
    if self.imgData is not None:
      oprot.writeFieldBegin('imgData', TType.STRING, 4)
      oprot.writeString(self.imgData)
      oprot.writeFieldEnd()
    if self.imgFormat is not None:
      oprot.writeFieldBegin('imgFormat', TType.STRING, 5)
      oprot.writeString(self.imgFormat)
      oprot.writeFieldEnd()
    if self.imgB64Encoding is not None:
      oprot.writeFieldBegin('imgB64Encoding', TType.BOOL, 6)
      oprot.writeBool(self.imgB64Encoding)
      oprot.writeFieldEnd()
    if self.textData is not None:
      oprot.writeFieldBegin('textData', TType.STRING, 7)
      oprot.writeString(self.textData)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.audioData)
    value = (value * 31) ^ hash(self.audioFormat)
    value = (value * 31) ^ hash(self.audioB64Encoding)
    value = (value * 31) ^ hash(self.imgData)
    value = (value * 31) ^ hash(self.imgFormat)
    value = (value * 31) ^ hash(self.imgB64Encoding)
    value = (value * 31) ^ hash(self.textData)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
