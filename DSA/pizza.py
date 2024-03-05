n = input()

def superprime(n):
    k = str(n)
    if prime(n) == True:
        for i in range(0, len(k) - 1):
            k = k[:-1]
            if prime(int(k)) == False:
                return False
    else:
        return False
    return True

def prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    if n % 2 == 0 or n % 5 == 0 or n % 7 == 0 or n % 3 == 0:
        return False
    else:
        for i in range(3, int(n**(1/2)) + 1, 2):
            if n % i == 0:
                return False
    return True


for i in range(int(n)):
    if i == 2 or i == 3 or i == 5 or i == 7:
        print(i, end = " ")
    if i >= 23 and i % 2 != 0 and i % 5 != 0 and i%3 != 0 and i%7 != 0:
        if superprime(i) == True:
            print(i, end = " ")