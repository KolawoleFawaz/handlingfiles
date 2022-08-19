

def calc(text_file):
    data = []
    f = open(text_file)
    data +=f.read().split()
    return len(data)


res = calc(r'C:\Users\FAWASI PC\Downloads\python.txt')
print(res)