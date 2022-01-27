import itertools

orders = 0
books = ['calculus', 'physics', 'chemistry', 'history', 'literature', 'french', 'astronomy']
books.sort()
s = []
for a in books:
    for b in books:
        if a != b:
            for c in books:
                if c != a and c != b:
                    for d in books:
                        if d != a and d != b and d != c:
                            orders += 1
                            s.append([a, b, c, d])

print(orders)
for x in s:
    print(x)
    pass

print("----------------------------")

book_orders = []
for a in books:
    for b in books:
        if a != b:
            for c in books:
                if c != a and c != b:
                    for d in books:
                        if d != a and d != b and d != c:
                            orders += 1
                            t_order = [a, b, c, d]
                            t_order.sort()
                            if t_order not in book_orders:
                                book_orders.append(t_order)

for x in book_orders:
    print("\item " + "$[$ " + x[0] + ", " + x[1] + ", " + x[2] + ", " + x[3] + " $]$")

print(len(book_orders))
