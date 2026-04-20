class destex:
    def __init__ (self, name):
        self.name = name
        print("Constructor called the", name)
    def __del__ (self):
        print("Destructor called", self.name)
d1 = destex("you zaid right shaik zaid right")
del d1
