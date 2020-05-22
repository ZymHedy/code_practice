while 1:
    nm = input()
    if nm != '':
        n, m = map(int, nm.split())
        price = list(map(int, input().split()))
        store = dict()
        for p in range(m):
            name = input()
            if name in store.keys():
                store[name] += 1
            else:
                store[name] = 1
        print('store:{}',store)
        price = sorted(price)
        count = (sorted(store.values()))
        print('count:{}',count)
        minv = 0
        maxv = 0
        l = len(count)
        for i in range(l):
            maxv += count[i] * price[-l + i]
            print(maxv)
            minv += count[-i - 1] * price[i]
            print(minv)
        print(minv, maxv)
