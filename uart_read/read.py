import serial
import datetime
import argparse

ser = serial.Serial('/dev/ttyUSB0', 9600)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default='/dev/ttyUSB0', help='serial port, default: /dev/ttyUSB0')
    parser.add_argument('--baud', default=9600, type=int, help='baudrate, default: 9600')
    parser.add_argument('--file', default='temp.txt', help='file name, default: temp.txt')
    args = parser.parse_args()

    ser = serial.Serial(args.port, args.baud)
    with open('temp.txt', 'a') as file:
        while 1:
            line = ser.readline().decode().strip()
            file.write(f'{datetime.datetime.now()},{line}\n')
            file.flush()
