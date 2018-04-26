from HouseDevice import HouseDevice
from DeviceType import DeviceType


class HairDrier(HouseDevice):

    def __init__(self, id, producer, power, speed_number):
        super(HairDrier, self).__init__(id, producer, power)
        self.device_type = DeviceType.hair_drier
        self.speed_number = speed_number

    def __str__(self):

        return super(HairDrier, self).__str__() + " speed number: "+str(self.speed_number)