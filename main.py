from member import member_id_check
from database import search, insert, table

print("Hello User!")
print("Welcome to our Library System!")
print("==============================")
print("Are you a member? (Y/n)")

is_member = input()

if is_member == "Y":
    member_id = input("Enter Member ID: ")
    member_id_check(member_id)

    print("Choose an option:")
    print("1. Search for a book by title")
    print("2. Add a book to library")
    print("3. See all of the books in the library")

    choice = input("Enter choice: ")

    if choice == "1":
        search(input("Enter Title: "))
    elif choice == "2":
        insert()
        print("Your book has been added to library!")
    elif choice == "3":
        print("All books in library")
        print(table)
    else:
        print("Please enter a valid input")

elif is_member == "n":
    print("Thank you! for using our library.")
else:
    print("Please enter a valid input.")