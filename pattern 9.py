num= int(input("Enter the number of rows: "))
for i in range(num):
    for j in range(num-i):
        print(end=' ')
    for k in range(num-j):
        print('*',end=' ')
    print()