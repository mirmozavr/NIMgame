import time


def print_rules():
    print('''
Играем в игру!
Вытягиваем палочки по очереди
одну, две или три за ход.
Кто вытягивает последнюю палочку - проиграл!
''')


def game(count, F):
    x = [3, 1, 1,2]
    time.sleep(0.6)
    print('Палочек', count)
    while True:
        if F:
            if count == 1:
                time.sleep(0.6)
                print('Я беру последнюю палочку. Поздравляю, вы выиграли!')
                return
            else:
                take = x[count % 4]
                time.sleep(0.6)
                print('Я беру', take)
                print('Осталось', count - take)
                count -= take
                F = not F

        else:
            if count == 1:
                time.sleep(0.6)
                print('Вы берете последнюю палочку. Я выиграл!')
                return
            else:
                while True:
                    time.sleep(0.6)
                    take = input('Сколько палочек вы берете? Введите число. ')
                    if not take.isdigit() or 1 > int(take) or int(take) > 3:
                        time.sleep(0.6)
                        print('Попробуйте еще раз. Введите число от 1 до 3.')
                    elif count - int(take) < 0:
                        print('Попробуйте еще раз. Нельзя брать больше палочек, чем есть!')
                    else:
                        take = int(take)
                        if not count - take:
                            time.sleep(0.6)
                            print('Вы взяли все палочки. Я выиграл!')
                            return
                        time.sleep(0.6)
                        print('Вы берете', take)
                        print('Осталось', count - take)
                        count -= take
                        F = not F
                        break


pos = {'y', 'yes'}
neg = {'n', 'no'}

while True:
    time.sleep(0.6)
    print('Сыграем в игру?  Уes/No')
    resp = input()
    if resp.lower() in pos:
        time.sleep(0.6)
        print_rules()
        while True:
            time.sleep(0.6)
            print('Сколько палочек на старте? Введите число больше 19')
            sticks = input()
            if not sticks.isdigit() or 20 > int(sticks):
                time.sleep(0.6)
                print('Попробуйте еще раз.')
            else:
                sticks = int(sticks)
                while True:
                    time.sleep(0.6)
                    print('Вы начинаете первым? Yes/No')
                    first = input()
                    if first.lower() in pos:
                        first = False
                        break
                    elif first.lower() in neg:
                        first = True
                        break
                    else:
                        time.sleep(0.6)
                        print('Не понял. Попробуйте еще раз.')
                game(sticks, first)
                break

    elif resp.lower() in neg:
        time.sleep(0.6)
        print('До свидания')
        break
    else:
        time.sleep(0.6)
        print("Не понял. Попробуйте еще раз")
