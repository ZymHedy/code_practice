while 1:
    A = []
    B = []
    n, m = input().split()
    n = int(n)
    m = int(m)
    for i in input().split():
        A.append(int(i))
    for j in input().split():
        A.append(int(j))
    B = sorted(set(A))
    for b in B:
        print(b, end=' ')
