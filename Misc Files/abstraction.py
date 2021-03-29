from abc import ABC, abstractmethod


# ABC: Abstract Base Class
class car(ABC):  # Abstract Parent Class
    def paySlip(self, amount):
        print('Your purchase amount: ', amount)

    @abstractmethod
    def payment(self, amount):  # Abstract method
        pass


class DebitCarPayment(car):  # Child class
    # Define payment function from the parent class
    def payment(self, amount):  # Define how to implement abstract method from parent class
        print('Your purchase amount of {} exceeded your $100 limit'.format(amount))


obj = DebitCarPayment()     # Instantiate DebitCarPayment()
obj.paySlip('$400')         # Method paySlip from parent abstract parent class
obj.payment('$400')         #

# obj2 = car() doesn't work because you can't make an instance of an abstract class
