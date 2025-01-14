class car:
    def __init__(self,brand,colour):
        self.brand=brand
        self.colour=colour
         

    def engine(self):
        print(f"the {self.colour} {self.brand} eagine has started")


car1=car("bmw","blue")
car2=car("audi","white")

car1.engine()
car2.engine()
        