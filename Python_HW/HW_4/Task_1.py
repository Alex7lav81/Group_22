''' Задача №1

===== Обменник =====

Создать скрипт, который будет запускаться из консоли 1 раз, выдавать результат и зарываться.
    1. На вход обменнику вводишь количество денег int.
    2. На выходе в консоль выводится ответ в таком виде:
                "Вы ввёли int (Валюта)"
                "конвертированная сумма в USD = int"
    3. Валюту пользователя определите сами.
'''


input_money_BYN = int(input("Введите сумму для конвертации: "))
input_money_USD = input_money_BYN / 2.5
print("Вы ввели ", input_money_BYN, " BYN")
print("Конвертированная сумма в USD = ", input_money_USD)