import unittest

from communication import Communication
from motor_control import user_input


class TestModules(unittest.TestCase):

    def test_motor_user_input(self):
        port = '/dev/tty.usbmodem1433401'
        baudrate = 9600
        timeout = 3
        arduino = Communication(port)
        for i in range(10):
            data = user_input()
            arduino.send(data)
            while not arduino.buffer:
                arduino.receive()
                if arduino.buffer:
                    print(arduino.buffer)


if __name__ == '__main__':
    unittest.main()
