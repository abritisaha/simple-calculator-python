# python program to create a simple calculator

# function to add two numbers
def add(num1 , num2):
    return num1 + num2

# function to subtraction two numbers
def sub(num1 , num2):
    return num1 - num2

# function to multiplication two numbers
def multi(num1 , num2):
    return num1 * num2

# function to division two numbers
def div(num1 , num2):
    return num1 / num2

# function to avg two numbers
def avg(num1 , num2):
    return (num1 + num2) / 2
print("please select an operation \n "\
        "1. Add \n "\
        "2. Subtract \n "\
        "3. Multiply \n "\
        "4. Divide \n "\
        "5. Average \n ")
select = int(input("Select operation from 1,2,3,4,5 :"))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if select == 1:
    print(num1,"+",num2,"=", add(num1 , num2))
elif select == 2:
    print(num1,"-",num2,"=", sub(num1 , num2))
elif select == 3:
    print(num1,"*",num2,"=", multi(num1 , num2))
elif select == 4:
    print(num1,"/",num2,"=", div(num1 , num2))
elif select == 5:
    print("(",num1,"+",num2,")","/","2","=", avg(num1 , num2))
else:
    print("Invalid operation")
    
    

    




