

#result = 7*5-9+12/3+32**2
#print(result)


#salary = 2555
#result = salary + float(40)
#print(result)


#lists = [1,2,3,4,5]
#print(lists[3])


#operas = {'Magice Flute': 'Mozart',
 #         'La Traviata': 'Verdi',
  #        'Barbar of Seville': 'Rossini'}
#print(operas)
#print(operas['La Traviata'])

#operas['Tosca'] = 'Puccini'
#print(operas)
#--------------------------------Practice--------------------------------------


print('****Travel Itinerary****')

city1 = input('Enter the name of the first city: ')
country1 = input('Enter the name of the first country: ')
duration1 = int(input('Enter the duration of stay (in days) for the first city: '))
budget1 = int(input('Enter the budget (in dollars) for the first city:$ ' ))


city2 = input('Enter the name of the second city: ')
country2 = input('Enter the name of the second country: ')
duration2 = int(input('Enter the duration of stay (in dollars) for the second city: '))
budget2 = int(input('Enter the budget (in dollars) for the second city: ' ))

city3 = input('Enter the name of the third city: ')
country3 = input('Enter the name of the third country: ')
duration3 = int(input('Enter the duration of stay (in days) for the third city: '))
budget3 = int(input('Enter the budget (in dollars) for the third city: ' ))


dictionary1 = {'City': city1,
               'Country': country1,
               'Duration': duration1,
               'bduget': budget1}
dictionary2 = {'City': city2,
               'Country': country2,
               'Duration': duration2,
               'Budget': budget2}
dictionary3 = {'City': city3,
               'Country': country3,
               'Duration': duration3,
               'Budget': budget3}

destinationList1 = [city1, country1, duration1, budget1]
destinationList2 = [city2, country2, duration2, budget2]
destinationList3 = [city3, country3, duration3, budget3]
              
print('***Itinerary Check-Out 1***')
print('City:', destinationList1[0])
print('Country:', destinationList1[1])
print(f'Duration: {destinationList1[2]} days')
print(f'Budget: ${destinationList1[3]}')

print('***Itinerary Check-Out 2***')
print('City:', destinationList2[0])
print('Country:', destinationList1[1])
print(f'Duration: {destinationList2[2]} days')
print(f'Budget: ${destinationList2[3]}')

print('***Itinerary Check-Out 3***')
print('City:', destinationList3[0])
print('Country:', destinationList3[1])
print(f'Duration: {destinationList3[2]} days')
print(f'Budget: ${destinationList3[3]}')

















  
