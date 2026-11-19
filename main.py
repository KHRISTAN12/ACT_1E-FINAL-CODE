# KHRISTAN AMIEL G. MANARANG
# ACT 1E

def pause():
    input("\nPress ENTER to continue...")

def lesson1():

    print("\n================================")
    print("LESSON 1: INTRODUCTION TO PROGRAMMING")
    print("================================")

    print("""
WHAT IS PROGRAMMING?

Programming is the process of writing instructions
that tell a computer what to do.

WHAT IS PYTHON?

Python is a high-level programming language.
It is easy to understand and commonly used for:

1. Web development
2. Game development
3. Data analysis
4. Artificial Intelligence
5. Automation

HOW DOES PROGRAMMING WORK?

Step 1: Identify the problem.
Step 2: Plan the solution.
Step 3: Write the code.
Step 4: Run the program.
Step 5: Check and fix errors.

FIRST PYTHON PROGRAM:

Code:
print("Hello, Mga Pogi!")

Expected Output:
Hello, Mga Pogi!

EXPLANATION:
The print() function displays text on the screen.
""")

    pause()

def lesson2():

    print("\n================================")
    print("LESSON 2: PYTHON BASIC SYNTAX")
    print("================================")

    print("""
WHAT IS SYNTAX?

Syntax refers to the rules used when writing
a Python program.

1. VARIABLES
Variables store information.

Example:
name = "Khristan"
age = 20

2. COMMENTS
Comments explain the code.

Example:
# This is a comment

3. INDENTATION
Indentation means adding spaces before a line
of code to organize code blocks.

4. STRINGS
Strings are text enclosed in quotation marks.

Example:
name = "Python"

5. CASE SENSITIVITY
Python distinguishes uppercase and lowercase letters.

Example:
Name = "Lawrence"
name = "Mark"

These are two different variables.
""")

    pause()

def lesson3():

    print("\n================================")
    print("LESSON 3: ARITHMETIC OPERATORS")
    print("================================")

    print("""
WHAT ARE ARITHMETIC OPERATORS?

These are symbols used to perform
mathematical calculations.

OPERATORS:

+  Addition
-  Subtraction
*  Multiplication
/  Division
%  Modulus
** Exponent
// Floor Division

EXAMPLE:

a = 15
b = 5

a + b = 20
a - b = 10
a * b = 75
a / b = 3
a % b = 0
a ** b = 759375
a // b = 3

EXPRESSIONS:

An expression combines values and operators.

Example:
result = (10 + 5) * 2

Expected Output:
30
""")

    pause()

def lesson4():

    print("\n================================")
    print("LESSON 4: BASIC INPUT AND OUTPUT")
    print("================================")

    print("""
WHAT IS INPUT?

Input allows the user to enter information.

Syntax:
input("Enter something: ")

WHAT IS OUTPUT?

Output displays information on the screen.

Syntax:
print("Hello")

TYPE CONVERSION:

int()   - Converts into integer.
float() - Converts into decimal.
str()   - Converts into string.

EXAMPLE:

age = int(input("Enter age: "))
print("Your age is", age)

EXPECTED OUTPUT:

Enter age: 20
Your age is 20
""")

    pause()

def lesson5():

    print("\n================================")
    print("LESSON 5: CONDITIONAL STATEMENTS")
    print("================================")

    print("""
WHAT ARE CONDITIONAL STATEMENTS?

Conditional statements allow a program
to make decisions based on conditions.

TYPES:

1. IF
Executes code when a condition is true.

2. ELIF
Checks another condition if the previous
condition was false.

3. ELSE
Executes when all previous conditions are false.

SYNTAX:

if condition:
    statement

elif condition:
    statement

else:
    statement

EXAMPLE:

grade = 90

if grade >= 75:
    print("Passed")
else:
    print("Failed")

EXPECTED OUTPUT:
Passed
""")

    pause()

def lesson6():

    print("\n================================")
    print("LESSON 6: LOGICAL OPERATORS")
    print("================================")

    print("""
WHAT ARE LOGICAL OPERATORS?

Logical operators combine or reverse
conditional statements.

THREE TYPES:

1. AND
Returns True when BOTH conditions are true.

2. OR
Returns True when AT LEAST ONE condition is true.

3. NOT
Reverses the result of a condition.

EXAMPLES:

AND:
True and True = True

OR:
True or False = True

NOT:
not True = False

PYTHON SYNTAX:

age >= 18 and grade >= 75
age >= 18 or grade >= 90
not(age >= 18)
""")

    pause()

def lesson7():

    print("\n================================")
    print("LESSON 7: ITERATION AND LOOPS")
    print("================================")

    print("""
WHAT IS ITERATION?

Iteration is the process of repeating
a set of instructions.

WHAT IS A LOOP?

A loop allows a program to execute
the same code multiple times.

TYPES OF LOOPS:

1. FOR LOOP
Repeats code for each item in a sequence.

SYNTAX:

for number in range(1, 6):
    print(number)

EXPECTED OUTPUT:
1
2
3
4
5

2. WHILE LOOP
Repeats code while a condition is true.

SYNTAX:

number = 1

while number <= 5:
    print(number)
    number += 1

EXPECTED OUTPUT:
1
2
3
4
5

OTHER LOOP CONTROLS:

BREAK - Stops the loop.
CONTINUE - Skips the current iteration.
""")

    pause()

while True:

    print("\n============================================")
    print("          PYTHON TUTORIAL SYSTEM")
    print("============================================")

    print("1. Introduction to Programming")
    print("2. Python Basic Syntax")
    print("3. Arithmetic Operators and Expressions")
    print("4. Basic Input and Output in Python")
    print("5. Conditional Statements in Python")
    print("6. Logical Operators")
    print("7. Introduction to Iteration and Loops")

    print("--------------------------------------------")
    print("0. Exit")
    print("============================================")

    choice = input("Choose your lesson (0-7): ")

    if choice == "1":
        lesson1()

    elif choice == "2":
        lesson2()

    elif choice == "3":
        lesson3()

    elif choice == "4":
        lesson4()

    elif choice == "5":
        lesson5()

    elif choice == "6":
        lesson6()

    elif choice == "7":
        lesson7()

    elif choice == "0":
        print("\nThank you pogi for studying Python!")
        print("Keep practicing and learning!")
        break

    else:
        print("\nInvalid selection. Please try again.")
