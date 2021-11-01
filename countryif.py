country = input('What country do you come from? ' )
if country.capitalize() in('Kenya', 'Tanzania','Morocco'):
    print('You come from the African Continent')

elif country.capitalize() in ('Malta', 'Germany', 'SPain'):
    print('You come from the European continent')

elif country.capitalize() in ('Bolivia', 'Brazil', 'Argentina'):
    print('You come from the South American Continent')
    

else:
    print('Country is not on the List')
