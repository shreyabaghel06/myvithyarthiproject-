import book_management as bm
import user_management as um
import borrow_return as br
import reporting as rp

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Add User")
        print("4. List Users")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Borrowed Books Report")
        print("8. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            copies = int(input("Copies: "))
            bm.add_book(book_id, title, author, copies)
        elif choice == "2":
            bm.list_books()
        elif choice == "3":
            user_id = input("User ID: ")
            name = input("Name: ")
            um.add_user(user_id, name)
        elif choice == "4":
            um.list_users()
        elif choice == "5":
            user_id = input("User ID: ")
            book_id = input("Book ID: ")
            br.borrow_book(user_id, book_id)
        elif choice == "6":
            user_id = input("User ID: ")
            book_id = input("Book ID: ")
            br.return_book(user_id, book_id)
        elif choice == "7":
            rp.borrowed_books_report()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
