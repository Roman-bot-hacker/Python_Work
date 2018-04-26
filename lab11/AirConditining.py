from HouseDevice import HouseDevice
from DeviceType import DeviceType


class AirConditining(HouseDevice):

    def __init__(self, id, producer, power, cold_producity):
        super(AirConditining, self).__init__(id, producer, power)
        self.device_type = DeviceType.air_conditining
        self.cold_producity = cold_producity

    def __str__(self):
        return super(AirConditining, self).__str__() + " cold producity: "+str(self.cold_producity)