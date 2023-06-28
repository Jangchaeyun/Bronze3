from sys import stdin

for i in range(int(stdin.readline())):
    n = int(stdin.readline())
    li = [list(map(float, stdin.readline().split())) for n in range(n)]
    X = sorted(li, key=lambda x:x[0])
    Y = sorted(li, key=lambda x:x[1])
    print(f"Case {i+1}:", end=' ')
    if n == 1:
        area = 0; per = 0
    else:
        x = X[-1][0] - X[0][0]; y = Y[-1][1]-Y[0][-1]
        area = x * y
        per = 2 * (x + y)
    print(f"Area {area}, Perimeter {per}")