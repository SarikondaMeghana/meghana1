history=[]
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "invalid operation"
    return a / b


print("Select operation.")
print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.History\n6.Exit")

while True:

    condition = input("Enter choice(1/2/3/4/5/6): ")

    if condition in ('1', '2', '3', '4','5','6'):
        if condition == "6":
            break
        if condition == '5':
            for i in history:
                print(i)
            continue
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if condition == '1':
            addition=add(num1, num2)
            print(num1, "+", num2, "=",addition)
            str1="addition of "+str(num1)+" + "+str(num2)+" = "+str(addition)
            history.append(str1)

        elif condition == '2':
            sub=subtract(num1, num2)
            print(num1, "-", num2, "=", sub)
            str2 = "subtraction of " + str(num1) + " - " + str(num2) + " = " + str(sub)
            history.append(str2)

        elif condition == '3':
            mul=multiply(num1, num2)
            print(num1, "*", num2, "=",mul)
            str3 = "multiplication of " + str(num1) + " * " + str(num2) + " = " + str(mul)
            history.append(str3)

        elif condition == '4':
            div=divide(num1, num2)
            print(num1, "/", num2, "=",div)
            str4 = "division of " + str(num1) + " / " + str(num2) + " = " + str(div)
            history.append(str4)
    else:
        print("Invalid Input")

