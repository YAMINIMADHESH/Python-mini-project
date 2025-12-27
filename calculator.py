import sys
import math

# Arithmetic functions

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Division by zero is not allowed')
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError('Modulus by zero is not allowed')
    return a % b


def factorial(n):
    if n < 0:
        raise ValueError('Factorial is not defined for negative numbers')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Helper to parse a float or int input

def parse_number(s):
    try:
        if '.' in s:
            return float(s)
        return int(s)
    except Exception:
        return float(s)


def run_demo():
    print('Demo: calculator functions')
    a, b = 23, 7
    print(f'{a} + {b} =', add(a, b))
    print(f'{a} - {b} =', subtract(a, b))
    print(f'{a} * {b} =', multiply(a, b))
    print(f'{a} / {b} =', divide(a, b))
    print(f'{a} ** {2} =', power(a, 2))
    print(f'{a} % {b} =', modulus(a, b))
    print('5! =', factorial(5))


def interactive():
    menu = '''
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power (a ** b)
6. Modulus (a % b)
7. Factorial (single integer n)
0. Exit
'''
    while True:
        print(menu)
        choice = input('Enter choice: ').strip()
        if choice == '0':
            print('Goodbye')
            break
        try:
            if choice == '7':
                n_str = input('Enter integer n: ').strip()
                n = int(n_str)
                print('Result:', factorial(n))
                continue

            a_str = input('Enter first number: ').strip()
            b_str = input('Enter second number: ').strip()
            a = parse_number(a_str)
            b = parse_number(b_str)

            if choice == '1':
                print('Result:', add(a, b))
            elif choice == '2':
                print('Result:', subtract(a, b))
            elif choice == '3':
                print('Result:', multiply(a, b))
            elif choice == '4':
                print('Result:', divide(a, b))
            elif choice == '5':
                print('Result:', power(a, b))
            elif choice == '6':
                print('Result:', modulus(a, b))
            else:
                print('Invalid choice, try again')
        except Exception as e:
            print('Error:', e)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'demo':
        run_demo()
    else:
        interactive()
