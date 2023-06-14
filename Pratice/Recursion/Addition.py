class AddArray:
    def __init__(self, my_array):
        self.my_array = my_array or {}
        self.total = 0

    def __sub_adder(self, my_array):
        while self.my_array:
            self.total += self.my_array[0]  # Add the first index in the array to the sum holder
            self.my_array = self.my_array[1:]  # Remove the first # from the array i.e. 2: means the first two
            self.__sub_adder(self.my_array)  # Pass the updated array back into the method

    def add(self):
        # if there are items in the list, send it through the sub_adder method
        if self.my_array:
            self.__sub_adder(self.my_array)

    def printer(self):
        print(self.total)


myAdder = AddArray([1, 2, 3, 4])
myAdder.add()
myAdder.printer()
