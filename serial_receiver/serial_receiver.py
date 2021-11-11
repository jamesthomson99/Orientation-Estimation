import matplotlib.pyplot as plt
import serial
import time

serialPort = serial.Serial(port="COM4", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
serialPort.flush()

serialString = ""

plt_pitch = plt
plt_roll = plt
plt_yaw = plt

pitch_list = []
roll_list = []
yaw_list = []
time_list = []

start_time = time.time()
current_time = time.time()
while current_time - start_time < 20:

    current_time = time.time()

    if serialPort.in_waiting > 0:

        serialString = serialPort.readline()
        serialString = serialString.decode('Ascii')
        pitch_search = "pi"
        roll_search = "ro"
        yaw_search = "ya"

        pi = serialString.find(pitch_search)
        ro = serialString.find(roll_search)
        ya = serialString.find(yaw_search)
        pitch_list.append(float(serialString[pi + 3:ro]))
        roll_list.append(float(serialString[ro + 3:ya]))
        yaw_list.append(float(serialString[ya + 3:]))

        end_time = time.time()
        time_elapsed = (end_time - start_time)
        time_list.append(time_elapsed)


print(pitch_list)
print(roll_list)
print(yaw_list)

plt_pitch.title("Pitch angle vs time")
plt_pitch.plot(time_list, pitch_list)
plt_pitch.xlabel("Time (s)")
plt_pitch.ylabel("Pitch angle (degrees)")
plt_pitch.show()

plt_roll.title("Roll angle vs time")
plt_roll.plot(time_list, roll_list)
plt_roll.xlabel("Time (s)")
plt_roll.ylabel("Roll angle (degrees)")
plt_roll.show()

plt_yaw.title("Yaw angle vs time")
plt_yaw.plot(time_list, yaw_list)
plt_yaw.xlabel("Time (s)")
plt_yaw.ylabel("Yaw angle (degrees)")
plt_yaw.show()
