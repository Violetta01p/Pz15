# Створення класу банківського рахунку
class BankAccount:
    # Конструктор — задає ім’я, номер рахунку та початковий баланс
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner                  # Власник рахунку
        self.account_number = account_number  # Номер рахунку
        self.balance = balance              # Баланс

    # Метод для поповнення рахунку
    def deposit(self, amount):
        self.balance += amount
        print(f"Поповнено на {amount} грн. Новий баланс: {self.balance} грн")

    # Метод для зняття коштів з перевіркою
    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостатньо коштів!")
        else:
            self.balance -= amount
            print(f"Знято {amount} грн. Залишок: {self.balance} грн")

    # Метод для перевірки балансу
    def check_balance(self):
        print(f"Поточний баланс: {self.balance} грн")

# Приклад використання
account = BankAccount("Іван Петренко", "UA123456789", 1000)
account.check_balance()
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
