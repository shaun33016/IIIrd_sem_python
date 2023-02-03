def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1 - i):
            if (list[j] > list[j+1]):
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def main():
    n=int(input("Enter number of elements"))
    list=[0]*n
    print("Enter the elements: ")
    for i in range(0,n):
        list[i]=int(input())
    print(list)
    bubbleSort(list)
    print(list)


main()
