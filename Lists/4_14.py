all_users = ["User 1", "User 2", "User 3"]
for user in all_users:
    print(user)

print("\nAdding another user to the list")
all_users.append("User 4")
for user in all_users:
    print(user)
print()

untrusted_users = ["User 2", "User 5"]
for user in untrusted_users:
    print(user)
print()

#Creating trusted_users list using a list comprehension
trusted_users = [user for user in all_users]

#Creating trusted_users list using a for loop
trusted_users = []
for user in all_users:
    trusted_users.append(user)

#Sets
all_user = {"Batman", "Superman", "The Flash", "Nightwing", "Joker"}

untrusted_users = {"Zoom", "Joker"}

trusted_users = all_user - untrusted_users

print(trusted_users)
