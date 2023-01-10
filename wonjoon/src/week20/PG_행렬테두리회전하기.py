def solution(row, col, q):
    
    board = [[0]*col for _ in range(row)]
    answer = []
    num = 1
    for i in range(row):
        for j in range(col):
            board[i][j] = num
            num+= 1

    for a in q:
        sr,sc,er,ec = a # 좌표 받기
        arr = []        
        
        r,c = sr-1,sc-1
        start = board[sr-1][sc-1] # 시작점 빼두기
        
        for b in range(sc, ec): # 상
            c = b
            tmp = board[r][c]
            if board[r][c] != start:
                arr.append(start)    
            board[r][c] = start
            start = tmp
            
        
        for b in range(sr, er): # 우
            r = b
            tmp = board[r][c]
            if board[r][c] != start:
                arr.append(start)    
            board[r][c] = start

            start = tmp

        for b in range(ec-2, sc-2,-1): # 하
            c = b
            tmp = board[r][c]
            if board[r][c] != start:
                arr.append(start)    
            board[r][c] = start

            start = tmp

        for b in range(er-2, sr-2,-1): # 좌
            r = b
            tmp = board[r][c]
            if board[r][c] != start:
                arr.append(start)    
            board[r][c] = start

            start = tmp
            
        if len(arr) != 0:
            answer.append(min(arr))
            
    return answer