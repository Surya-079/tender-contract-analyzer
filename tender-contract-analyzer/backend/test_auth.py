from backend.auth import *
create_database()
print(register_user("Surya", "7979"))
print(login_user("Surya", "7979"))
print(login_user("Surya", "abcd"))
