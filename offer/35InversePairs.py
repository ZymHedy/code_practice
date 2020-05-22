# 传统的归并排序

def mergesort(data):
    if len(data) < 2:
        return data
    mid = len(data) // 2
    left = mergesort(data[0:mid])
    right = mergesort(data[mid:])
    return merge(left, right)


def merge(left, right):
    count = 0
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            count += 1
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


data = [7,6,5,4]
print(mergesort(data))
