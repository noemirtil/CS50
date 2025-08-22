# My first Python script

def main():
    name = input('Enter your name: ')
    print('Hello, ', name, '!')

if __name__ == '__main__':
    main()

def square(num):
    numSquared = num * num
    return numSquared

print(square(5)) # Prints 25
print(square(8)) # Prints 64
