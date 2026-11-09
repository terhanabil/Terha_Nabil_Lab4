
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def goldbach(n):
    if n <= 2 or n % 2 != 0:
        print("Please enter an even number greater than 2.")
        return

    print("Goldbach decompositions:")

    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            print(n, "=", i, "+", n - i)


number = input("Enter an even number: ")

if number.isdigit():
    goldbach(int(number))
else:
    print("Invalid input. Please enter a natural number.")
