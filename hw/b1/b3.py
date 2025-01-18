def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


sum = sum(num for num in range(100) if isPrime(num))
print(sum)
