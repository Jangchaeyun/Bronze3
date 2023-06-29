from sys import stdin

K = int(stdin.readline())
N = int(stdin.readline())
bomb_time = 210
accum_time = 0
for i in range(N):
    T, Z = stdin.readline().rstrip().split(' ')
    T = int(T)
    
    accum_time += T

    if bomb_time <= accum_time:
        print(K)
        break
    if Z == 'T':
        K += 1
    
    if K == 9:
        K = 1