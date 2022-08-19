file_name = open(r'C:\Users\FAWASI PC\Downloads\python.txt')
n = int(input("Enter number of first n lines: "))

for i in range(n):
    print(file_name.readline())

