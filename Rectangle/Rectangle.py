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
        print(f"Height:     {self.height}")
        print(f"Width :     {self.width}")
        print(f"Perimeter:  {self.perimeter()}")
        print(f"Area :      {self.area()}")
        
        if self.height == 1:
            print('* ' * self.width)
        elif self.width == 1:
            for _ in range(self.height):
                print('*')
        else:
            print('* ' * self.width)
            for _ in range(self.height - 2):
                print('*' + ' ' * (2 * self.width - 3) + '*')
                
            print('* ' * self.width)


def main():
    print(" Welcome to the Rectangle Calculator ")

    while True:
        height = float(input("Enter the height of your rectangle: "))
        width = float(input("Enter the width of your rectangle: "))

        rect = Rectangle(height, width)
        rect.display()

        choice = input("\nWould you like to continue? (y/n): ").strip().lower()
        if choice != 'y':
           print(" Thank you for using the Rectangle Calculator. ")
           break
if __name__=="__main__":
    main()