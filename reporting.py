from user_management import users

def borrowed_books_report():
    print("Borrowed Books Report:")
    for user in users:
        if user['borrowed_books']:
            print(f"{user['name']} has borrowed:")
            for book in user['borrowed_books']:
                print(f" - {book['title']} by {book['author']}")
        else:
            print(f"{user['name']} has no books borrowed.")
