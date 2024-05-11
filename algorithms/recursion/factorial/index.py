num = int(input("Enter the number to find the factorial: "))

def fact(num: int):
    if (num==1):
        return num
    return num * fact(num - 1)

print(f"The factorial of {num} is {fact(num)}")