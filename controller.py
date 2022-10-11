import txt_base as tb
import gui, main


dict_command = {'1': gui.scan, '2': main.search, '3': main.entry, '4': main.delete_line, '0': quit}
while True:
    gui.start_print()
    command = input('Команда: > ')
    if command in dict_command:
        dict_command[command](tb.data)
    else:
        print('COMMAND ERROR!!!')