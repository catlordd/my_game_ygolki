#
dask = [[1,3,5,0,0,0,0,0],
        [7,9,11,0,0,0,0,0],
        [13,15,17,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,2,4,6],
        [0,0,0,0,0,8,10,12],
        [0,0,0,0,0,14,16,18]]

#
player = True

#
start = True
win_player1 = [1,3,5,7,9,11,13,15,17]
win_player2 = [2,4,6,8,10,12,14,16,18]

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
    for number in corner1:
        if number in win_player2:
            corner1.remove(number)
            print(corner1)
        if len(corner1) == 0:
            start = False
            print('Player_2 is WIN!!!')
            
    for number in corner2:
        if number in win_player1:
            corner2.remove(number)
            print(corner2)
        if len(corner2) == 0:
            start = False
            print('Player_1 is WIN!!!')
    
    #  
    p = 'Игрок 1' if player else 'Игрок 2'
    
    # Ввод числа и поиск его координат(x, y)
    number = input(f'{p} выберите число \n')
    number = int(number)
    x,y = 0,0       
    
    for y1,line in enumerate(dask):
            for x1, n  in enumerate(line): 
                if number == n:
                    x, y = x1, y1
                    print(x, y)
    # Функция для преображения таблицы в более читаемый вид (str)
    def print_dask(d):
        
        for y1,line in enumerate(d):
            for x1, n  in enumerate(line): 
                n = str(n)
                n = '0'+n if len(n)==1 else n
            
                d[y1][x1] = n
        for line in d:
            print(line)    
    
    # Функция, которая показывает куда можно перемещать число
    def resolution_move(_x:int,_y:int,d):
        
        #
        left_stеp, left_jump = True
        right_stеp, right_jump = True
        up_stеp, up_jump = True
        down_stеp, down_jump = True
        
        #
        if _y == 0: 
            left_stеp = False
            left_jump = False
        if _y == 1: left_jump = False
        if _y == 7: 
            right_stеp = False
            right_jump = False
        if _y == 6: right_jump = False
        if _x == 0: 
            up_stеp = False
            up_jump = False
        if _x == 1: up_jump = False
        if _x == 7: 
            down_stеp = False 
            down_jump = False
        if _x == 6: down_jump = False 
    
    # Обратное преображение таблицы в int 
    '''for y1,line in enumerate(dask):
        for x1, n  in enumerate(line): 
            if number == n:
                x, y = x1, y1
                print(x, y)
            n = int(n)            
            dask[y1][x1] = n'''
    
    print_dask(dask)
    
    
    # 
    start = False
    