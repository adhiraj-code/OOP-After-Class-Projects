class ReverseString:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return self.text[::-1]

s = ReverseString("Adhiraj")
print("Reversed String:", s.reverse())