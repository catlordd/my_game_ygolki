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
    for num in corner1:
        if num in win_player2:
            corner1.remove(num)
            print(corner1)
        if len(corner1) == 0:
            start = False
            print('Player_2 is WIN!!!')
            
    for num in corner2:
        if num in win_player1:
            corner2.remove(num)
            print(corner2)
        if len(corner2) == 0:
            start = False
            print('Player_1 is WIN!!!')
    
    
    #  
    p = 'Игрок 1' if player else 'Игрок 2'
    print_dask(dask)
    # Ввод числа и поиск его координат(x, y)
    number = int(input(f'{p} выберите число \n'))
    x,y = 0,0       
    
    
    
    while True:
        
        print_dask(dask)
        
        for y1,line in enumerate(dask):
                for x1, n  in enumerate(line): 
                    if number == n:
                        x, y = x1, y1
                        print(x, y)
                        
        # Шаг и прижок
        left_stеp, left_jump = True, True
        right_stеp, right_jump = True, True
        up_stеp, up_jump = True, True
        down_stеp, down_jump = True, True
        
        # Куда можно сделать ход, а куда нельзя
        if x == 0 or dask[y][x-1]!=0: left_stеp = False   
        if x <= 1 or dask[y][x-2]!=0: left_jump = False
        if x == 7 or dask[y][x+1]!=0: right_stеp = False    
        if x >= 6 or dask[y][x+2]!=0: right_jump = False
        
        if y == 0 or dask[y-1][x]!=0: up_stеp = False     
        if y >= 1 or dask[y-2][x]!=0: up_jump = False
        if y == 7 or dask[y+1][x]!=0: down_stеp = False     
        if y >= 6 or dask[y+2][x]!=0: down_jump = False
        
        vector = int(input(f'{p} выберите направление хода \n'))
        
        if vector == 8:
            if up_stеp:
                dask[y-1][x] = number
            elif up_jump:
                dask[y-2][x] = number
        elif vector == 2:
            if down_stеp:
                dask[y+1][x] = number
            elif down_jump:
                dask[y+2][x] = number
        elif vector == 4:
            if left_stеp:
                dask[y][x-1] = number
            elif left_jump:
                dask[y][x-2] = number
        elif vector == 6:
            if right_stеp:
                dask[y][x+1] = number
            elif right_jump:
                dask[y][x+2] = number
        
        dask[y][x] = 0
        
        if vector == 5:
            start = False
            
    
        
    
    
    # 
        
    