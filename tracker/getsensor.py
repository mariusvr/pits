import sensor
import urllib2

ozone = sensor.getOzone()
(humidity, pressure, temperature) = sensor.getTemp()
(visible,ir,uv) = sensor.getLight()

print "Humidity is : %.0f %%" %humidity
print "Pressure is : %.0f mbar" %pressure
print "Temperature is : %.1f C" %temperature
print "Visible light is : %.0f lux" %visible
print "IR light is : %.0f lux" %ir
print "UV light is : %.0f lux" %uv
print "Ozone concentration is : %.0f ppm" %ozone

baseURL = "https://api.thingspeak.com/update?api_key=KA8898GKT8TYZUYQ"
baseURL += "&field1=" + str(round(temperature,1))
baseURL += "&field2=" + str(round(humidity,0))
baseURL += "&field3=" + str(round(pressure,0))
baseURL += "&field4=" + str(round(ozone,0))
baseURL += "&field5=" + str(round(uv,0))
baseURL += "&field6=" + str(round(visible,0))
baseURL += "&field7=" + str(round(ir,0))
urllib2.urlopen(baseURL).read()







