# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 10:33:58 2021

@author: Luke
"""
import matplotlib.pyplot as plt
import serial
import time

serialPort = serial.Serial(port="COM4", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)


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

counter = 0;

start_time = time.time()
while 1:

    if serialPort.in_waiting > 0:

        serialString = serialPort.readline()

        serialString = serialString.decode('Ascii')
        gyro_x = "vx"
        gyro_y = "vy"
        gyro_z = "vz"
        mag_x = "mx"
        mag_y = "my"
        mag_z = "mz"
        acc_x = "ax"
        acc_y = "ay"
        acc_z = "az"

        # if gyro_x in serialString:
        #     x = serialString.find(gyro_x)
        #     y = serialString.find(gyro_y)
        #     z = serialString.find(gyro_z)
        #     gx.append(float(serialString[x + 3:y]))
        #     gy.append(float(serialString[y + 3:z]))
        #     gz.append(float(serialString[z + 3:]))
        #
        #     end_time = time.time()
        #     time_elapsed = (end_time - start_time)
        #     tg.append(time_elapsed)
        #     plt1.subplot(2, 2, 1)
        #     plt1.plot(tg, gx)
        #     plt1.title("x-axis")
        #     plt1.subplot(2, 2, 2)
        #     plt1.plot(tg, gy)
        #     plt1.title("y-axis")
        #     plt1.subplot(2, 2, 3)
        #     plt1.plot(tg, gz)
        #     plt1.title("z-axis")
        #     plt1.suptitle("Gyroscope Data")
        #     plt1.tight_layout()
        #
        #     plt1.show()

        if acc_x in serialString:
            x = serialString.find(acc_x)
            y = serialString.find(acc_y)
            z = serialString.find(acc_z)
            ax.append(float(serialString[x + 3:y]))
            ay.append(float(serialString[y + 3:z]))
            az.append(float(serialString[z + 3:]))

            counter += 1

            print(counter, "ax: ", ax[-1], "ay: ", ay[-1], "az: ", az[-1])

            # end_time = time.time()
            # time_elapsed = (end_time - start_time)
            # ta.append(time_elapsed)
            # plt2.subplot(2, 2, 1)
            # plt2.plot(ta, ax)
            # plt2.title("x-axis")
            # plt2.subplot(2, 2, 2)
            # plt2.plot(ta, ay)
            # plt2.title("y-axis")
            # plt2.subplot(2, 2, 3)
            # plt2.plot(ta, az)
            # plt2.title("z-axis")
            # plt2.suptitle("Accelerometer data")
            # plt2.tight_layout()
            # plt2.show()

        # if mag_x in serialString:
        #     x = serialString.find(mag_x)
        #     y = serialString.find(mag_y)
        #     z = serialString.find(mag_z)
        #     mx.append(float(serialString[x + 3:y]))
        #     my.append(float(serialString[y + 3:z]))
        #     mz.append(float(serialString[z + 3:]))
        #
        #     end_time = time.time()
        #     time_elapsed = (end_time - start_time)
        #     tm.append(time_elapsed)
        #     plt3.subplot(2, 2, 1)
        #     plt3.plot(tm, mx)
        #     plt3.title("x-axis")
        #     plt3.subplot(2, 2, 2)
        #     plt3.plot(tm, my)
        #     plt3.title("y-axis")
        #     plt3.subplot(2, 2, 3)
        #     plt3.plot(tm, mz)
        #     plt3.title("z-axis")
        #     plt3.suptitle("Magnetometer data")
        #     plt3.tight_layout()
        #     plt3.show()