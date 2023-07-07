class MyInt:
    def __init__(self, number):
        self.number = number

    def isPrime(self):
        if self.number<2:
            return False
        for i in range(2, int(self.number**0.5) + 1):
            if self.number % i == 0:   
                return False
        return True
    
    def showPrime(self):
        primes = []
        for i in range(2, self.number+1):
            if MyInt(i).isPrime():
                primes.append(i)
        return primes

    def __sub__(self, other):
        half_other = other / 2
        return round(self.number - half_other)
        

print(" *** class MyInt ***")

n, m = map(int, input("Enter 2 number : ").split())
a = MyInt(n)
b = MyInt(m)
print(n, "isPrime :", a.isPrime())
print(m, "isPrime :", b.isPrime())

print("Prime number between 2 and", n, ":", end=" ")
listA = a.showPrime()
if len(listA)<=0:
    print("!!!A prime number is a natural number greater than 1", end="")
else:
    for i in listA:
        print(i, end=" ")

print("\n", end="")
print("Prime number between 2 and", m, ":", end=" ")
listB = b.showPrime()
if len(listB)<=0:
    print("!!!A prime number is a natural number greater than 1", end="")
else:
    for i in listB:
        print(i, end=" ")

diff = a.__sub__(m)
print("\n", end="")
print(n, "-", m, "=", diff)