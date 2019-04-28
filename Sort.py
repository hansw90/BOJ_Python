""""
정렬만큼 알고리즘의 효율성 차이를 명확하게 보여주는 것이 없기 때문에 알고리즘 부터 배운다

선택정렬,버블정렬,삽입정열

""""


#선택정렬
def sel_sort(a) :
    n = len(a)
    for i in range(0,n-1) :
        min_idx = i
        for j in range(i+1,n) :
            if a[j]<a[min_idx] :
                min_idx = j
        a[i],a[min_idx] = a[min_idx],a[i]
        print(a)

d = [10,4,5,6,1,2,3,8,9,7]
sel_sort(d)
print(d)


# 내림차순 삽입 정렬
def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] < key: # 부등호 방향 뒤집기
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
d = [10,4,5,6,1,2,3,8,9,7]
ins_sort(d)
print(d)


# 퀵 정렬


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


print(quick_sort([3,4,5,7,8,1,2]))
