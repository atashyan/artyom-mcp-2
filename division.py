def divide(a, b):
    if b == 0:
        return 'Cannot divide by zero'
    return a / b

if __name__ == '__main__':
    result = divide(5, 3)
    print(f'The quotient is: {result}')