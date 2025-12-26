table = [
   #table structure
    [
        {"ID": "101"}, {"Author": "J.K. Rowling"}, {"Genre": "Fantasy"}, {"Title": "Harry Potter"}, {"Purchase Price JOD": "15"}, {"Purchase Date": "12/01/2024"}
    ],
    [
        {"ID": "102"}, {"Author": "George Orwell"}, {"Genre": "Dystopian"}, {"Title": "1984"}, {"Purchase Price JOD": "8"}, {"Purchase Date": "05/15/2023"}
    ],
    [
        {"ID": "103"}, {"Author": "Agatha Christie"}, {"Genre": "Mystery"}, {"Title": "Murder on the Orient Express"}, {"Purchase Price JOD": "12"}, {"Purchase Date": "09/22/2025"}
    ],
    [
        {"ID": "104"}, {"Author": "Isaac Asimov"}, {"Genre": "Sci-Fi"}, {"Title": "I, Robot"}, {"Purchase Price JOD": "10"}, {"Purchase Date": "01/30/2026"}
    ]
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
