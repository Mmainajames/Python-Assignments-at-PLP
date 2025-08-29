# Using Vehicle as the Base Class
class Vehicle:
    def move(self):
        # This will be overridden by child classes
        pass


# Derived Classes for different vehicle types
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

# Function to demonstrate polymorphism
def vehicle_move(vehicle):
    vehicle.move()  # Calls the appropriate move method based on the object type  


# Example usage of Polymorphism
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat(), Bicycle()]

    for v in vehicles:
        v.move()  # Each calls its own version of move()