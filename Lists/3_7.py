invites = ["Grant Gustin", "Christian Bale", "Henry Cavill"]
for invite in invites:
	print(f"{invite.title()}, I’d like to invite you to dinner.")

print(f"{invites[0].title()} unfortunately cannot make it to dinner since he recently became a father.")

invites[0] = "Stephen Amell"

print("\nNew Guest list:")

for invite in invites:
	print(f"{invite.title()}, I’d like to invite you to dinner.")

print("\nBREAKING NEWS: A BIGGER TABLE HAS BEEN ACQUIRED!")

invites.insert(0, "Brenton Thwaites")
invites.insert(1, "Conor Lesile")
invites.append("Margot Robbie")

for invite in invites:
	print(f"{invite.title()}, I’d like to invite you to dinner.")

print(f"\nThere are {len(invites)} invites in the list.")
print("Unfortunately, due to restrictions I can only invite 2 guests.\n")

print(f"{invites.pop()} you're no longer invited")
print(f"{invites.pop()} you're no longer invited")
print(f"{invites.pop()} you're no longer invited")
print(f"{invites.pop()} you're no longer invited")
print("\n")

for invite in invites:
	print(f"{invite.title()}, you're still invited to dinner.")

print("\nRemoving Names to get Empty List")
invites.remove("Conor Lesile")
del invites[0]

print(invites)