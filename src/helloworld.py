# Define a new class named 'HelloWorld' using PascalCase
class HelloWorld:
    
    # The constructor method. Python runs this automatically when you create a new object.
    def __init__(self):
        # Create an instance variable (attribute) called 'message' and store the string in it
        self.message = "Hello, World!"

    # A custom method (function inside a class) to print the stored message
    def say_hello(self):
        # 'self' allows the method to look inside the object and find 'self.message'
        print(self.message)


# This checks if the script is being run directly (not being imported into another file)
if __name__ == "__main__":
    
    # 1. Instantiate the class: This creates a new object based on the HelloWorld blueprint
    greeter = HelloWorld()
    
    # 2. Call the method: This tells the 'greeter' object to execute its 'say_hello' function
    greeter.say_hello()


 #print("Hello, World!")            #byitself works just fine
