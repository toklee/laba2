with open('books.csv') as a:
    list_books = a.readlines()
tabl = []

for i in range(len(list_books)):
    tabl.append(list_books[i].split(';'))
#print(tabl[0][1])
count=0
for number in range(len(tabl)):
    if len(tabl[number][1]) > 30:
        count += 1
print(count)