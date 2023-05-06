# Ask for user's 2 input numbers.
num_1 = input("Enter the first number: ")
try:
# Convert the input into float data type.
    float_value = float(num_1)
# Check if the input is an integer
    if float_value.is_integer():
# If yes, convert the input to an integer
        int_value = int(float_value)
        num_1 = int_value
    else:
        num_1 = float_value
except ValueError:
# Else, if theinput is neither integer nor float, print an error message.
    print("Invalid input. Please enter a valid number.")

num_2 = input("Enter the second number: ")
try:
# Convert the input into float data type.
    float_value = float(num_2)
# Check if the input is an integer
    if float_value.is_integer():
# If yes, convert the input to an integer
        int_value = int(float_value)
        num_2 = int_value
    else:
        num_1 = float_value
except ValueError:
# Else, if theinput is neither integer nor float, print an error message.
    print("Invalid input. Please enter a valid number.")

# Ask for user's input for operation.
while True:
    operation = input("\nPlease select an operation to perform + for addition, - for subtraction, * for multiplication, / for division: ")
    # If the user's input for operation is +, add the 2 input numbers.
    if operation == "+":
        answer = num_1 + num_2
        print("\nThe sum of the 2 numbers: " , answer , "\n")
        break
    # If the user's input for operation is -, subtract the second number from the first number.
    if operation == "-":
        answer = num_1 - num_2
        print("\nThe difference of the 2 numbers: " , answer , "\n")
        break
    # If the user's input for operation is *, multiply the first and second input numbers.
    if operation == "*":
        answer = num_1 * num_2
        print("\nThe product of the 2 numbers: " , answer , "\n")
        break
    # If the user's input for operation is /, divide the first input number by the second input number.
    if operation == "/":
        try:
            answer = num_1 / num_2
            print("\nThe quotient of the 2 numbers: " , answer ,"\n")
            break
        except ZeroDivisionError:
            print("Error, the number is divided by 0.\n")
            break
    else:
        print("Sorry, invalid input for opration\n")
        continue


# Ask the user if they need to use the calculator again.
# If yes, repeat the process.
# Else, if no, end the program.


