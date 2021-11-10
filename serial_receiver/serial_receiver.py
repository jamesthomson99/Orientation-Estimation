import matplotlib.pyplot as plt
import serial
import time

serialPort = serial.Serial(port="COM4", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

serialString = ""

plt1 = plt
plt2 = plt
plt3 = plt
plth = plt

gx = []
gy = []
gz = []
tg = []

ax = []
ay = []
az = []
ta = []

mx = []
my = []
mz = []
tm = []

start_time = time.time()
current_time = time.time()
while current_time - start_time < 10:

    current_time = time.time()

    if serialPort.in_waiting > 0:

        serialString = serialPort.readline()
        print("Before Ascii: ", serialString)
        serialString = serialString.decode('Ascii')
        print("After Ascii", serialString)
        gyro_x = "vx"
        gyro_y = "vy"
        gyro_z = "vz"
        mag_x = "mx"
        mag_y = "my"
        mag_z = "mz"
        acc_x = "ax"
        acc_y = "ay"
        acc_z = "az"

        if gyro_x in serialString:
            x = serialString.find(gyro_x)
            y = serialString.find(gyro_y)
            z = serialString.find(gyro_z)
            gx.append(float(serialString[x + 3:y]))
            gy.append(float(serialString[y + 3:z]))
            gz.append(float(serialString[z + 3:]))

            # end_time = time.time()
            # time_elapsed = (end_time - start_time)
            # tg.append(time_elapsed)
            # plt1.plot(tg, gx, label="x-axis")
            # plt1.plot(tg, gy, label="y-axis")
            # plt1.plot(tg, gz, label="z-axis")
            # plt1.title("Gyroscope data")
            # plt.legend(loc="upper right")
            # plt1.show()

        if acc_x in serialString:
            x = serialString.find(acc_x)
            y = serialString.find(acc_y)
            z = serialString.find(acc_z)
            ax.append(float(serialString[x + 3:y]))
            ay.append(float(serialString[y + 3:z]))
            az.append(float(serialString[z + 3:]))

            # end_time = time.time()
            # time_elapsed = (end_time - start_time)
            # ta.append(time_elapsed)
            # plt2.plot(ta, ax, label="x-axis")
            # plt2.plot(ta, ay, label="y-axis")
            # plt2.plot(ta, az, label="z-axis")
            # plt2.title("Accelerometer data")
            # plt.legend(loc="upper right")
            # plt2.show()

        if mag_x in serialString:
            x = serialString.find(mag_x)
            y = serialString.find(mag_y)
            z = serialString.find(mag_z)
            mx.append(float(serialString[x + 3:y]))
            my.append(float(serialString[y + 3:z]))
            mz.append(float(serialString[z + 3:]))

            # end_time = time.time()
            # time_elapsed = (end_time - start_time)
            # tm.append(time_elapsed)
            # plt3.plot(tm, mx, label="x-axis")
            # plt3.plot(tm, my, label="y-axis")
            # plt3.plot(tm, mz, label="z-axis")
            # plt3.title("Magnotometer data")
            # plt.legend(loc="upper right")
            # plt3.show()

print(ax)
print(ay)
print(az)
