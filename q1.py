def add_numbers(num1, num2):
    return num1 + num2
def process_list(user_list, num1, num2):
    if len(user_list) == 0:
        print("List is empty")
        return
    middle_index = len(user_list) // 2
    middle_value = user_list[middle_index]

    total = add_numbers(num1, num2)

    print("Sum of two numbers:", total)
    print("Middle value of list:", middle_value)

    if total > middle_value:
        result = set(user_list[:middle_index + 1])
        print("Output (Set):", result)

    elif total == middle_value:
        result = {middle_index: middle_value}
        print("Output (Dictionary):", result)

    else:
        result = tuple(user_list[middle_index + 1:])
        print("Output (Tuple):", result)
# Input
user_list = list(map(int, input("Enter list elements separated by space: ").split()))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
process_list(user_list, num1, num2)