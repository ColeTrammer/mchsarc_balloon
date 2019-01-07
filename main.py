from sense_hat import SenseHat
import time

sense = SenseHat()
f = open("data.csv", "w")
f.write("Temperature,Humidity,Pressure,Pitch,Roll,Yaw,Acceleration X,Acceleration Y,Acceleration X")

def write_data():
