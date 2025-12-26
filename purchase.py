def generate_purchase_recommendations(budget):
    inventory_file = "Book_Info.txt"
    log_file = "logfile.txt"

    # Data structures to hold our analysis
    # book_lookup: { '1': {'title': 'Dune', 'genre': 'Sci-Fi', 'price': 15.0} }
    book_lookup = {}

    # genre_prices: { 'Sci-Fi': [15.0, 18.0, ...], 'Fantasy': [12.0, ...] }
    genre_prices = {}

    # 1. READ INVENTORY (To get Titles, Genres, and Prices)
    try:
        with open(inventory_file, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                # Validation: Ensure line has enough parts and ID is a number
                if len(parts) < 5 or not parts[0].isdigit():
                    continue

                b_id = parts[0].strip()
                genre = parts[1].strip()
                title = parts[2].strip()
                try:
                    price = float(parts[4].strip())
                except ValueError:
                    price = 0.0  # Default if price is invalid

                book_lookup[b_id] = {'title': title, 'genre': genre, 'price': price}

                # Store price to calculate average later
                if genre not in genre_prices:
                    genre_prices[genre] = []
                genre_prices[genre].append(price)

    except FileNotFoundError:
        print(f"Error: {inventory_file} not found. Cannot analyze genres.")
        return

    # 2. READ LOGFILE (To count popularity)
    title_counts = {}
    genre_counts = {}
    total_loans = 0

    try:
        with open(log_file, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                # Skip headers or empty lines
                if len(parts) < 2 or not parts[0].isdigit():
                    continue

                b_id = parts[0].strip()

                # lookup the book details using the ID from the log
                if b_id in book_lookup:
                    book_data = book_lookup[b_id]
                    title = book_data['title']
                    genre = book_data['genre']

                    # Increment counts
                    title_counts[title] = title_counts.get(title, 0) + 1
                    genre_counts[genre] = genre_counts.get(genre, 0) + 1
                    total_loans += 1
                else:
                    # Optional: warning if a log ID doesn't match any known book
                    pass

    except FileNotFoundError:
        print(f"Error: {log_file} not found.")
        return

    # 3. GENERATE REPORT
    if total_loans == 0:
        print("No transactions found.")
        return

    print(f"\n===== PURCHASE ORDER RECOMMENDATION =====")
    print(f"Total Budget: {budget} JOD")
    print(f"Based on analysis of {total_loans} transactions.\n")

    # --- PART A: TOP POPULAR TITLES ---
    print(">> TOP 3 MOST BORROWED TITLES (Buy more copies of these):")
    # Sort titles by count, highest first
    sorted_titles = sorted(title_counts.items(), key=lambda x: x[1], reverse=True)[:3]

    for rank, (title, count) in enumerate(sorted_titles, 1):
        print(f"   {rank}. {title} (Requested {count} times)")

    print("\n>> GENRE BUDGET ALLOCATION:")
    print(f"{'GENRE':<15} | {'DEMAND':<8} | {'BUDGET':<10} | {'SUGGESTED BUY'}")
    print("-" * 60)

    # --- PART B: GENRE ANALYSIS ---
    # Sort genres by popularity
    sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)

    for genre, count in sorted_genres:
        # 1. Calculate Demand Percentage
        demand_percent = count / total_loans

        # 2. Allocate Budget
        allocated_money = budget * demand_percent

        # 3. Calculate Average Price for this Genre
        prices_list = genre_prices.get(genre, [10])  # Default to 10 if error
        avg_price = sum(prices_list) / len(prices_list)

        # 4. Calculate how many copies to buy
        # We use int() to round down to whole books
        copies_to_buy = int(allocated_money / avg_price)

        if copies_to_buy == 0 and allocated_money > 0:
            copies_to_buy = 1  # Suggest at least 1 if there is demand

        print(f"{genre:<15} | {demand_percent * 100:5.1f}%   | {allocated_money:6.2f} JOD | {copies_to_buy} New Books")


# --- EXECUTE ---
# Run the function with a budget of 500 JOD
generate_purchase_recommendations(500)