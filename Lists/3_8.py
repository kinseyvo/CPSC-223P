want_to_visit = ["New York", "Hawaii", "Washington", "Japan", "Canada"]
print(want_to_visit)

#Use sorted() to print  list in alphabetical order without modifying the actual list
print(sorted(want_to_visit))

#Printing original order of list
print(want_to_visit)

#Use sorted() to print  list in reverse alphabetical order without changing the order of the original list
print(sorted(want_to_visit, reverse = True))

#List is still in its original order by printing it again
print(want_to_visit, "\n")

#Use reverse to change the order of your list
want_to_visit.reverse()
print(want_to_visit, "\n")

#Reestablish original list
want_to_visit.reverse()
print(want_to_visit, "\n")

#Combination of remove() and sorted() to remove the alphabetically first occurring value
want_to_visit.remove(sorted(want_to_visit)[0])
print(want_to_visit, "\n")

#Use sort() to change list so it’s stored in alphabetical order 
want_to_visit.sort()
print(want_to_visit, "\n")

#Use sort() to change your list so it’s stored in reverse alphabetical order
want_to_visit.reverse()
print(want_to_visit)