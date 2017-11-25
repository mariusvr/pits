import sensor
import time

while True:
    ozone = sensor.getOzone()
    (humidity, pressure, temperature) = sensor.getTemp()
    (visible,ir,uv) = sensor.getLight()

    line = "%s,%s,%s,%s,%s,%s,%s" % (humidity,pressure,temperature,visible,ir,uv,ozone)
    
    print (line)

    with open("sensordata", "a") as myfile:
        myfile.write(line + '\n')
    time.sleep(15)
