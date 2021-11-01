#come_from_africa = '' #Apparently this code works whether we have initialized this or not
country = input('What country do you come from? ' )
if country.capitalize() in('Kenya', 'Ethiopia','Morocco'):
    come_from_africa = True
else:
    come_from_africa = False

if come_from_africa:
    print('You come from the African continent')

else:
    print('You are not from the African Continent')






