while True: # loop until valid input
    try:
        a = int(input("pls Enter number a (which should be int!): "))
        b = int(input("pls Enter number b (which should be int!): "))

        if b > a:
            print(f"{a} Is greater than {b}")
        elif b == a:
            print(f"{a} and {b} are equal!")
        else:
            print(f"{a} is smaller than {b}")

        break  #if anything is right get out of the loop

    except ValueError:
        print("Error: Please enter a valid integer number! (No decimals or letters allowed)\nTry again...\n")
