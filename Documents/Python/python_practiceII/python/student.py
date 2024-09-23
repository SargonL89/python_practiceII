import csv

class Student:
    def __init__(self, name, city, cities):
        self.name = name
        self.cities = cities
        self.city = city

    def __str__(self):
        return f"{self.name} from {self.city}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def cities(self):
        return self._cities
    
    @cities.setter
    def cities(self, cities):
        self._cities = cities
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        if city not in self._cities:
            raise ValueError("Invalid city")
        self._city = city


def main():
    cities = load_cities("voluspa/students.csv")
    student = get_student(cities)
    print(student)


def load_cities(filename):
    cities = []
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            cities.append(row[4])
    return cities


def get_student(cities):
    name = input("Name: ")
    city = input("City: ")
    return Student(name, city, cities)

if __name__ == "__main__":
    main()
