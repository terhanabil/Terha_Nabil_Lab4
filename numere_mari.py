
def addition(a, b):
    result = []
    carry = 0

    a = a[::-1]
    b = b[::-1]

    length = max(len(a), len(b))

    for i in range(length):
        digit1 = int(a[i]) if i < len(a) else 0
        digit2 = int(b[i]) if i < len(b) else 0

        total = digit1 + digit2 + carry

        result.append(str(total % 10))
        carry = total // 10

    if carry > 0:
        result.append(str(carry))

    return ''.join(result[::-1])


def multiplication(a, b):
    result = [0] * (len(a) + len(b))

    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):

            product = int(a[i]) * int(b[j])

            total = product + result[i + j + 1]

            result[i + j + 1] = total % 10
            result[i + j] += total // 10

    answer = ''.join(map(str, result))

    answer = answer.lstrip('0')

    if answer == '':
        return '0'

    return answer


def main():
    try:
        with open("numere.txt", "r") as file:
            numbers = file.readlines()

        if len(numbers) != 2:
            print("The file must contain exactly two numbers.")
            return

        a = numbers[0].strip()
        b = numbers[1].strip()

        if not a.isdigit() or not b.isdigit():
            print("Invalid numbers in the file.")
            return

        if len(a) > 200 or len(b) > 200:
            print("Numbers must contain at most 200 digits.")
            return

        a = a.lstrip('0') or '0'
        b = b.lstrip('0') or '0'

        print("First number:", a)
        print("Second number:", b)

        print("Addition:", addition(a, b))
        print("Multiplication:", multiplication(a, b))

    except FileNotFoundError:
        print("Error: numere.txt was not found.")


main()
