# Task_1
def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        end -= 1
        swapped = False
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1
    return arr
arr = [5, 1, 4, 2, 8, 0, 2]
print(cocktail_sort(arr))

# Task_2
def merge_sort(arr):
    def merge(low, mid, high):
        temp = []
        i = low
        j = mid + 1
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= high:
            temp.append(arr[j])
            j += 1
        for k in range(low, high + 1):
            arr[k] = temp[k - low]
    def sort(low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid + 1, high)
        merge(low, mid, high)
    sort(0, len(arr) - 1)
    return arr
arr = [12, 11, 13, 5, 6, 7]
print(merge_sort(arr))
