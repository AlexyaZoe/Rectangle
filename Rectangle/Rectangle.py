class Rectangle:
    def__init__(self, height, width):
        self.height = height
        self.width = width
    def perimeter(self):
        return 2 * (self.height + self.width)
    def area(self):
        return self.height + self.width)
    def area(self):
        return self.height * self.width
    def display(self):
        print("\nRectangle Calculator Details:")
        print(f"Height: {self.height}")
        print(f"Width : {self.width}")
        print(f"Perimeter: {self.perimeter()}")
        print(f"Area : {self.area()}")
def main():
    print(" Welcome to the Rectangle Calculator ")

    height = float(input("Enter the height of your rectangle: "))
    width = float(input("Enter the width of your rectangle: "))

    rect =Rectangle(height, width)
    rect.display()

if __name__=="__main__":
    main()