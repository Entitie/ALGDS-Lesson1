# 5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

alf = input('В каком алфавите будем искать букву(Ru/En)? ').lower()
letter1, letter2 = input('Введите первую букву: ').upper(), input('Введите вторую букву: ').upper()

if alf == 'ru':
    letter1 = ord(letter1) - ord("А") + 1
    letter2 = ord(letter2) - ord("А") + 1
elif alf == 'en':
    letter1 = ord(letter1) - ord("A") + 1
    letter2 = ord(letter2) - ord("A") + 1

print(f'Первая буква стоит под номером {letter1}')
print(f'Вторая буква стоит под номером {letter2}')
print(f'Количество букв между ними равно {abs(letter1 - letter2) - 1}')
