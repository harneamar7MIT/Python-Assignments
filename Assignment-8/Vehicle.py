# ---------------- Base Class ----------------
class Vehicle:
    def move(self):
        print("Vehicle is moving")


# ---------------- Subclass: Car ----------------
class Car(Vehicle):
    def move(self):
        print("Driving on the road")


# ---------------- Subclass: Bicycle ----------------
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")


# ---------------- Main Program ----------------
if __name__ == "__main__":

    car = Car()
    bicycle = Bicycle()

    # Demonstrating Polymorphism
    vehicles = [car, bicycle]

    print("Demonstrating Polymorphism:\n")

    for vehicle in vehicles:
        vehicle.move()