num = int(input("Enter the number to find the number of digits it has: "))
def sum_of_digits(val: int):
    if (not val):
        print(val)
        return 0
    val = val // 10
    return sum_of_digits(val) + 1
print(f"{num} has {sum_of_digits(num)} digits.")