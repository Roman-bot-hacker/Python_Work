from abc import ABC


class HouseDevice(ABC):

    device_type = None

    def __init__(self, id, producer, power):
        self.id = id
        self.producer = producer
        self.power = power

    def __str__(self):
        return str(self.device_type) + " " + str(self.producer) + " " + str(self.id) + " " + str(self.power)+" "
