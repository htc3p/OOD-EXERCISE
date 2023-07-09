class MyInt:
    def __init__(self, number):
        self.number = number

    def isPrime(self):
        if self.number <= 1:
            return False
        for i in range(2, int(self.number**0.5) + 1):
            if self.number % i == 0:   
                return False
        return True
    
    def showPrime(self):
        primes = ''
        if self.number < 2:
            return '!!!A prime number is a natural number greater than 1'
        for i in range(self.number+1):
            if MyInt(i).isPrime():
                primes += str(i) + ' '
        return primes

    def __sub__(self, other):
        return self.number - other.number//2
        

print(" *** class MyInt ***")

n, m = map(int, input("Enter 2 number : ").split())
a = MyInt(n)
b = MyInt(m)

print(n, "isPrime :", a.isPrime())
print(m, "isPrime :", b.isPrime())
print(f'Prime number between 2 and {n} :', a.showPrime())
print(f'Prime number between 2 and {m} :', b.showPrime())
print(f'{n} - {m} =', a-b)