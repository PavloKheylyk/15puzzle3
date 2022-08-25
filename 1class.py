class Rest:
    def __init__(self, rest_name, cuisine_type):
        self.rest_name = rest_name
        self.cuisine_type = cuisine_type

    def descr_rest(self):
        print(f"{self.rest_name} is a restaurant of {self.cuisine_type} food")


mnr = Rest("HongKong", "Chinese")
mnr.descr_rest()
