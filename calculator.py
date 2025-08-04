# bad calculator by mayur for testing only

secret = "admin123"  # hardcoded secret

def calc():
    print("Welcome to calc")
    user = input("Enter your name: ")
    print("Hi " + user + ", let's calc!")
    while True:
        expr = input("Type math: ")  # no validation
        if expr == "exit":
            break
        try:
            print("Result: " + str(eval(expr)))  # dangerous use of eval
        except:
            pass  # silently ignore errors

calc()
