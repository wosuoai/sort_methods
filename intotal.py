class Solution:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return
        A.sort()


#冒泡排序
class bubble_sort:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return

        for i in range(len(A) - 1):
            for j in range(len(A) - 1 - i):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]


#选择排序
class select_sort:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return
        for i in range(len(A)):
            tmp = i
            for j in range(i + 1, len(A)):
                if A[j] < A[tmp]:
                    tmp = j
            A[i], A[tmp] = A[tmp], A[i]


#插入排序
class insert_sort:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return
        for i in range(1, len(A)):
            for j in range(i - 1, -1, -1):
                if A[i] < A[j]:
                    A[i], A[j] = A[j], A[i]
                    i = j
                else:
                    break


#希尔排序
class shell_sort:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return
        dk = len(A) // 2
        while dk >= 1:
            self.InsertSort(A, dk)
            dk = dk // 2

    def InsertSort(self, A, dk):
        for i in range(dk):
            for j in range(i, len(A), dk):
                for k in range(j - 1, -1, -dk):
                    if A[j] < A[k]:
                        A[j], A[k] = A[k], A[j]
                        j = k
                    else:
                        break


#合并排序
class merge_sort:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return
        tmp = [0] * len(A)
        self.mergeSort(A, 0, len(A) - 1, tmp)

    def mergeSort(self, A, start, end, tmp):
        if start >= end:
            return

        self.mergeSort(A, start, (start + end) // 2, tmp)
        self.mergeSort(A, (start + end) // 2 + 1, end, tmp)

        self.merge(A, start, end, tmp)

    def merge(self, A, start, end, tmp):
        mid = (start + end) // 2
        leftIndex = start
        rightIndex = mid + 1
        index = leftIndex

        while leftIndex <= mid and rightIndex <= end:
            if A[leftIndex] <= A[rightIndex]:
                tmp[index] = A[leftIndex]
                leftIndex += 1
            else:
                tmp[index] = A[rightIndex]
                rightIndex += 1
            index += 1

        while leftIndex <= mid:
            tmp[index] = A[leftIndex]
            index += 1
            leftIndex += 1
        while rightIndex <= end:
            tmp[index] = A[rightIndex]
            index += 1
            rightIndex += 1

        for index in range(start, end + 1):
            A[index] = tmp[index]


#快速排序
class quick_sort:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return
        self.quickSort(A, 0, len(A) - 1)

    def quickSort(self, A, start, end):
        if start >= end:
            return

        left, right = start, end
        pivot = A[(start + end) // 2]

        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        self.quickSort(A, start, right)
        self.quickSort(A, left, end)


#堆排序
class heap_sort:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return
        A.insert(0, 0)

        lenA = len(A) - 1
        dk = lenA // 2
        for i in range(dk):
            self.heapAdjust(A, dk - i, lenA)

        for i in range(lenA - 1):
            A[1], A[lenA - i] = A[lenA - i], A[1]
            self.heapAdjust(A, 1, lenA - i - 1)

        A.remove(0)

    def heapAdjust(self, A, start, end):
        tmp = A[start]

        i = start
        j = 2 * i

        while j <= end:
            if j < end and A[j] < A[j + 1]:
                j += 1
            if tmp < A[j]:
                A[i] = A[j]
                i = j
                j = 2 * i
            else:
                break

        A[i] = tmp


#计数排序
class counting_sort:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return

        minA = min(A)
        maxA = max(A)

        L = [0] * (maxA - minA + 1)

        for i in range(len(A)):
            L[A[i] - minA] += 1

        index = 0
        for i in range(len(L)):
            while L[i] > 0:
                A[index] = minA + i
                index += 1
                L[i] -= 1


#桶排序
class bucket_sort:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return

        n = 100
        new_list = [[] for _ in range(n)]
        minA = min(A)

        for data in A:
            index = (data - minA) // 100
            new_list[index].append(data)

        for i in range(n):
            new_list[i].sort()

        index = 0
        for i in range(n):
            for j in range(len(new_list[i])):
                A[index] = new_list[i][j]
                index += 1


#基数排序
class radix_sort:
    def sortIntegers(self, A):
        if A == None or len(A) == 0:
            return

        maxA = max(A)

        d = 0
        while maxA // 10 > 0:
            d += 1
            maxA = maxA // 10
        d += 1

        for i in range(d):
            s = [[] for _ in range(10)]
            for data in A:
                s[data // (10 ** i) % 10].append(data)
            index = 0
            for j in s:
                for k in j:
                    A[index] = k
                    index += 1
