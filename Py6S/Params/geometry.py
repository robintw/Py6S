class GeometryUser:
  solar_z = 0
  solar_a = 0
  view_z = 0
  view_a = 0
  day = 1
  month = 1
  
  def __str__(self):
    return '0 (User defined)\n%d %d %d %d %d %d\n' % (self.solar_z, self.solar_a, self.view_z, self.view_a, self.month, self.day)
    
  
  
class GeometryMeteosat:
  month = 1
  day = 1
  gmt_decimal_hour = 0
  column = 0
  line = 0
  
  def __str__(self):
    return '1 (Meteosat)\n%d %d %d %d %d (Geometrical Conditions)' % (self.month, self.day, self.gmt_decimal_hour, self.column, self.line)
    
class GeometryGoesEast:
  month = 1
  day = 1
  gmt_decimal_hour = 0
  column = 0
  line = 0
  
  def __str__(self):
    return '2 (Goes East)\n%d %d %d %d %d (Geometrical Conditions)' % (self.month, self.day, self.gmt_decimal_hour, self.column, self.line)
    
    
class GeometryGoesWest:
  month = 1
  day = 1
  gmt_decimal_hour = 0
  column = 0
  line = 0
  
  def __str__(self):
    return '3 (Goes West)\n%d %d %d %d %d (Geometrical Conditions)' % (self.month, self.day, self.gmt_decimal_hour, self.column, self.line)
    
class GeometryAVHRR_PM:
  month = 1
  day = 1
  gmt_decimal_hour = 0
  column = 0
  ascendant_node_longitude = 0
  ascendant_node_hour = 0
  
  def __str__(self):
    return '4 (AVHRR PM NOAA)\n%d %d %d %d %d (Geometrical Conditions)' % (self.month, self.day, self.gmt_decimal_hour, self.column, self.ascendant_node_longitude, self.ascendant_node_hour)
    
class GeometryAVHRR_AM:
  month = 1
  day = 1
  gmt_decimal_hour = 0
  column = 0
  ascendant_node_longitude = 0
  ascendant_node_hour = 0
  
  def __str__(self):
    return '5 (AVHRR AM NOAA)\n%d %d %d %d %d (Geometrical Conditions)' % (self.month, self.day, self.gmt_decimal_hour, self.column, self.ascendant_node_longitude, self.ascendant_node_hour)
    
class GeometrySPOT_HRV:
  month = 1
  day = 1
  gmt_decimal_hour = 0
  longitude = 0
  latitude = 0
  
  def __str__(self):
    return '6 (SPOT)\n%d %d %d %d %d (Geometrical Conditions)' % (self.month, self.day, self.gmt_decimal_hour, self.longitude, self.latitude)
    
class GeometryLandsat_TM:
  month = 1
  day = 1
  gmt_decimal_hour = 0
  longitude = 0
  latitude = 0
  
  def __str__(self):
    return '7 (TM)\n%d %d %d %d %d (Geometrical Conditions)' % (self.month, self.day, self.gmt_decimal_hour, self.longitude, self.latitude)