# 汉明距离
while 1:
    n = int(input())
    nums = list(map(int, input().split()))

    n_bin = []
    while n > 0:
        temp = n % 2
        n_bin.append(temp)
        n = n // 2
    print(n_bin)

    nums_bin = dict()
    for i in range(len(nums)):
        nums_bin[i] = []
        while nums[i] > 0:
            temp = nums[i] % 2
            nums_bin[i].append(temp)
            nums[i] = nums[i] // 2

    print(nums_bin)
    distance = dict()

    for index in range(len(nums)):
        count = 0
        distance[index] = []
        i = len(n_bin) - 1
        j = len(nums_bin[index]) - 1
        while i >= 0 & j >= 0:
            if n_bin[i] != nums_bin[i]:
                count += 0
                i -= 1
                j -= 1
        distance[index].append(count)
        # while i < range
        # for i in range(len(n_bin),-1,-1):
        #
        #     if i < len(nums_bin[i]):


