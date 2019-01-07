from sense_hat import SenseHat
import time

sense = SenseHat()
f = open("data.csv", "w")
f.write("Temperature,Humidity,Pressure,Pitch,Roll,Yaw,Acceleration X,Acceleration Y,Acceleration X")

def write_data():
  f.write(f"{sense.get_temperature()},{sense.get_humidity},{sense.get_pressure()},{sense.get_orientation()["pitch"]},{sense.get_orientation()["roll"]},{sense.get_orientation()["yaw"]},{sense.get_acceleromter_raw()["x"]},{sense.get_acceleromter_raw()["y"]},{sense.get_acceleromter_raw()["z"]}")
