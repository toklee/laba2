with open('books-en.csv') as a:
    list_books = a.readlines()
tabl = []

for i in range(len(list_books)):
    tabl.append(list_books[i].split(';'))
popular = []

for num in range(1,len(tabl)):
    popular.append(int(tabl[num][-2]))
MAXPOP = max(popular)
count = 0

for title in range(1,len(tabl)):
    if count<20 and int(tabl[title][-2]) == MAXPOP:
        print(tabl[title][1])
        count+=1

