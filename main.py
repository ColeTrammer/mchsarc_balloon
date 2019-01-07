from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_imu_config(False, True, True)
file = open("data.csv", "w")
file.write("Temperature,Humidity,Pressure,Pitch,Roll,Yaw,Acceleration X,Acceleration Y,Acceleration X\n")

def write_data():
    file.write("%f,%f,%f,%f,%f,%f,%f,%f,%f\n" % sense.get_temperature(), sense.get_humidity, sense.get_pressure(), sense.get_orientation()["pitch"], sense.get_orientation()["roll"], sense.get_orientation()["yaw"], sense.get_acceleromter_raw()["x"], sense.get_acceleromter_raw()["y"], sense.get_acceleromter_raw()["z"])

start_time = time.time()
interval = 3.0 # seconds
for i in range(0,100000):
    write_data()
    time.sleep(interval - ((time.time() - start_time) % interval)

