users = []

def add_user(user_id, name):
    user = {'id': user_id, 'name': name, 'borrowed_books': []}
    users.append(user)
    print(f"User {name} added.")

def list_users():
    if users:
        for user in users:
            print(f"ID: {user['id']} - Name: {user['name']} - Borrowed Books: {len(user['borrowed_books'])}")
    else:
        print("No users registered.")
        
def find_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    return None
