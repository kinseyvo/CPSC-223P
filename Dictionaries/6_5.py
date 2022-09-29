major_rivers = {'nile': 'egypt', 'amazon': 'south america', 'yangtze': 'china'}

#Loop to print a sentence about each river
for river, location in major_rivers.items():
    print(f"The {river.title()} runs through {location.title()}.")

print()

#Loop to print the name of each river included in the dictionary
for river in major_rivers.keys():
    print(river.title())

print()

#Loop to print the name of each country included in the dictionary
for location in major_rivers.values():
    print(location.title())