def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    num = int(input("Enter a number: "))
    print("Factorial:", factorial(num))
    print("Fibonacci:", fibonacci(num))

if __name__ == "__main__":
    main()
