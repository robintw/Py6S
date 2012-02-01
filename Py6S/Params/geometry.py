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