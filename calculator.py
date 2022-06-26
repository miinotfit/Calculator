from re import sub

def addition(x,y):
    return x + y 

def subtraction(x,y):
    return x - y 

def multiplication(x,y):
    return x * y 

def division(x,y):
    return x / y 

print ("Welcome to my Calculator")
inp = 0

while inp != 5:
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except:
            print("That's not a valid option!")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except:
            print("That's not a valid option!")
            
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    inp = float(input("Choose an operation: "))

    if inp == 1:
        print(num1, "+", num2, "=", addition(num1, num2))

    elif inp == 2:
        print(num1, "-", num2, "=", subtraction(num1, num2))

    elif inp == 3:
        print(num1, "*", num2, "=", multiplication(num1, num2))

    elif inp == 4:
        print(num1, "/", num2, "=", division(num1, num2))

    else:
        quit()

