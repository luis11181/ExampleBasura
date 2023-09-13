# Importing the function from helper_functions.py
from helper_functions import imported_function


# Explaining basic data types
def explain_data_types():
    print("\n=== Data Types in Python ===")
    print("Integers, Floats, Strings, Lists, Dictionaries.")
    a = 5  # Integer
    b = 5.5  # Float
    c = "Hello, World!"  # String
    d = [1, 2, 3]  # List
    e = {"name": "Alice", "age": 30}  # Dictionary
    print(f"a is {a}, type: {type(a)}")
    print(f"b is {b}, type: {type(b)}")
    print(f"c is {c}, type: {type(c)}")
    print(f"d is {d}, type: {type(d)}")
    print(f"e is {e}, type: {type(e)}")


# Explaining scopes
global_variable = "I'm a global variable"


def explain_scopes():
    print("\n=== Scopes in Python ===")
    print(f"In the main scope, global_variable is {global_variable}")

    def outer_function():
        global global_variable  # modifies the global variable
        local_variable = "I'm a local variable of outer_function"
        local_variable2 = "I'm a local variable of outer_function"

        def inner_function():
            nonlocal local_variable  # modifies the local variable in the outer function
            local_variable = "Modified local variable"
            print(f"Inside inner_function, local_variable is {local_variable}")

        inner_function()
        print(f"Inside outer_function, local_variable is {local_variable}")

        def inner_function2():
            local_variable2 = "Modified local variable 2"
            print(f"Inside inner_function2, local_variable is {local_variable2}")

        inner_function2()
        print(f"Inside outer_function2, local_variable is {local_variable2}")

    outer_function()


# Explaining functions
def explain_functions():
    print("\n=== Functions in Python ===")

    def add(a, b):
        return a + b

    def greet(name):
        return f"Hello, {name}!"

    print(f"add(5, 3) returns {add(5, 3)}")
    print(f"greet('Alice') returns {greet('Alice')}")


# Explaining string functions
def explain_string_functions():
    print("\n=== Basic String Functions ===")

    sample_str = "hello"
    print(f"Original string: {sample_str}")
    print(f"Upper case: {sample_str.upper()}")
    print(f"Capitalized: {sample_str.capitalize()}")
    print(f"Replace 'l' with 'r': {sample_str.replace('l', 'r')}")


# Explaining number functions
def explain_number_functions():
    print("\n=== Basic Number Functions ===")

    print(f"Absolute value of -5: {abs(-5)}")
    print(f"Rounded value of 5.7: {round(5.7)}")
    print(f"Maximum number in [1, 2, 3, 4]: {max([1, 2, 3, 4])}")


# Explaining how to import from other Python files
def explain_imports():
    print("\n=== Importing from Other Files ===")
    print(imported_function())


# Explaining how to read from a file
def explain_file_reading():
    print("\n=== Reading from a File ===")
    try:
        with open("sample.txt", "r") as file:
            content = file.read()
            print(f"Content of sample.txt:\n{content}")
    except FileNotFoundError:
        print("File sample.txt not found.")


# Explaining classes
def explain_classes():
    print("\n=== Classes in Python ===")

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self):
            return f"Hello, my name is {self.name} and I'm {self.age} years old."

    alice = Person("Alice", 30)
    print(alice.greet())


# Main menu function
def main():
    while True:
        print("\nWhat would you like to learn about?")
        print("1. Data Types")
        print("2. Scopes")
        print("3. Functions")
        print("4. Basic String Functions")
        print("5. Basic Number Functions")
        print("6. Importing from Other Files")
        print("7. Reading from a File")
        print("8. Classes")
        print("10. Quit")

        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            explain_data_types()
        elif choice == "2":
            explain_scopes()
        elif choice == "3":
            explain_functions()
        elif choice == "4":
            explain_string_functions()
        elif choice == "5":
            explain_number_functions()
        elif choice == "6":
            explain_imports()
        elif choice == "7":
            explain_file_reading()
        elif choice == "8":
            explain_classes()
        elif choice == "10":
            print("Exiting. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# def exampleTypes(numero: int) -> str:
#     return "hola"
