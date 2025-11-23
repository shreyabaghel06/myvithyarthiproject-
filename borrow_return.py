from book_management import books
from user_management import find_user

def borrow_book(user_id, book_id):
    user = find_user(user_id)
    if not user:
        print("User not found.")
        return
    for book in books:
        if book['id'] == book_id:
            if book['copies'] > 0:
                book['copies'] -= 1
                user['borrowed_books'].append(book)
                print(f"{user['name']} borrowed '{book['title']}'.")
                return
            else:
                print("No copies available.")
                return
    print("Book not found.")

def return_book(user_id, book_id):
    user = find_user(user_id)
    if not user:
        print("User not found.")
        return
    for book in user['borrowed_books']:
        if book['id'] == book_id:
            user['borrowed_books'].remove(book)
            # Return copies
            for b in books:
                if b['id'] == book_id:
                    b['copies'] += 1
            print(f"{user['name']} returned '{book['title']}'.")
            return
    print("User does not have this book borrowed.")
