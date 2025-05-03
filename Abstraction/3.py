from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass 
    def fuel(self):
        print("There is enough fuel")
class Car(Vehicle):
    def drive(self):
        print("Car is being driven")
v = Car()
v.drive()
v.fuel()
