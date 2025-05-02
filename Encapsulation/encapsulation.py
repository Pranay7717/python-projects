class Car:
  def __init__(self, owner, miles, speed):
      self.owner = owner
      self.__miles = miles
      self.__speed = speed
  @property
  def mileage(self):
      return self.__miles
  @mileage.setter
  def mileage(self, distance):
      if distance > 0:
          self.__miles = distance
      else:
         print("Invalid miles value")
  @property
  def speed(self):
      return self.__speed
  @speed.setter
  def speed(self, new_speed):
      if 0 <= new_speed <= 200:
           self.__speed = new_speed
      else:
          print("Speed must be between 0 and 200 mph")
  def drive(self, distance):
      if distance > 0:
          self.__miles += distance
          print(f"Drove {distance} miles")
      else:
          print("Distance must be positive")
my_car = Car("Pranay", 150, 0)
print(my_car.owner)
print(my_car.mileage)
my_car.speed = 76
print(my_car.speed)
my_car.drive(140)
print(my_car.mileage)