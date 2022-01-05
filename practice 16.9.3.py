# Задание 16.9.3

# В проекте «Дом питомца» скоро появится новая услуга: электронный кошелек.
# То есть система будет хранить данные о своих клиентах и об их финансовых операциях.

# Вам нужно написать программу, обрабатывающую данные, и на выходе в консоль
# получить следующее: Клиент "Иван Петров". Баланс: 50 руб.

class Online_Wallet:
    def __init__(self, atr1, atr2, atr3):
       self.atr1 = atr1
       self.atr2 = atr2
       self.atr3 = atr3

    def get_client_balance(self):
        print(f"Клиент: ",self.atr1, self.atr2, "Баланс:", self. atr3  )

client = Online_Wallet('Иван', 'Петров', '50 руб')
client.get_client_balance()