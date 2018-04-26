from HouseDevice import HouseDevice
from DeviceType import DeviceType


class Refrigerator(HouseDevice):

    def __init__(self, id, producer, power, volume):
        super(Refrigerator, self).__init__(id, producer, power)
        self.device_type = DeviceType.refrigerator
        self.volume = volume

    def __str__(self):
        return super(Refrigerator, self).__str__() + " Volume: "+str(self.volume)