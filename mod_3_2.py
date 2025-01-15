# Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
#
# Внутри функции реализовать следующую логику:
#
# Проверка на корректность e-mail отправителя и получателя.
# Проверка на отправку самому себе.
# Проверка на отправителя по умолчанию.
# Пункты задачи:
#
# Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение),
#   recipient(получатель) и 1 обязательно именованный аргумент со значением
#   по умолчанию sender = "university.help@gmail.com".
# Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
#   то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
# Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
# Если же отправитель по умолчанию - university.help@gmail.com,
#   то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
# В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!
#   Письмо отправлено с адреса <sender> на адрес <recipient>."
# Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
# За один вызов функции выводится только одно из перечисленных уведомлений! Проверки перечислены по мере выполнения.


import re
def check_adres(adres):
    patern = r'[\w\.-]+@\w+\.\w+'  # шаблон адреса электронной почты
    if re.search(patern, adres):
        return True
    return False


def send_email(message, recipient, sender = "university.help@gmail.com"):
    # if @ not in recipient:
    #     print(f"Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>")
    # if  not in recipient.endswich(".com" or ".ru" or ".net")
    if check_adres(recipient) and check_adres(sender):
        if recipient == sender:
            print('\033[30;43m Письмо отправленно самому себе!\033[0m')

        print(f'\033[32mПисьмо отправлено успешно\033[0m\n\t от \t{sender}\t кому \t{recipient}')
        # print(f'письмо отправить не возможно\n\tадрес получателя {recipient} не корректен.')

    elif not check_adres(sender):
       print(f'\033[31m письмо отправить не возможно\033[0m\n\tадрес отправителя {sender} не корректен')

    elif not check_adres(recipient):
       print(f'\033[31m письмо отправить не возможно\033[0m\n\tадрес получателя {recipient} не корректен')

    # else:
    #    print(f'Письмо отправлено успешно\n\t от \t{sender}\tдо \t{recipient}')


text_message = 'ПРИВЕТ' # не придумал куда воткнуть

to_adres_1 = 'anything_1@unigum.education' # input('введите адрес получастеля')
to_adres_2 = 'anything_2#unigum.education'
to_adres_3 = "university.help@gmail.com"
to_adres_4 = 'anything_2@unigum.education'
# from_adres = input('введите адрес отправителя')

from_adres = "university.helpATgmail.com"
print()
print('отправка письмо 1:')
print(f'\n\t{send_email(text_message, to_adres_1, from_adres)}')
print()
print('отправка письмо 2:')
print(f'\n\t{send_email(text_message, to_adres_2)}')
print()
print('отправка письмо 3:')
print(f'\n\t{send_email(text_message, to_adres_3)}')
print()
print('отправка письмо 4:')
print(f'\n\t{send_email(text_message, to_adres_4)}')
print()