import csv

class Student:
    def __init__(self, name, city, cities, career=None):
        if not name:
            raise ValueError("Missing name")
        if city not in cities:
            raise ValueError("Invalid city")
        if career and career not in ["Legals", "Architecture", "Medicine", "Chemistry"]:
            raise ValueError("Invalid career")
        self.name = name
        self.city = city
        self.career = career

    def __str__(self):
        return f"{self.name} from {self.city}" 
    
    def studies(self):
        match self.career:
            case "Legals":
                return "⚖️"
            case "Architecture":
                return "⚒️" 
            case "Medicine":
                return "🩺" 
            case "Chemistry": 
                return "🧪"



def main():
    cities = load_cities("voluspa/students.csv")
    student = get_student(cities)
    print(student.studies())


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
    career = input("Career: ") or None
    return Student(name, city, cities, career)

if __name__ == "__main__":
    main()
