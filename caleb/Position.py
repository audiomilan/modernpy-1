from enum import Enum

class Position():
    def __init__(self, pan, tilt, zoom):
        self.pan = pan
        self.tilt = tilt
        self.zoom = zoom

    def log(self):
        print(self.pan, self.tilt, self.zoom)


class Camera:
    def __init__(self, serial_number, position, camera_type):
        self.serial_number = serial_number
        self.position = position
        self.camera_type = camera_type

    def log(self):
        print(self.serial_number, self.camera_type)
        self.position.log()

    class CameraType(Enum):
        ptz = 0
        eptz = 1
        stationary = 2


c = Camera("abcde", Position('10', '11', '12'), Camera.CameraType.eptz)
c.log()