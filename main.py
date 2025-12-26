from member import member_id_check
from database import search , insert , table


print("Hello User!")
print("Welcome to our Library System!")
print("==============================")
print("Are you a member? (Y/n)")
if input() == "Y":
    member_id = int(input("Enter Member ID: "))
    member_id_check(member_id)
    print("Choose an option:")
    print("1. Search for a book by title")
    print("2. Add a book to library")
    print("3. See all of the books in the library")
    if input() == "1":
        search(input("Enter Title: "))
    elif input() == "2":
        insert(
            member_id,
            input("Enter Author: "),
            input("Enter Genre: "),
            input("Enter Title: "),
            input("Enter Purchase Price: "),
            input("Enter Purchase Date: ")
        )
        print("Your book has been added to library!")
    elif input() == "3":
        print("All books in library")
        print(table)
    else:
        print("Please enter a valid input")
elif input() == "n":
    print("Thank you! for using our library.")
else:
    print("Please enter a valid input.")

