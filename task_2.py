file = list(open(r'space.txt', encoding='utf-8'))[1:]
index_number = []
for i in range(len(file)):
    index_number += [[int(file[i][5:file[i].index('*')]), i]]
index_number = sorted(index_number)
for i in range(10):
    print(file[index_number[i][1]])
