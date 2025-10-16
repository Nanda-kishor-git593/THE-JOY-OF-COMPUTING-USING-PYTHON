
#linar_search

def linear_search(n, x):
    element = []
    for i in range(1, n + 1):  # Includes n in the list [1, n]
        element.append(i)
    print(element)
    count = 0
    flag = 0
    for i in element:
        count += 1
        if i == x:
            print("Yes! I found my number at position :", str(i))
            flag = 1
            break
    if flag == 0:
        print("Number is Not found")
    print("Number of iterations:", count)

a = int(input("Enter the n value: "))
b = int(input("Enter the value (element) to find in list: "))
linear_search(a, b)

