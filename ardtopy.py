from serial.tools import list_ports
import serial
import time
import csv

ports = list_ports.comports()
for port in ports: print(port)

f = open("data.csv", "w", newline='')
f.truncate()
serialcom = serial.Serial('COM3', 9600)

serialcom.setDTR(False)
time.sleep(1)
serialcom.flushInput()
serialcom.setDTR(True)

sampled_points = 187
for sampled_point in range(sampled_points):
	try:
		s_bytes = serialcom.readline()
		decoded_bytes = s_bytes.decode("utf-8").strip('\r\n')
		print(decoded_bytes)
		if sampled_point == 0:
			values = decoded_bytes.split(",")
		else:
			values = [float(x) for x in decoded_bytes.split()]
		print(values)
		
		write = csv.writer(f,delimiter=",")
		write.writerow(values)


	except:
		print("Error")
f.close()
