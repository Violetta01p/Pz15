# Створення класу Person
class Person:
    # Конструктор — задає ім’я, вік та місто при створенні об'єкта
    def __init__(self, name, age, city):
        self.name = name       # Зберігає ім'я
        self.age = age         # Зберігає вік
        self.city = city       # Зберігає місто

    # Метод для виводу короткої інформації
    def info(self):
        print(f"{self.name}, {self.age} років, проживає у місті {self.city}")

# Приклад використання
p1 = Person("Олена", 27, "Львів")
p1.info()
