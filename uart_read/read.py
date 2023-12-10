import serial
import datetime
import argparse

options = {
    'port': {
        'name': '--port',
        'default': '/dev/ttyUSB0',
        'type': str,
        'help': 'serial port, default: /dev/ttyUSB0'
    },
    'baud': {
        'name': '--baud',
        'default': 9600,
        'type': int,
        'help': 'baudrate, default: 9600'
    },
    'file': {
        'name': '--file',
        'default': 'temp.txt',
        'type': str,
        'help': 'file name, default: temp.txt'
    }
}


def read_serail(args):
    ser = serial.Serial(args.port, args.baud)
    with open(args.file, 'a') as file:
        while 1:
            line = ser.readline().decode().strip()
            file.write(f'{datetime.datetime.now()},{line}\n')
            file.flush()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    for k, v in options.items():
        name, default, type, help = v['name'], v['default'], v['type'], v['help']
        parser.add_argument(name, default=default, type=type, help=help)
    args = parser.parse_args()

    read_serail(args)
