def bubble(arr):
    for i in range(len(arr)):
        j = i + 1
        while j < len(arr) and arr[j] < arr[i]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    return arr


def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]
test_arr = [2, 1, 5, 3, 4, 7]

bubbleSort(test_arr)

print("排序后的数组:")
for i in range(len(test_arr)):
    print("%d" % test_arr[i]),


print(bubble(test_arr))