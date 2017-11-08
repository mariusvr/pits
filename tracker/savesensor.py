import sensor

while True:
    ozone = sensor.getOzone()
    (humidity, pressure, temperature) = sensor.getTemp()
    (visible,ir,uv) = sensor.getLight()
    
    sensorFile = open('sensordata', 'w')
    sensorFile.write(humidity + "," + pressure + "," + temperature + "," + visible + "," + ir + "," + uv + "," + ozone)
    sensorFile.close()
    print(humidity + "," + pressure + "," + temperature + "," + visible + "," + ir + "," + uv + "," + ozone)    

