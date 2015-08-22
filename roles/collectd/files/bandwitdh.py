import collectd

class Interface(object):
  def __init__(self):
    self.rx = Traffic('rx')
    self.tx = Traffic('tx')


class Traffic(object):
  def __init__(self,direction):
    self.octets = Measurepoint(direction,'octets')
    self.packets = Measurepoint(direction,'packets')


class Measurepoint(object):
  def __init__(self,direction,unit):
    self.unit = unit
    self.direction = direction
    if self.unit == "octets":
      self.unit = "bytes"
    self.file_handle = open("/sys/class/net/{0}/statistics/{1}_{2}".format(self.direction,self.unit))
    collectd.register_read(self.get)
    self.bandwidth = Bandwith(data)
  def get(self):
    measurement = Measurement(self.unit,int(self.file_handle.read()))
    bandwidth = self.bandwith.calculate(measurement)
    value = collectd.Values(type='gauge')
    value.plugin='bandwidth.'.data.interface
    value.dispatch(bandwidth)
    


class Measurement(object):
  def __init__(self,unit,value):
    self.unit = unit
    self.value = value


class Bandwidth(object):
  def __init__(self,data):
    self.last_measurement = None
    self.interval = data.interval
  def calculate(measurement):
    self.last_measurement = measurement
    difference = measurement.value - self.last_measurement.value
    return (difference / self.interval)
