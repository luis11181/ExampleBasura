def explain_data_types():
    print("\n=== Data Types in Python ===")
    a = 5
    b = 5.5
    c = "Hello, World!"
    d = [1, 2, 3]
    e = {"name": "Alice", "age": 30}

    print(f"a is {a} and its type is {type(a)}")
    print(f"b is {b} and its type is {type(b)}")
    print(f"c is {c} and its type is {type(c)}")
    print(f"d is {d} and its type is {type(d)}")
    print(f"e is {e} and its type is {type(e)}")


def explain_scopes():
    print("\n=== Scopes in Python ===")
    global_variable = "I'm a global variable"

    def inner_function():
        nonlocal_variable = "I'm a nonlocal variable"
        print(f"Inside inner_function, global_variable is {global_variable}")
        print(f"Inside inner_function, nonlocal_variable is {nonlocal_variable}")

    def outer_function():
        local_variable = "I'm a local variable"
        inner_function()
        print(f"Inside outer_function, local_variable is {local_variable}")

    outer_function()
    print(f"In the main scope, global_variable is {global_variable}")


def explain_functions():
    print("\n=== Functions in Python ===")

    def add(a, b):
        return a + b

    def greet(name):
        return f"Hello, {name}!"

    print(f"add(5, 3) returns {add(5, 3)}")
    print(f"greet('Alice') returns {greet('Alice')}")


def main():
    while True:
        print("\nWhat would you like to learn about?")
        print("1. Data Types")
        print("2. Scopes")
        print("3. Functions")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            explain_data_types()
        elif choice == "2":
            explain_scopes()
        elif choice == "3":
            explain_functions()
        elif choice == "4":
            print("Exiting. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
