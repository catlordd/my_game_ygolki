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
def print_dask(dd:list):
    
    d = []
    
    for y1,line in enumerate(dd):
        d.append([])
        for x1, n  in enumerate(line): 
            d[y1].append(n)
    
    for y1,line in enumerate(d):
        for x1, n  in enumerate(line): 
            n = str(n)
            n = '0'+n if len(n)==1 else n
            
            d[y1][x1] = n
    for line in d:
        print(line)

#
player = True

# Массивы из чисел для игроков
start = True
win_player1 = [1,3,5,7,9,11,13,15,17]
win_player2 = [2,4,6,8,10,12,14,16,18]
win_player = []
#
while(start):
    
    # Списки цифр углах
    corner1 = [dask[0][0],dask[0][1],dask[0][2],
               dask[1][0],dask[1][1],dask[1][2],
               dask[2][0],dask[2][1],dask[2][2]]
    
    corner2 = [dask[5][5],dask[5][6],dask[5][7],
               dask[6][5],dask[6][6],dask[6][7],
               dask[7][5],dask[7][6],dask[7][7]] 
    
    # Условие победы
    for num in corner1:
        if num in win_player2:
            corner1.remove(num)
            print(corner1)
        if len(corner1) == 0:
            start = False
            print('Игрок 2 выйграл!!!')
            
    for num in corner2:
        if num in win_player1:
            corner2.remove(num)
            print(corner2)
        if len(corner2) == 0:
            start = False
            print('Игрок 1 выйграл!!!')
    
    
    # Присваевание переменным номера игрока и соответсвующего ему списка чисел
    p = 'Игрок 1' if player else 'Игрок 2'
    win_player = win_player1 if player else win_player2
    print_dask(dask)
    
    # Ввод числа и поиск его координат(x, y)
    number = input(f'{p} выберите число \n')
    if number == '':
        moving = False
        print("Ощибка: вы не ввели число")
        continue
    number = int(number)
    x,y = 0,0
    
    # Проверка: выбранное число из списка чисел для этого игрока?       
    if number in win_player:
        moving = True
    else:
        moving = False
        print("Ощибка: вы выбрали число не из вашего набора")
    
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
                        
        # Переменные для прижов
        left_jump, right_jump, up_jump, down_jump = True, True, True, True
        
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
        
        # Вызываем ошибку если некуда делать ход
        if left_stеp == False and \
            left_jump == False and \
            right_stеp == False and \
            right_jump == False and \
            up_stеp == False and \
            up_jump == False and \
            down_stеp == False and \
            down_jump == False:
                print("Ощибка: вы выбрали число, которому некуда делать ход")
                moving = False
                break
        
        # Выбор направления хода
        vector = input(f'{p} выберите направление хода \n')
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
