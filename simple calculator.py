def calculator(a, b, op):

    if op == "+":
        print("sum:", a + b)

    elif op == "-":
        print("sub:", a - b)

    elif op == "*":
        print("mult:", a * b)

    elif op == "/":
        if b != 0:
            print("divi:", a / b)
        else:
            print("error!")

    else:
        print("error 1!")


# taking number from user
n1 = float(input("pls enter your first number: "))
n2 = float(input("pls enter your second number: "))
operator = input("pls enter your operation (+ , - , / , *): ")

# calling the function
calculator(n1, n2, operator)