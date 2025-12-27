class Laptop:

    def __init__(self, make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def power_on(self):
        print("the laptop is being started")
    def shut_down(self):
        print("the laptop is being shutdown")

