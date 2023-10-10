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
    
    # Ввод числа и поиск его координат
    number = input(f'{p} выберите число \n')
    number = int(number)
    x,y = 0,0       
    
    
    # Преображение таблицы в более читаемый вид (str) 
    for y1,line in enumerate(dask):
        for x1, n  in enumerate(line): 
            if number == n:
                x, y = x1, y1
                print(x, y)
            
            n = str(n)
            n = '0'+n if len(n)==1 else n
            
            dask[y1][x1] = n
            
    # 
    start = False
    for line in dask:
        print(line)
    
    # Обратное преображение таблицы в int 
    for y1,line in enumerate(dask):
        for x1, n  in enumerate(line): 
            if number == n:
                x, y = x1, y1
                print(x, y)
            n = int(n)            
            dask[y1][x1] = n
    
    for line in dask:
        print(line)
    