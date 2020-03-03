from abc import abstractmethod

class Bird:
    fly=True

    def noise(self):
        print("Birdnoise")
    
    babies=0

    def reproduce(self):
        self.babies +=1
    
    @abstractmethod
    def eat(self):
        pass

    extinct=False

class owl(Bird):
    def reproduce(self):
        self.babies +=6
    
    def eat(self):
        print("peck peck")

class Dodo(Bird):
    fly=False
    extince=True

    def eat(self):
        print("Nom Nom")

    def reproduce(self):
        if self.extinct ==False:
            self.babies +=1
        else:
            print("No more Dodo's")

# for this subclass have used polymorphism to override the reproduce method and fly and extinct variables
# encapsulation to keep the babies variable from being directly accessed as well as inheritance again to 
# create a child class of bird