import pyfiglet
from termcolor import colored

#colored_title = colored("Calculator", "magenta", attrs=["bold"])
banner = pyfiglet.figlet_format("Calculator", font="serifcap", justify="center")
print("\033[0;32m+ \033[0;33m- \033[0;31mx \033[0;35m÷ " * 12)
print(banner)
print("\033[0;32m+ \033[0;33m- \033[0;31mx \033[0;35m÷ " * 12)
print("\033[0m")


def process():
# Ask for user's 2 input numbers.
    while True:
        num_1 = input("\033[1;33mEnter the first number: \033[4;37m")
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
            break
        except ValueError:
# Else, if theinput is neither integer nor float, print an error message.
            print("\033[0m\033[0;101m\033[1;30m⚠️   Invalid input . Please enter a valid number.\033[0m")
            continue

    while True:
        num_2 = input("\033[0m\033[1;32mEnter the second number: \033[4;37m")
        try:
# Convert the input into float data type.
            float_value = float(num_2)
# Check if the input is an integer
            if float_value.is_integer():
# If yes, convert the input to an integer
                int_value = int(float_value)
                num_2 = int_value
            else:
                num_2 = float_value
            break
        except ValueError:
# Else, if theinput is neither integer nor float, print an error message.
            print("\033[0m\033[0;101m\033[1;30m⚠️   Invalid input . Please enter a valid number.\033[0m")
            continue

# Ask for user's input for operation.
    while True:
        operation = input("\033[0m\033[1;34mPlease select an operation to perform \033[0;32m+\033[1;34m for \033[4;32maddition \033[1;34m, \033[0;33m-\033[1;34m for \033[4;33msubtraction\033[1;34m, \033[0;31m*\033[1;34m for \033[4;31mmultiplication\033[1;34m, \033[0;35m/\033[1;34m for \033[4;35mdivision\033[1;34m: \033[0m")
        print()
        import time
        import sys
        print("\033[0;100mLoading:\033[0m".center(90))
        # Make a loading animation.
        animation = ["🐣🥚🥚🥚🥚🥚🥚🥚🥚🥚]".center(70),"[🐣🐣🥚🥚🥚🥚🥚🥚🥚🥚]".center(70), "[🐣🐣🐣🥚🥚🥚🥚🥚🥚🥚]".center(70), "[🐣🐣🐣🐣🥚🥚🥚🥚🥚🥚]".center(70), "[🐣🐣🐣🐣🐣🥚🥚🥚🥚🥚]".center(70), "[🐣🐣🐣🐣🐣🐣🥚🥚🥚🥚]".center(70), "[🐣🐣🐣🐣🐣🐣🐣🥚🥚🥚]".center(70), "[🐣🐣🐣🐣🐣🐣🐣🐣🥚🥚]".center(70), "[🐣🐣🐣🐣🐣🐣🐣🐣🐣🥚]".center(70), "[🐣🐣🐣🐣🐣🐣🐣🐣🐣]".center(70)]
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n")

    
    # If the user's input for operation is +, add the 2 input numbers.
        if operation == "+":
            answer = num_1 + num_2
            print("\n\033[0;32mThe \033[1;92msum\033[0;32m of the 2 numbers: " , "\033[47m\033[1;30m", answer , "\033[0m\n")
            break
    # If the user's input for operation is -, subtract the second number from the first number.
        if operation == "-":
            answer = num_1 - num_2
            print("\n\033[0;33mThe \033[1;93mdifference\033[0;33m of the 2 numbers: " , "\033[47m\033[1;30m", answer, "\033[0m\n")
            break
    # If the user's input for operation is *, multiply the first and second input numbers.
        if operation == "*":
            answer = num_1 * num_2
            print("\n\033[0;31mThe \033[1;91mproduct\033[0;31m of the 2 numbers: " , "\033[47m\033[1;30m", answer, "\033[0m\n")
            break
    # If the user's input for operation is /, divide the first input number by the second input number.
        if operation == "/":
            try:
                answer = num_1 / num_2
                print("\n\033[0;35mThe \033[1;95mquotient \033[0;35mof the 2 numbers: " , "\033[47m\033[1;30m", answer,"\033[0m\n")
                break
            except ZeroDivisionError:
                print("Error, the number is divided by 0.\n")
                break
        else:
            print("\033[0m\033[0;101m\033[1;30m⚠️   Sorry, invalid input for opration\033[0m\n")
            continue
process()
# Ask the user if they need to use the calculator again.
while True:
    decision = input("\033[0;96mDo you want to do more calculations?  Type Yes or No: \033[4;37m")
    print("\033[0m")
    # If yes, repeat the process.
    if decision.lower() == "yes":
        print("\033[0;100mOkay, please wait for a while...\033[0m".center(90))
        
        # Make a loading animation.
        import time
        import sys
        animation = ["🌕         ]".center(70),"[🌕🌖        ]".center(70), "[🌕🌖🌗       ]".center(70), "[🌕🌖🌗🌘      ]".center(70), "[🌕🌖🌗🌘🌑     ]".center(70), "[🌕🌖🌗🌘🌑🌒    ]".center(70), "[🌕🌖🌗🌘🌑🌒   ]".center(70), "[🌕🌖🌗🌘🌑🌒🌓🌔  ]".center(70), "[🌕🌖🌗🌘🌑🌒🌓🌔 ]".center(70), "[🌕🌖🌗🌘🌑🌒🌓🌔🌕]".center(70)]
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n")
        print("\n", "\033[0;33m="*120)
        process()
    # Else, if no, end the program.
    elif decision.lower() == "no":
        print("\n\033[0;92mProcess done!")
        print("\n", "\033[0;33m="*120)
        break
    # When the input is neither yes nor no, print a message and ask again.
    else:
        print("\033[1;34mPlease type in only Yes or No.")
        continue




