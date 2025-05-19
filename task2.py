# Створення класу Car
class Car:
    # Конструктор — задає характеристики автомобіля
    def __init__(self, brand, model, year, color):
        self.brand = brand     # Марка
        self.model = model     # Модель
        self.year = year       # Рік випуску
        self.color = color     # Колір

    # Метод для виводу повної інформації про автомобіль
    def full_info(self):
        print(f"{self.brand} {self.model}, {self.year} року, колір: {self.color}")

    # Метод для зміни кольору
    def change_color(self, new_color):
        self.color = new_color
        print(f"Колір змінено на {self.color}")

# Приклад використання
car1 = Car("Toyota", "Corolla", 2020, "синій")
car1.full_info()
car1.change_color("чорний")
car1.full_info()
