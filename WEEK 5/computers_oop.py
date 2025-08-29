class Computer: #Creating a class named Computer
# Adding attributes: brand, model, storage, price etc
    def __init__(self, brand, model, processor, ram, storage, price, battery_life, operating_system):
        self.brand = brand
        self.model = model
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.price = price
        self.battery_life = battery_life  # in percentage (0–100)
        self.operating_system = operating_system
        self.used_storage = 0  # starts with empty storage

    # Including methods for battery operations to show encapsulation
    def check_battery(self):
        print(f"Battery level: {self.battery_life}%")

    def charge_battery(self, amount):
        self.battery_life = min(100, self.battery_life + amount)
        print(f"Battery charged. Current level: {self.battery_life}%")

    def use_battery(self, amount):
        if self.battery_life - amount >= 0:
            self.battery_life -= amount
            print(f"Used {amount}%. Remaining battery: {self.battery_life}%")
        else:
            print("Battery too low! Please charge.")

# Adding inheritances for different types of computers 
# The special features show polymorphism
class Ultrabook(Computer):
    def special_feature(self):
        print(f"{self.brand} {self.model} is lightweight and ultra-portable!")

class Chromebook(Computer):
    def special_feature(self):
        print(f"{self.brand} {self.model} runs primarily on cloud apps!")

class Notebook(Computer):
    def special_feature(self):
        print(f"{self.brand} {self.model} is perfect for students and daily use.")

class Workstation(Computer):
    def special_feature(self):
        print(f"{self.brand} {self.model} is powerful for heavy workloads!")

class Business(Computer):
    def special_feature(self):
        print(f"{self.brand} {self.model} is secure and reliable for businesses.")


# Example usage
if __name__ == "__main__":
    laptop1 = Ultrabook("Dell", "XPS 13", "Intel i7", 16, 512, 1500, 80, "Windows 11")
    laptop2 = Workstation("HP", "ZBook", "Intel Xeon", 32, 1024, 2500, 100, "Windows 11")

    print(laptop1)
    laptop1.check_battery()
    laptop1.use_battery(30)
    laptop1.charge_battery(20)
        
    laptop1.special_feature()
    laptop2.special_feature()