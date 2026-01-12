# Library Management System

library = []   # List to store all books
issued_books = []  # List to track issued books

while True:
    print("\n------ LIBRARY MENU ------")
    print("1. Add New Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Show All Books")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # 1. Add New Book
    if choice == '1':
        title = input("Enter book title: ").title()
        author = input("Enter author name: ").title()
        book = {'title': title, 'author': author}
        library.append(book)
        print(f"✅ '{title}' by {author} added to library!")

    # 2. Issue Book
    elif choice == '2':
        title = input("Enter book title to issue: ").title()
        found = False
        for book in library:
            if book['title'] == title:
                issued_books.append(book)
                library.remove(book)
                print(f"📘 '{title}' has been issued!")
                found = True
                break
        if not found:
            print("Book not available or already issued!")

    # 3. Return Book
    elif choice == '3':
        title = input("Enter book title to return: ").title()
        found = False
        for book in issued_books:
            if book['title'] == title:
                library.append(book)
                issued_books.remove(book)
                print(f"📗 '{title}' has been returned!")
                found = True
                break
        if not found:
            print("This book was not issued!")

    # 4. Search Book
    elif choice == '4':
        keyword = input("Enter title or author to search: ").title()
        found = False
        print("\nSearch Results:")
        for book in library + issued_books:
            if keyword in book['title'] or keyword in book['author']:
                print(f"Title: {book['title']}, Author: {book['author']}")
                found = True
        if not found:
            print("No matching books found!")

    # 5. Show All Books
    elif choice == '5':
        print("\n📚 Available Books:")
        if library:
            for book in library:
                print(f"- {book['title']} by {book['author']}")
        else:
            print("No books available right now!")

        print("\n📕 Issued Books:")
        if issued_books:
            for book in issued_books:
                print(f"- {book['title']} by {book['author']}")
        else:
            print("No books issued currently!")

    # 6. Exit
    elif choice == '6':
        print("👋 Goodbye! Thank you for using Library System.")
        break

    else:
        print("Invalid choice! Please try again.")
