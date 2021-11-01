# You can create a function to perform the operation below. 
#first_name =input('Enter your first name ')
#first_name_initial = first_name[0:1]
#last_name = input('Enter your last name ')
#last_name_initial = last_name[0:1]
#print('Your initials are: ' + first_name_initial + last_name_initial)
#print(first_name)
#print(last_name)
#Now lets represent this in a function
#Note that you can include the parameter when calling it in this case name 
#This was not in the previous code. 

def get_initial(name):
    initial= name[0:1]
    return initial
first_name =input('Enter your first name ')
first_name_initial = get_initial(name =first_name)
last_name = input('Enter your last name ')
last_name_initial = get_initial(name =last_name)

print('Your initials are:' + first_name_initial + last_name_initial)

