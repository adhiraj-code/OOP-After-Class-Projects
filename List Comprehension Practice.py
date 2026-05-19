num = int(input("Enter a number: "))

odd_numbers = [x for x in range(num) if x % 2 != 0]

print("Odd numbers:", odd_numbers)

fruits = ["apple", "banana", "mango", "orange", "grapes"]

fruits2 = [fruit.capitalize() for fruit in fruits]

print("fruits list:", fruits2)