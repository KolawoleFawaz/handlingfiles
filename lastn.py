contents=[]
def tail(contents,n):
    with open(r'C:\Users\FAWASI PC\Downloads\python.txt') as file:
        for x in file.readlines():
            contents.append(x)

    for x in contents[:n:-1]:
        print(x)

tail(contents,-3)