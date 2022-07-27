class Car:
    def intro(self):
        print("There are many types of Cars.")
  
    def expen(self):
        print("Most of the cars are expensive.")

class bmw(Car):
    def expen(self):
        print("Price of BMW is greater than 50 Lakh.")
  
class nano(Car):
    def expen(self):
        print("Price of Nano is less than 5 Lakh.")
  
obj_Car = Car()
obj_bmw = bmw()
obj_nano = nano()

obj_Car.intro()
obj_Car.expen()

obj_bmw.intro()
obj_bmw.expen()

obj_nano.intro()
obj_nano.expen()