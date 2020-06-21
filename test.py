from dhtsensor.sensor import Sensor

s = Sensor(pi, 4, powered_by=1)

s.activate()

reading = s.read_once()
temp, rh = s.read_once()

print("temperatura e humidade relativa") 
print(temp)
print(rh)


print("variavel reading")
print(reading)

