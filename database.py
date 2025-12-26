from datetime import datetime


def read_books():
    """
    Returns all books in library
    """
    filename = "Book_Info.txt"
    books = []
    try:
        with open(filename, "r") as file:
            books = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        # Return an empty list so the program doesn't crash
        return []
    except Exception as e:
        print(f"An error occurred while reading the database: {e}")
        return []

    return books

#example of usage
# print(read_books())

def checkout_book(book_id, member_id):

    filename = "logfile.txt"
    current_date = datetime.now().strftime("%d/%m/%Y")

    # We need to check if the book is currently available before adding a new line.
    is_available = True

    try:
        with open(filename, "r") as file:
            books = file.readlines()

            # Skip the header if it exists
            # (Assuming the first line might be headers, but your data starts with ID 1)

            for line in books:
                line = line.strip()
                if not line or line.startswith("bookID"): continue

                parts = line.split(",")

                # Check formatting safety
                if len(parts) < 5: continue

                b_id = parts[0].strip()
                return_date = parts[3].strip()
                reservation_status = parts[4].strip()

                # Logic: If we find this book ID, check its status
                if b_id == str(book_id):
                    # 1. Is it currently out? (Return Date is '-')
                    if return_date == "-":
                        print(f"Cannot checkout: Book {book_id} is currently out.")
                        is_available = False
                        break

                    # 2. Is it reserved by someone else?
                    # The format is "Reserved by XXXX" or "None"
                    if "Reserved by" in reservation_status:
                        # Optional: Check if the person reserving it is the current user
                        reserver = reservation_status.split("Reserved by ")[1]
                        if reserver != str(member_id):
                            print(f"Cannot checkout: Book {book_id} is reserved by member {reserver}.")
                            is_available = False
                            break

        # If the book is safe to check out, append the new transaction
        if is_available:
            with open(filename, "a") as file:  # 'a' mode appends to the end of the file
                # Format: bookID,memberID,checkoutDate,returnDate,reservation
                # Your request said: "put book is reserved by user_id"
                new_entry = f"\n{book_id},{member_id},{current_date},-,Reserved by {member_id}"
                file.write(new_entry)
                print(f"Success! Book {book_id} checked out to member {member_id}.")

    except FileNotFoundError:
        print("Error: Database file not found.")

# Example Usage:
# checkout_book("199", "9999")
# checkout_book("99", "9999")

def returned_book(book_id):
    filename = "logfile.txt"
    updated_lines = []
    book_found = False

    current_date = datetime.now().strftime("%d/%m/%Y")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        for line in lines:
            # Clean up line and skip empty ones
            stripped_line = line.strip()
            if not stripped_line:
                continue

            parts = stripped_line.split(",")

            # Ensure safe parsing (needs at least 5 columns)
            if len(parts) >= 5:
                current_book_id = parts[0].strip()
                return_date = parts[3].strip()

                # We are looking for the specific book ID AND a line where it hasn't been returned yet
                if current_book_id == str(book_id) and return_date == "-":
                    print(f"Returning book {book_id}...")

                    # Update Return Date to today
                    parts[3] = current_date

                    # Update Reservation to None
                    parts[4] = "None"

                    book_found = True

                    # Reconstruct the line
                    new_line = ",".join(parts) + "\n"
                    updated_lines.append(new_line)
                else:
                    # Keep the line exactly as it was
                    updated_lines.append(line)
            else:
                updated_lines.append(line)

        # Write changes back to file ONLY if we found the book
        if book_found:
            with open(filename, "w") as file:
                file.writelines(updated_lines)
            print(f"Success: Book {book_id} has been returned and reservation cleared.")
        else:
            print(f"Error: Could not find an active checkout for Book ID {book_id}.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Example Usage:
# returned_book("99")

def add_book(genre, title, author, price, purchase_date):
    filename = "Book_Info.txt"

    # 1. Calculate the New ID
    new_id = 1  # Default if file is empty

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

            # We need to find the highest ID currently in the file
            ids = []
            for line in lines:
                parts = line.strip().split(",")
                # Skip header or empty lines
                if not line.strip() or not parts[0].isdigit():
                    continue
                ids.append(int(parts[0]))

            if ids:
                new_id = max(ids) + 1

    except FileNotFoundError:
        # If file doesn't exist, we will create it when writing
        pass

    # 2. Append the new book
    try:
        with open(filename, "a") as file:
            # Format: ID,Genre,Title,Author,Purchase Price JOD,Purchase Date
            new_entry = f"{new_id},{genre},{title},{author},{price},{purchase_date}\n"
            file.write(new_entry)
            print(f"Success: Added '{title}' with ID {new_id}.")

    except Exception as e:
        print(f"An error occurred: {e}")


# --- Example Usage ---
# You can call it like this:
# add_book("Sci-Fi", "Project Hail Mary", "Andy Weir", "20", "26/12/2025")
# add_book("Tech", "Clean Code", "Robert C. Martin", "35", "26/12/2025")

