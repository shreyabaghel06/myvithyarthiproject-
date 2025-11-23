books = []

def add_book(book_id, title, author, copies):
    book = {'id': book_id, 'title': title, 'author': author, 'copies': copies}
    books.append(book)
    print(f"Added book '{title}'.")

def list_books():
    if books:
        for book in books:
            print(f"ID: {book['id']} - Title: {book['title']} by {book['author']} (Copies: {book['copies']})")
    else:
        print("No books available.")
