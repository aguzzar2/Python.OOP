import random
class Hitchhiker:

    planets = ["Antares", "Damogren", "Eadrax", "Earth", "Betelgeuse Seven"]
    locations = ["Vogon Constructor Fleet", "Damogren", "Heart of Gold"]
    people = ["Zaphod", "Trillion", "Arthur", "Ford", "Marvin", ""]
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hitchhiker {self.name}"
    
    @classmethod
    def escape(cls, name):
        cls.name = name
        print(f"{cls.name} is escaping from {random.choice(cls.locations)} to {random.choice(cls.planets)}")

Hitchhiker.escape("Ford")



# if __init__ == "__main__":
#     main()

