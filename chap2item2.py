pi = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328238644709384
class Spherical:

    def __init__(self,r):

        self.radius = r
        
    def changeR(self,Radius):

        self.radius = Radius

    def findVolume(self):

        vol = (4/3)*pi*(self.radius**3)
        return vol

    def findArea(self):

        area = 4*pi*(self.radius**2)
        return area

    def __str__(self):

        return "Radius ={} Volumn = {} Area = {}".format(self.radius, self.findVolume(), self.findArea())
    

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)