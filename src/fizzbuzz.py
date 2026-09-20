# HOW TO RUN: python3 fizzbuzz_basics.py


def main(): 
    while True:  # loop forever until we break
        n = int(input("Enter a number (0 to quit): "))  # read text, convert to int
        if n == 0:  # sentinel value to exit
            print("Goodbye!")
            break  # exit the loop
            print(fizzbuzz(n))


def fizzbuzz(n):
    if n % 15 == 0:  # % is modulus (remainder of division)
        return "FizzBuzz"
    elif n % 3 == 0:  # elif = "else if"
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


if __name__ == "__main__":
    main()



