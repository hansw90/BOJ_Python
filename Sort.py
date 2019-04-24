""""
정렬만큼 알고리즘의 효율성 차이를 명확하게 보여주는 것이 없기 때문에 알고리즘 부터 배운다

선택정렬,버블정렬,삽입정열

""""


"""
선택정렬

"""

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
