from HouseDevice import HouseDevice
from DeviceType import DeviceType


class TV(HouseDevice):

    def __init__(self, id, producer, power, diagonal):
        super(TV, self).__init__(id, producer, power)
        self.device_type = DeviceType.tv
        self.diagonal = diagonal

    def __str__(self):
        return super(TV, self).__str__() + " Diagonal: "+str(self.diagonal)