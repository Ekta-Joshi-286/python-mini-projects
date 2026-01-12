# Movie Ticket Booking System

# Step 1: Represent seats in a 2D list (O = available, X = booked)
seats = [
    ["O", "O", "O", "O", "O"],  # Row 1
    ["O", "O", "O", "O", "O"],  # Row 2
    ["O", "O", "O", "O", "O"]   # Row 3
]

# Step 2: Define seat prices
# (Row 1 = Premium ₹200, Row 2 = Standard ₹150, Row 3 = Economy ₹100)
prices = [200, 150, 100]

# Step 3: Display seats
def display_seats():
    print("\n------ CINEMA SEAT LAYOUT ------")
    for i, row in enumerate(seats):
        print(f"Row {i+1}: {' '.join(row)}")

# Step 4: Book a seat
def book_seat():
    display_seats()
    row = int(input("Enter row number (1-3): ")) - 1
    col = int(input("Enter seat number (1-5): ")) - 1

    if seats[row][col] == "X":
        print("❌ Seat already booked! Please choose another.")
    else:
        seats[row][col] = "X"
        print(f"✅ Seat booked successfully! Price: ₹{prices[row]}")

# Step 5: Main program loop
while True:
    print("\n------ MOVIE TICKET MENU ------")
    print("1. View Seats")
    print("2. Book Seat")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        display_seats()
    elif choice == "2":
        book_seat()
    elif choice == "3":
        print("🎬 Thank you for booking! Enjoy your movie!")
        break
    else:
        print("Invalid choice. Try again.")
