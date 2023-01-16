from collections import deque
def solution(q1, q2):
    q1 = deque(q1)
    q2 = deque(q2)
    max_cnt = len(q1)*3
        
    q1s = sum(q1)
    q2s = sum(q2)
    
    if q1s == q2s:
        return 0
    
    if (q1s + q2s) % 2 == 1:
        return -1
    
    avg = (q1s + q2s) // 2
    
    cnt = 0
    while q1s != q2s:
        cnt += 1
        if q1s > q2s:
            a = q1.popleft()
            q2s+= a
            q1s-= a
            q2.append(a)
            
        else :
            a = q2.popleft()
            q1s+= a
            q2s-= a
            q1.append(a)
        
        
        if max_cnt == cnt:
            return -1        
        
    return cnt

"""
3 2 7 2-> 14  18(+4) 15(-3)
4 6 5 1-> 16 12(-4) 15(3)

합/2 => 15
res = 2번

1 2 1 2     -> 6  |  7   17 16   14  13  11 10
1 10 1 2    -> 14 |  13  3   4   5   6   8 10
합 /2 = 10
res = 7

1 1 -> 2 | 3 8 7 6 5 0
1 5 -> 6 | 5 0 1 2 3 8 -> 넘어서면 안 됨
합 / 2  = 3

1 1 1 5
0


~ 20
1 2 3 4 5 : 15 -> 16 19 24 (1 2 3 4 5 1 3 5)    -> 23 21 18 (4 5 1 3 5) -> 25 (4 5 1 3 5 7)
1 3 5 7 9 : 25 -> 24 21 16 (7 9)                -> 17 19 22 (7 9 1 2 3) -> 15 (9 1 2 3)

21 16 (1 3 5 7)     -> 24 (1 3 5 7 9)
19 24 (9 1 2 3 4 5) -> 16 (1 2 3 4 5)


"""