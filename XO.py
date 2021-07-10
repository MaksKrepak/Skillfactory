field = [i for i in range(1,10)] # заполняем ячейки поля координатами
def draw(field): # ф-я рисования поля
    print("-------------")
    for i in range(3): # заполняем ячеки цифрами 1-9
        print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
        print("-------------")
draw(field)

def check_win(field): # ф-я проверки выигрышных комбинаций
    win_comb = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)) # набор выигрышных комбинаций
    for each in win_comb: # проверяем заполненные ячейки на совпадение с выигрышными комбинациями
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]] # возвращаем Х или О, в зависимости от того, чья комбинация выигрышная
    return False

def move(field):
    n = 1 # задаем счетчик ходов
    while True: # запускаем бесконечный цикл
        move = input("take your move:")
        if (move.isdigit()) and (1 <= int(move) <= 9): # проверяем, что введана цифра и она из диап. 1-9
            move = int(move) # преобразуем в целочисленный (а то ругается)
            if str(field[move-1]) in "XO": # проверяем не занята ли ячейка
                print("the place is taken, try again")
                n -= 1 # уменьшаем счетчик, чтобы не сбилась последовательность Х и О
            if n % 2 != 0: # задаем последовательность Х и О: на чет/не чет
                field[move-1] = str("X") # заносим в список Х, если не чет
            else:
                field[move-1] = str("O") # заносим в список О, если чет
            if n > 4: # с 5го хода начинаем проверять выигрышные комбинации
                winner = check_win(field)
                if winner:
                    print(winner, "выиграл!")
                    draw(field) # рисуем финальное поле
                    break # прерываем цикл
            if n == 9: # если никто не выиграл, а все ячейки поля заполнены, то "ничья"
                print("Ничья!")
                draw(field)  # рисуем финальное поле
                break  # прерываем цикл
            n += 1
            draw(field) # рисуем текущее поле
        else:
            print("enter the number from 1 to 9")

move(field)