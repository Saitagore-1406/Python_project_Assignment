print("=== calculator ===")   # display title

# function to check if input is a valid number
def check(n):
    if n == "":
        return False

    dot = 0
    i = 0

    # check for negative number
    if n[0] == "-":
        if len(n) == 1:
            return False
        i = 1

    # loop through each character
    for j in range(i, len(n)):
        if n[j] == ".":
            dot = dot + 1
            if dot > 1:
                return False
        elif n[j] < "0" or n[j] > "9":
            return False

    return True


previous_result = 0        # store last result
history_list = []          # store all results

# infinite loop
while True:
    print("\noperations: +  -  *  %  **")
    print("type 'p' to use previous result while entering numbers")
    print("type 'h' to view history")
    print("type 'c' to clear history")
    print("type 'q' to quit")

    operator = input("enter operator: ")

    # exit
    if operator == "q" or operator == "Q":
        print("exit")
        break

    # show history
    if operator == "h":
        print("history:", history_list)
        continue

    # clear history
    if operator == "c":
        history_list = []
        print("history cleared")
        continue

    # if p is typed as operator
    if operator == "p":
        print("use p only when entering numbers")
        continue

    # validate operator
    if operator != "+" and operator != "-" and operator != "*" and operator != "%" and operator != "**":
        print("invalid operator")
        continue

    # input numbers
    num1_input = input("enter first number: ")
    num2_input = input("enter second number: ")

    # use previous result
    if num1_input == "p":
        num1 = previous_result
    else:
        if check(num1_input) == False:
            print("invalid number")
            continue
        num1 = float(num1_input)

    if num2_input == "p":
        num2 = previous_result
    else:
        if check(num2_input) == False:
            print("invalid number")
            continue
        num2 = float(num2_input)

    # match case operations
    match operator:
        case "+":
            result = num1 + num2

        case "-":
            result = num1 - num2

        case "*":
            result = num1 * num2

        case "%":
            if num2 == 0:
                print("cannot divide  by zero")
                continue
            result = num1 % num2

        case "**":
            result = num1 ** num2

        case _:
            print("error")
            continue

    previous_result = result        # store last result
    history_list.append(result)     # add to history

    print("Result:", result)