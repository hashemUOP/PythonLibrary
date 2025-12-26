table = [
    # [
    # {"ID":""},{"Author":""},{"Genre":""},{"Title":""},{"Purchase Price JOD":""},{"Purchase Date":""},
    # ],table structure
]


def insert(id, author, genre, title, purchase_price, purchase_date):
    table.append(
        [
            {"ID": id},
            {"Author": author},
            {"Genre": genre},
            {"Title": title},
            {"Purchase Price JOD": purchase_price},
            {"Purchase Date": purchase_date},
        ]
    )  # this adds data of the book as list of dictionaries to table at its last row


# example of inserting data to table
# insert('0', 'charles', 'horror', 'five trees', '10', '12/26/2026')


def search(title):
    found = False
    for row in table:
        for item in row:
            if item.get("Title") == title:
                found = True
                print(row)

    if not found:
        print("Book not found.")
#example of search usage
# search(input("Enter Title: "))
