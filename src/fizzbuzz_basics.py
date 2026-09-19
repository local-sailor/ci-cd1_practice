# HOW TO RUN: python3 fizzbuzz_basics.py

while True:  # loop forever until we break
    n = int(input("Enter a number (0 to quit): "))  # read text, convert to int

    if n == 0:  # sentinel value to exit
        print("Goodbye!")
        break  # exit the loop

    if n % 15 == 0:  # % is modulus (remainder of division)
        print("FizzBuzz")
    elif n % 3 == 0:  # elif = "else if"
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
