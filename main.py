import txt_base as tb
import gui
def search(data):
    dict_search = {'1': search_firstname, '2': search_secondname, '3': search_number, '0': quit}

    while True:
        gui.search_menu()
        command = input('Команда: > ')
        if command == '9':
            break
        elif command in dict_search:
            dict_search[command](data)
        else:
            print(' COMMAND ERROR!!!')


def entry(firstname, secondname, number, other):     #для добавления данных
    firstname = input('Введите Имя: ')
    secondname: str = input('Введите Фамилию: ')
    number = input('Телефон: ')
    other = input('Описание: ')
    with open('contacts.txt', 'a') as file:
        file.write(f'{firstname} {secondname} {number} {other}')
    

def quit(data):       #для выхода
    gui.sys.exit()

def scan(data):       #сканирует файл и выводит
    for i in data:
        print(i)


def search_firstname(data):           #поиск по имени и вывод с индексом
    find = input('Введите Имя: ')
    index = 0
    dict_change = {'1': search_firstname, '2': search_secondname, '3': search_number,
                    '4': delete_line, '0': quit}
    for line in data:
        if find in line:
            print(f'{index} {line}')

        with open('contacts.txt', 'w') as file:
            for lin in line:
                file.write(lin)


            gui.change_menu()
            command = input('Команда: > ')
            if command == '9':
                break
            elif command in dict_change:
                dict_change[command](data)
            else:
                print(' COMMAND ERROR!!!')


def search_secondname(data):          #поиск по фамилии и вывод
    find = input('Введите Фамилию: ')
    index = 0
    dict_change = {'1': search_firstname, '2': search_secondname, '3': search_number,
                    '8': delete_line, '0': quit}
    for line in data:
        if find in line:
            print(f'{index} {line}')
            index += 1
            gui.change_menu()
            command = input('Команда: > ')
            if command == '9':
                break
            elif command in dict_change:
                dict_change[command](data)
            else:
                print(' COMMAND ERROR!!!')



def search_number(data):             #поиск по номеру телефона
    find = input('Введите Номер: ')
    index = 0
    for line in data:
        if find in line:
            print(f'{index} {line}')
            index += 1

def delete_line(data):
    dict_change = {'1': search_firstname, '2': search_secondname, '3': search_number,
                    '4': delete_line, '0': quit}
    
    # filename = input('name:')
    line_name = int(input('Line:'))
    with open('contacts.txt', 'r') as file:
        lines = file.readlines()

    if(line_name <= len(lines)):
        del lines[line_name - 1]

        with open('contacts.txt', 'w') as file:
            for i in lines:
                file.write(i)
                print(i)
                gui.change_menu()
                command = input('Команда: > ')
                if command == '9':
                    break
                elif command in dict_change:
                    dict_change[command](data)
                else:
                    print('COMMAND ERROR!!!')