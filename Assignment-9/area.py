import math

# ---------------- Area Functions ----------------

def area_circle(radius):
    return math.pi * radius ** 2


def area_rectangle(length, width):
    return length * width


def area_residential(length, width):
    return length * width


# ---------------- Main Program ----------------

def main():
    print("===== AREA CALCULATOR =====")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Residential Room")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        radius = float(input("Enter radius: "))
        print("Area of Circle =", area_circle(radius))

    elif choice == 2:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print("Area of Rectangle =", area_rectangle(length, width))

    elif choice == 3:
        length = float(input("Enter room length: "))
        width = float(input("Enter room width: "))
        print("Area of Residential Room =", area_residential(length, width))

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()