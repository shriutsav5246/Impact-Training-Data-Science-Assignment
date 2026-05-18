print("Method 1: Using for loop")
for i in range(5, 51, 5):
    print(i, end=" ")

print("\n")

print("Method 2: Using while loop")
num = 5
while num <= 50:
    print(num, end=" ")
    num += 5

print("\n")

print("Method 3: Using list comprehension")
multiples = [i for i in range(5, 51) if i % 5 == 0]
print(multiples)