from termcolor import colored, cprint

# Правила игры
print("Правила игры:\n\
Два игрока. Первый игрок управляет нечетными числами, второй четными.\n\
Побеждает тот, кто сможет первым переместить свои числа\n\
в противоположный угол.\n\
Игроки ходят по очереди. За один ход можно переместить одно число.\n\
Порядок хода:\n\
1) Выбираете число\n\
2) Выбираете направление хода с помощью Num-клавиатуры\n\
(влево - 4, вправо - 6, вверх - 8, вниз - 2).\n\
Число может шагнуть на соседнюю клетку, если там '00'\n\
или может перепрыгнуть через любое число кроме '00'\n\
3) Чтобы закончить ход введите '5', или ход закончится автоматически,\
если вы переместили чисто просто на соседнюю клетку")
input('Если готовы, нажмите "Enter"')


# Массив из чисел для игральной доски
dask = [[1,3,5,0,0,0,0,0],
        [7,9,11,0,0,0,0,0],
        [13,15,17,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,2,4,6],
        [0,0,0,0,0,8,10,12],
        [0,0,0,0,0,14,16,18]]

# Функция для отрисовки игральной доски
def print_dask(dd:list, select_num = '0'):
    select_num = '0'+select_num if len(select_num)==1 else select_num
    d = []
    for y1,line in enumerate(dd):
        d.append([])
        for x1, n  in enumerate(line): 
            d[y1].append(n)
    #  Массив для хранения цветов
    color_list = [[],[],[],[],[],[],[],[]]
            
    for y1,line in enumerate(d):
        for x1, n  in enumerate(line): 
            n = str(n)
            n = '0'+n if len(n)==1 else n
            d[y1][x1] = n
            
            if n == '00': color_list[y1].append('white')
            elif n == select_num: color_list[y1].append('yellow')
            elif n in ['01','03','05','07','09','11','13','15','17']: color_list[y1].append('red')
            elif n in ['02','04','06','08','10','12','14','16','18']: color_list[y1].append('green')
            
    for line, color_line in zip(d, color_list): 
        print(colored(line[0], color_line[0]),colored(line[1], color_line[1]),\
            colored(line[2], color_line[2]),colored(line[3], color_line[3]),\
            colored(line[4], color_line[4]),colored(line[5], color_line[5]),\
            colored(line[6], color_line[6]),colored(line[7], color_line[7]))

# Переменная для выбора игрока
player = True

# Массивы из чисел для игроков
start = True
win_player1 = [1,3,5,7,9,11,13,15,17]
win_player2 = [2,4,6,8,10,12,14,16,18]
win_player = []
#
while(start):
    
    # Присваивание переменным соответсвующего им номера игрока, цвета и списка чисел
    p = 'Игрок 1' if player else 'Игрок 2'
    p_color = 'red' if player else 'green'
    win_player = win_player1 if player else win_player2
    print_dask(dask)
    
    # Ввод числа и поиск его координат(x, y)
    number = input(colored(p,p_color)+' выберите число \n')
    if number == '':
        moving = False
        print("Ошибка: вы не ввели число")
        continue
    number = int(number)
    x,y = 0,0
    
    # Проверка: выбранное число из списка чисел для этого игрока?       
    if number in win_player:
        moving = True
    else:
        moving = False
        print("Ошибка: вы выбрали число не из вашего набора")
    
    # Переменные для шагов
    left_stеp, right_stеp, up_stеp, down_stеp = True, True, True, True
    
    while moving:
        
        print_dask(dask)
        
        # Цикл для поиска координат выбранного числа
        for y1,line in enumerate(dask):
                for x1, n  in enumerate(line): 
                    if number == n:
                        x, y = x1, y1
                        #print(x, y)
                        
        # Переменные для прыжков
        left_jump, right_jump, up_jump, down_jump = True, True, True, True
        try:
            # Куда можно сделать ход, а куда нельзя
            if x == 0 or dask[y][x-1]!=0: left_stеp = False   
            if x <= 1 or dask[y][x-2]!=0: left_jump = False
            if x == 7 or dask[y][x+1]!=0: right_stеp = False    
            if x >= 6 or dask[y][x+2]!=0: right_jump = False
        
            if y == 0 or dask[y-1][x]!=0: up_stеp = False     
            if y <= 1 or dask[y-2][x]!=0: up_jump = False
            if y == 7 or dask[y+1][x]!=0: down_stеp = False     
            if y >= 6 or dask[y+2][x]!=0: down_jump = False
        
            if dask[y][x-1]==0: left_jump = False
            if dask[y][x+1]==0: right_jump = False
            if dask[y-1][x]==0: up_jump = False
            if dask[y+1][x]==0: down_jump = False
        except IndexError:
            pass
        
        # Вызываем ошибку если некуда делать ход
        if left_stеp == False and \
            left_jump == False and \
            right_stеp == False and \
            right_jump == False and \
            up_stеp == False and \
            up_jump == False and \
            down_stеp == False and \
            down_jump == False:
                print("Ошибка: вы выбрали число, которому некуда делать ход")
                moving = False
                break
        
        # Выбор направления хода
        vector = input(colored(p,p_color)+' выберите направление хода \n')
        if vector not in ['8','2','4','6','5'] or vector == '':
            print("Нет такого направления хода")
            continue
        
        # Функция для шагов
        def step_False():
            global left_stеp
            global right_stеp
            global up_stеp
            global down_stеp
            left_stеp = False
            right_stеp = False
            up_stеp = False
            down_stеp = False
        
        # Алгоритм хода
        vector = int(vector)
        if vector == 8:
            if up_stеp:
                dask[y-1][x] = number
                dask[y][x] = 0
                moving = False
                player = not player
            elif up_jump:
                dask[y-2][x] = number
                dask[y][x] = 0
                step_False()
        elif vector == 2:
            if down_stеp:
                dask[y+1][x] = number
                dask[y][x] = 0
                moving = False
                player = not player
            elif down_jump:
                dask[y+2][x] = number
                dask[y][x] = 0
                step_False()
        elif vector == 4:
            if left_stеp:
                dask[y][x-1] = number
                dask[y][x] = 0
                moving = False
                player = not player
            elif left_jump:
                dask[y][x-2] = number
                dask[y][x] = 0
                step_False()
        elif vector == 6:
            if right_stеp:
                dask[y][x+1] = number
                dask[y][x] = 0
                moving = False
                player = not player
            elif right_jump:
                dask[y][x+2] = number
                dask[y][x] = 0
                step_False()
    
        if vector == 5:
            moving = False
            player = not player
    # Списки цифр в углах
    corner1 = [dask[0][0],dask[0][1],dask[0][2],
               dask[1][0],dask[1][1],dask[1][2],
               dask[2][0],dask[2][1],dask[2][2]]
    
    corner2 = [dask[5][5],dask[5][6],dask[5][7],
               dask[6][5],dask[6][6],dask[6][7],
               dask[7][5],dask[7][6],dask[7][7]] 
    
    # Условие победы
    win_p1 = 0
    win_p2 = 0
    
    for num in corner1:
        if num in win_player2:
            win_p2 += 1
        else:
            break       
    for num in corner2:
        if num in win_player1:
            win_p1 += 1
        else:
            break
    
    if win_p1 == 9: 
        print(colored('Игрок 1 выйграл!!!', 'red'))
        start = False
    elif win_p2 == 9: 
        print(colored('Игрок 2 выйграл!!!', 'green'))
        start = False