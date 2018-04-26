from HouseDevice import HouseDevice
from DeviceType import DeviceType


class WashingMachine(HouseDevice):

    def __init__(self, id, producer, power, max_weight_load):
        super(WashingMachine, self).__init__(id, producer, power)
        self.device_type = DeviceType.washing_machine
        self.max_weight_load = max_weight_load

    def __str__(self):
        return super(WashingMachine, self).__str__() + " max weight to load: "+str(self.max_weight_load)