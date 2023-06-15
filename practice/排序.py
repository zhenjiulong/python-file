#选择排序
# def selectionsort(a):
#     n = len(a)
#     for i in range(n-1):
#         min = i
#         for j in range(i+1,n):
#             if a[j] < a[min]:
#                 min = j
#         a[i],a[min] = a[min],a[i]
#         print(a)
#
# a = [9,11,13,4,6,5,7,12,1,10,2,8,3,16,14]
#
# selectionsort(a)
#冒泡排序
def poposort(b):
    for i in range(len(b)-1,-1,-1):
        for j in range(i):
            if b[j] > b[j+1]:
                b[j],b[j+1] = b[j+1],b[j]
        print(b)
# b = [9,11,13,4,6,5,7,12,1,10,2,8,3,16,14]
# poposort(b)
#插入排序
# def insertsort(a):
#     n = len(a)
#     for i in range(1,n):
#         x = a[i]
#         j = i-1
#         while j >= 0 and x <=a[j]:
#             a[j+1] = a[j]
#             j-=1
#         a[j+1] = x
#     print(a)
# a= [9,11,13,4,6,5,7,12,1,10,2,8,3,16,14]
# insertsort(a)
#归并排序
def merge(a,start,mid,end):
    tmp = []
    l = start
    r = mid+1
    while l <= mid and r <= end:
        if a[l] <= a[r]:
            tmp.append(a[l])
            l += 1
        else:
            tmp.append(a[r])
            r += 1
    tmp.extend(a[l:mid+1])
    tmp.extend(a[r:end+1])
    for i in range(start,end+1):
        a[i] = tmp[i-start]
    print(start,end,tmp)

def mergesort(a,start,end):
    if start == end:
        return
    mid = (start+end)//2
    mergesort(a,start,mid)
    mergesort(a,mid+1,end)
    merge(a,start,mid,end)

a=[9,8,7,6,3,1,4,5]
mergesort(a,0,7)