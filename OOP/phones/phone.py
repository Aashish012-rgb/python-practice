class Phone:

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def wow(self):
        print("this " + self.model + " is awesome")

    def waw(self):
        print("this " + self.model + " is good but not useful")