import pigpio
# Connect to the pigpio daemon
pi = pigpio.pi()

# Set up the sensor pin
humiTempSensor = 17
pi.set_mode(humiTempSensor, pigpio.INPUT)

# Read data from the sensor
sensor_data = pi.read(humiTempSensor)

# Print the sensor data
print("Sensor data:", sensor_data)

# Disconnect from the pigpio daemon
pi.stop()
