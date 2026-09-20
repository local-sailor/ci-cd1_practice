from helloworld import greet
from helloworldB import greet as #greetBeta #testing a second file with an identical function

def test_greet_returns_message():
    assert greet() == "Hello World!"
    assert greetBeta() == "Hello World!" #second file


