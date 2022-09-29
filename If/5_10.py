current_users = ["User 1", "User 2", "User 3", "User 4", "noobmaster69"]
new_users = ["User 6", "Deez", "NOOBMASTER69", "User 1", "Nutz"]

temp_list_for_comparison = []
for current in current_users:
    temp_list_for_comparison.append(current.lower())
 
for new in new_users:
    if new.lower() in temp_list_for_comparison:
        print(f"{new} is already being used. Please enter a new username.")
    else:
        print(f"Username {new} is available.")
