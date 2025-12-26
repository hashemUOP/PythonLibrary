def member_id_check(member_id):
    # convert passed param to string just in case it was passed as an integer on call
    member_id = str(member_id)

    # member id must only contain decimal values and 4 digit max to be valid
    if member_id.isdigit() and len(member_id) <= 4:
        print("Member ID is valid.")
        print("Welcome back " + member_id)
    else:
        print("Member ID is invalid.")
        exit("Goodbye.") # This stops the program immediately