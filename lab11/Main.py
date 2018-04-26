from AirConditining import AirConditining
from HairDrier import HairDrier
from Refrigerator import Refrigerator
from TV import TV
from WashingMachine import WashingMachine
from HouseManager import HouseManager


if __name__=='__main__':
    air = AirConditining(2, "Sakuto", 185, 15)
    drier = HairDrier(3,"kjfke", 125, 3)
    ref = Refrigerator(4, "prioek", 700, 295.6)
    tv = TV(5, "jdkwjd", 450, 21)
    wash = WashingMachine(6, "iieoeo", 489, 5)
    manager = HouseManager()
    manager.house_device_list = [air, drier, ref, tv, wash]
    manager.print_list(manager.house_device_list)
    print("\n\n\n")
    print(manager.consumer_power())
    print("\n\n\n")
    manager.print_list(manager.search_by_producer("Sakuto"))
    print("\n\n\n")
    manager.print_list(manager.sort_by_power())