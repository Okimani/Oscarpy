from datetime import datetime, timedelta
#print task completed, print date and time and a space into  a function

def print_time():
    print('Task Completed')
    print(datetime.now())
    print()

first_name = 'Oscar'
initial =first_name[0:2].upper()
print(first_name)
print_time()
for x in range (0, 6):
    print(x)
print_time()

for y in range(0,5,2): #the 2 is the step during execution it will step 2 digits
     print(y)

print(initial)