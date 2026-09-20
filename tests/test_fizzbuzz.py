from fizzbuzz import fizzbuzz


def test_A():
    assert fizzbuzz(3) == "Fizz"
    

def test_B():
    assert fizzbuzz(5) == "Buzz"


def test_C():
    assert fizzbuzz(15) == "FizzBuzz"


def test_D():
    assert fizzbuzz(7) == "7"
