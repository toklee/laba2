with open('books.csv') as a:
    list_books = a.readlines()
tabl = []

for i in range(len(list_books)):
    tabl.append(list_books[i].split(';'))

#print(tabl[0][3])
#print(tabl[0][7])

tabl = tabl[1:]
autor = input()

for num in tabl:
    name_aut = num[3]
    if name_aut == autor:
        price = float(num[7])
        title = num[1]
        if  price < 150:
            print(name_aut,"<",title,">","Цена :",price)
