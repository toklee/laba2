with open('books.csv') as a:
    list_books = a.readlines()

tabl = []
for i in range(len(list_books)):
    tabl.append(list_books[i].split(';'))
k = 1

for num in range(1, len(tabl)):
    if k < 21:
        print(num, tabl[num][3], '<', tabl[num][1], '>', tabl[num][6])
        k += 1