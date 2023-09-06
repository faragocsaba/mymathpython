def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    for i in range(1, 20) :
        if is_prime(i):
            print(i)
