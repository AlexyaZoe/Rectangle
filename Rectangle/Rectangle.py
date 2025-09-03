class Rectangle:
    def __init__(self, height, width):
        self.height = int(height)
        self.width = int(width)
    def perimeter(self):
        return 2 * (self.height + self.width)
    def area(self):
        return self.height * self.width
    def display(self):
        print("\nRectangle Calculator Details:")
        print(f"Height: {self.height}")
        print(f"Width : {self.width}")
        print(f"Perimeter: {self.perimeter()}")
        print(f"Area : {self.area()}")

        print("Rectangle Calculator Shape:")

        for row in range(int(self.height)):
            if row == 0 or row == self.height - 1:
                print('*' * self.width)
            else:
                print('*' + ' ' * (2 * self.width - 3) + '*')
def main():
    print(" Welcome to the Rectangle Calculator ")

    height = float(input("Enter the height of your rectangle: "))
    width = float(input("Enter the width of your rectangle: "))

    rect = Rectangle(height, width)
    rect.display()

if __name__=="__main__":
    main()