price = input('how much did you pay? ')

price = float(price) #convert price to float since input function has everything as string by default
if price >= 4.00:
    tax = .07

else:
    tax = 0
print('Tax rate is: ' + str(tax)) #When u concatenate with a string you put the str before variable
    
x, y, z, = "Gender" , "Weight", "height"
print (x)
print(y)
print(z)
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
