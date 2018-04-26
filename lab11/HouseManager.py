from typing import List
from HouseDevice import HouseDevice


class HouseManager:

    house_device_list = List

    def consumer_power(self):
        consume_power = 0
        for house_device in self.house_device_list:
            consume_power += house_device.power
        return consume_power

    def search_by_producer(self, producer):
        parameter_device_list = []
        for house_device in self.house_device_list:
            if house_device.producer == producer:
                parameter_device_list.append(house_device)
        return parameter_device_list

    def sort_by_power(self):
        self.house_device_list.sort(key=lambda house_device: house_device.power)
        return self.house_device_list

    def print_list(self, list):
        for house_device in list:
            print(house_device)
