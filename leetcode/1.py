# 输出单科最高成绩，以及需要表彰人数
while 1:
    nm = input()
    if nm != '':
        n, m = map(int, nm.split())
        student_score = dict()
        for i in range(n):
            student_score[i] = []
            for s in input().split():
                student_score[i].append(int(s))

        # print('n:{},m:{}'.format(n,m))
        print(student_score)
        subject = dict()
        max_score = []
        for i in range(m):
            subject[i] = []
            for j in range(n):
                subject[i].append(student_score[j][i])
            subject[i] = sorted(subject[i])
            max_score.append(subject[i][-1])
        # print(subject)

        count = []
        for i in range(n):
            for j in range(m):
                if max_score[j] == student_score[i][j]:
                    count.append(i)
        print(max_score)
        print(count)
        print(len(set(count)))
