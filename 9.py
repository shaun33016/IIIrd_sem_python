def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

n=int(input("Enter the number of elements:"))
arr=[0]*n
print("Enter the elements")
for i in range(0,n):
    arr[i]=int(input())
x = int(input("Enter the number to be searched: "))
result = binary_search(arr, x)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in the list")
