def indexOfSmallestElement(list):
    index = 0
    for i in range(len(list)):
        if (list[i] < list[index]):
            index = i
    return index
def main():
    n = int(input("Enter n: "))
    list = []
    for i in range(n):
        list.append(int(input()))
    print(list)
    print("Index of smallest element is", indexOfSmallestElement(list) + 1)
main()
