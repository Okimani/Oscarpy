#orking with dictionaries
students = {"fname": "Jacob", "lname": "Michael",}
print(students)
first_name =students["fname"]
print(first_name)
print(students["lname"])
#looping through key and value
for firstname, lastname in students.items():
    print(firstname, lastname)

#looping through keys only
for firstname in students.keys():
    print(firstname)

#looping through values only
for firstname in students.values():
    print(firstname)
