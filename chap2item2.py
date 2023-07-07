class Spherical:

    def __init__(self,r):

        self.radius = r
        self.pi = calculate_pi(1000000)

    def changeR(self,Radius):

        self.radius = Radius

    def findVolume(self):

        vol = (4/3)*self.pi*(self.radius**3)
        return vol

    def findArea(self):

        area = 4*self.pi*(self.radius**2)
        return area

    def __str__(self):

        return "Radius ={} Volumn = {} Area = {}".format(self.radius, self.findVolume(), self.findArea())

def calculate_pi(iterations):
    pi = 0.0
    sign = 1.0

    for i in range(iterations):
        term = sign / (2 * i + 1)
        pi += term
        sign *= -1

    pi *= 4.0
    return pi
    

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)