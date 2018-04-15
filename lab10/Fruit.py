class Fruit:
    total_price = 0

    def __init__(self, type_of_fruit = "Apple", sort_of_fruit = "Golden", producer = "Ukraine",
                 price_by_kg = 29.5, lot_number = "150418"):
        self.type_of_fruit = type_of_fruit
        self.sort_of_fruit = sort_of_fruit
        self.producer = producer
        self.price_by_kg = price_by_kg
        self.lot_number = lot_number
        Fruit.total_price += price_by_kg

    def to_string(self):
        print("Type of fruit: "+self.type_of_fruit+"; Sort of fruit: "+self.sort_of_fruit+
              "; Producer: "+self.producer+"; Lot number: "+self.lot_number)

    def print_sum(self):
        print("Price of "+str(self.type_of_fruit)+" "+str(self.sort_of_fruit)+" is "+str(self.price_by_kg))

    @staticmethod
    def print_static_sum():
        print("Total price for fruits is "+str(Fruit.total_price))


if __name__=='__main__':
    apple = Fruit()
    orange = Fruit("Orange", "Cinesis", "Spain", 54.5)
    banana = Fruit("Banana", "Small", "Kongo", 36.6, "160218")

    apple.to_string()
    orange.to_string()
    banana.to_string()

    apple.print_sum()
    orange.print_sum()
    banana.print_sum()
    Fruit.print_static_sum()

