class Powers(object):
    def __init__(self, name):
        self.name = name

    def power_of(self, base, power):
        if power > 1:
            return base * self.power_of(base, (power - 1))
        elif power == 1:
            return base
        else:
            print("Error")


myPower = Powers("Peter")
print(myPower.power_of(3, 2))
print(myPower.name)
