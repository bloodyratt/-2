1 завдання:
class Zoo:
    type_of_animal = "Animal"
    total_animals = 0

    def __init__(self, name, age, can_fly=False, can_swim=False):
        self.name = name
        self.age = age
        self.can_fly = can_fly
        self.can_swim = can_swim
        Zoo.total_animals += 1

    def fly(self):
        if self.can_fly:
            print(f"{self.name} літає")
        else:
            print(f"{self.name} не вміє літати")

    def swim(self):
        if self.can_swim:
            print(f"{self.name} плаває")
        else:
            print(f"{self.name} не вміє плавати")



tiger = Zoo("Тигр", 5)
bird = Zoo("Пташка", 2, can_fly=True)
fish = Zoo("Рибка", 1, can_swim=True)
elephant = Zoo("Слон", 10)


tiger.swim()
bird.fly()
fish.swim()
elephant.fly()


print("Загальна кількість тварин:", Zoo.total_animals)



2 завдання:

class Car:
    type_of_vehicle = "Car"

    def __init__(self, brand, color, speed, is_running=False):
        self.brand = brand
        self.color = color
        self.speed = speed
        self.is_running = is_running

    def start_engine(self):
        self.is_running = True
        print(f"{self.color} {self.brand} поїхав")

    def stop_engine(self):
        self.is_running = False
        print(f"{self.color} {self.brand} зупинився")



bmw = Car("BMW", "чорний", 200)
toyota = Car("Toyota", "синій", 180)


bmw.start_engine()
toyota.start_engine()
bmw.stop_engine()
toyota.stop_engine()
