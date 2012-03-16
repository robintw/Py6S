class Altitudes:
  """Allows the specification of target and sensor altitudes."""
  
  def __init__(self):
    self.target_alt_pres = None
    self.sensor_alt_pres = None
    self.sensor_altitude = None
    self.aot = None
    self.water = None
    self.ozone = None
  
  def set_target_sea_level(self):
    """Set the altitude of the target to be at sea level (0km)"""
    
    self.target_alt_pres = 0
  
  def set_target_custom_altitude(self, altitude):
    """Set the altitude of the target.
    
    Arguments:
     * `altitude` -- The altitude of the target, in km
    
    """
    
    self.target_alt_pres = -1 * altitude
    
  def set_target_pressure(self, pressure):
    """Set the pressure of the target (a proxy for the height of the target).
    
    Arguments:
     * `pressure` -- The pressure at the target, in mb`
    
    """
    
    self.target_alt_pres = pressure
  
  def set_sensor_sea_level(self):
    """Set the sensor altitude to be sea level."""
    
    self.sensor_alt_pres = 0
    
  def set_sensor_satellite_level(self):
    """Set the sensor altitude to be satellite level."""
    self.sensor_alt_pres = -1000
    
  def set_sensor_custom_altitude(self, altitude, aot, water=-1, ozone=-1):
    """Set the altitude of the sensor, along with other variables required for the parameterisation of the sensor.
    
    Arguments:
     * `altitude` -- The altitude of the sensor, in km.
     * `aot` -- The AOT at 550nm at the sensor
     * `water` -- (Optional, keyword argument) The water vapour content (in g/cm^2) at the sensor
     * `ozone` -- (Optional, keyword argument) The ozone content (in cm-atm) at the sensor
    
    Example usage::
    
      s.altitudes = Altitudes()
      s.altitudes.set_sensor_altitude(8, 0.35, 1.6, 0.4) # Altitude of 8km, AOT of 0.35, Water content of 1.6g/cm^2 and Ozone of 0.4cm-atm
    
    """
    
    self.sensor_altitude = altitude
    self.aot = aot
    self.water = water
    self.ozone = ozone
    
  
  def __str__(self):
    if self.sensor_altitude == None:
      return "%f\n%f\n" % (self.target_alt_pres, self.sensor_alt_pres)
    else:
      return "%f\n%f %f\n%f\n" % (self.target_alt_press, self.sensor_altitude, self.water, self.ozone, self.aot)