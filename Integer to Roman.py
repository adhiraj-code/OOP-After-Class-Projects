class Roman:
    def __init__(self, number):
        self.number = number

    def convert(self):
        values = [90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        roman = ""
        num = self.number

        for i in range(len(values)):
            while num >= values[i]:
                roman += symbols[i]
                num -= values[i]

        return roman

rome = int(input("Enter a number (1-99): "))

if 1 <= rome <= 99:
    obj = Roman(rome)
    print("Roman Numeral:", obj.convert())
else:
    print("Enter a number between 1 and 99.")