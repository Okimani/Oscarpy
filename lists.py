from array import array # this has got  nothing to do with lists. it is for the arrays below the lists
names = ['Margaret', 'George', 'Richard'] #This is how you create lists in python
scores = [] # creating an empty list
scores.append(100)
scores.append(70)
scores.append(50)
scores.append(20)
my_numbers = [2, 5,6]
print(my_numbers)
print(names)
print(scores)
print(scores[3]) # prints the 4th item at index 3, indexes start from 0
print(names[2]) # This will print George which is at index 2

#Python also supports arrays you just run the from array import array command
item = array('d') #Indicate the numeric data type we're gonna be using in this case 'double'
item.append(98)
item.append(99)
item.append(100)
print(item)
print(item[2])https://github.com/Okimani/Oscarpy/tree/master
#Difference between arrays and lists is that arrays allow you to store numeric data types
#and everything in there has to be the same data type. 
#Lists on the other hand enable you to store anything.

#Below is a list of common operations on lists and their output
print(len(names)) # this will give you an output of 3 that is Margaret , Oscar and Gianna
names.insert(0, 'Joyce') #This inserts Joyce at Index 0
print(names)
print(len(names))
names.sort() #sorts the names in the list alphabetically
print(names)
# You can also grab a range from a list
moms_family_members = (names[1:3]) #prints the 2nd and 3rd on the alphabetic list
#Another shortcut you can use is just to indicate (names[:3])
print(names)
print(moms_family_members)
names.append('Brenda') #appending adds to the end of the list
print(names)
print(names[:4])
names.insert(2, 'Stranger') #Inserts stranger at index 2 becoming the item
# at index 2, that is third item
print(names)
