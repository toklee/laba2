with open('books-en.csv') as a:
    list_books = a.readlines()
tabl = []

for i in range(len(list_books)):
    tabl.append(list_books[i].split(';'))
publishers = []

for publ in range(1,len(tabl)):
    if not(tabl[publ][4] in publishers):
        publishers.append(tabl[publ][4])
print(publishers)

