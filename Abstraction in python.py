from abc import ABC,abstractclassmethod
class car(ABC):
   @abstractclassmethod
   def milage(self):
    pass
   def color(self):
       print("white")

class Maruthi_suzuki(car):
   def milage(self):
      print("milage is 35 kmph")
class Duster(car):
   def milage(self):
      print("milage is 40 kmph")
class TATA(car):
   def milage(self):
       print("milage is 40 kmph")

m1=Maruthi_suzuki()
t1=TATA()
d1=Duster()
t1.milage()
m1.milage()
t1.color()
m1.color()
d1.color()
d1.milage()
from  abc import ABC,abstractclassmethod
class CMD(ABC):
   @abstractclassmethod
   def cd(self,dir):
      pass
   def exist(self):
      pass
 
      


