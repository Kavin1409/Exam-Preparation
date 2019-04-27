class SimpleMaths():
    '''
    A simple class to allow calculations to be performed on an integer.
    '''
    def __init__(self, number):
        self.number = number
        
        if type(self.number) != int:
            if type(self.number) == float:
                raise ValueError(
                  self.number, "is not an integer. It is a float")
            if type(self.number) == str:
                raise ValueError(
                  self.number, "is not an integer. It is a string")
            if type(self.number) == complex:
                raise ValueError(
                  self.number, "is not an integer. It is a complex number")
            if type(self.number) == bool:
                raise ValueError(
                  self.number, "is not an integer. It is a boolean")
        

    def square(self):
        return self.number ** 2

    def _factorial(self, value):
        if value == 0:
            return 1
        else:
            return value * self._factorial(value - 1)

    def factorial(self):
        if self.number < 0:
            raise ValueError(
                  self.number, "a negative number. No factorial")
        return self._factorial(self.number)

    def power(self, power=3):
        if type(power) == bool:
            raise ValueError(
              power, "Power given is a boolean")
        return self.number ** power

    def odd_or_even(self):
        '''
        Note that this code assumes that 0 is even.
        '''
        if (self.number % 2) == 0:
            return 'Even'
        elif (self.number % 2) == 1:
            return 'Odd'

    def square_root(self):
        if self.number < 0:
            raise ValueError(
                  self.number, "a negative number")
        return self.number ** (0.5)
